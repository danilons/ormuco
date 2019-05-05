import scrapy
import nltk
import re
from scrapy.selector import Selector
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
import tldextract

class InsightSpider(scrapy.Spider):
	name = "insights"
	base_url = "https://www.google.com/search?q={}&oq={}"
	
	stop_words = set(stopwords.words() +  # english stopwords are loaded by default
	                 nltk.corpus.stopwords.words('portuguese') + # custom language (should be configurable)
	                 ["function", "var", "http", "https", "span", "typeof", "div"]) # html and js stuff to be removed

	# Restricted some domains that might not be useful
	unallowed_domains = ["youtube", "facebook"]

	lemma = WordNetLemmatizer()

	def __init__(self, search_term="insights", *args, **kwargs):
		super(InsightSpider, self).__init__(*args, **kwargs)
		self.start_urls = [self.base_url.format(search_term, search_term)]
		self.logger.info("Start url: {}".format(self.start_urls))	

	def parse(self, response):
		selector = Selector(response)
		selected = selector.xpath('//div[@id="ires"]//div[@class="g"]//h3[@class="r"]')

		links = {}
		for sel in selected:
			raw_url = sel.xpath(".//a/@href").extract_first()
			if raw_url:
				url = raw_url.replace('/url?q=', '')
				url = re.sub(r"\/([^\/]+)$", "", url)
				if url is None or len(url.strip()) <= 1:
					continue
				meta = tldextract.extract(url)
				if meta.domain not in self.unallowed_domains:
					links[meta.domain] = url

		# limit to 5 pages
		keys = list(links.keys())[:5]
		for key in keys:
			link = links[key]
			self.logger.info("Requesting url: {}".format(link))
			try:
				yield scrapy.Request(url=link, callback=self.read_insights_from_page)
			except scrapy.exceptions.NotSupported as ex:
				self.logger.error("Unable to parse url {}".format(ex))


	def read_insights_from_page(self, response):
		self.logger.info("Getting insights from page: {}".format(response.url))
		page_source = "\n".join(response.xpath('//text()').getall())
		words = nltk.word_tokenize(page_source)
		# optional
		words = [word for word in words if word.isalpha() and not word.isnumeric()]
		words = [word.lower().strip() for word in words]
		words = [word for word in words if word not in self.stop_words]
		words = [word for word in words if len(word) > 1]
		words = [self.lemma.lemmatize(word) for word in words]

		fdist = nltk.FreqDist(words)
		insights = []
		# get insights for top-5 words
		for word, frequency in fdist.most_common(5):
			insights.append(word)
			self.logger.info("{}: {}".format(word, frequency))

		bgs = list(ngrams(words, 2))
		fdist_bgs = nltk.FreqDist(bgs)
		bigrams = []	
		# get insights for top-5 bigrams
		for bigram, frequency in fdist_bgs.most_common(5):
			bigrams.append(bigram)
			self.logger.info("{}: {}".format(bigram, frequency))

		yield {"insights": insights, "bigrams": bigrams, "url": response.url}

