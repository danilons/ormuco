# Introduction

This is an assignment to a position of machine learning engineer.

# Structure

There are three questions: A, B, and C. Each of them was written in a separated folder accordingly:

- questionA
- questionB
- questionC

# Setup 

The necessary dependencies are listed on `requirements.txt`

In order to install them: 

```
pip install -r requirements.txt`
```

# Running

The first two questions (A and B) are simpler and they have tests. The best way to execute them is by running unit tests. 
Both of them has the same project structure, then it is only necessary to run the following command in their respective root folders:

```
pytest test_solution.py
```

It runs a `pytest` test suite and should execute without any errors


Regarding *question C* it is necessary to run a crawler, in question C root folder just run the command below:

```
scrapy crawl insights -a search_term='keystone - Circular reference found role inference' -o insigths.jl
```

This command runs the `insights` spider and it searches Google for the search term 'keystone - Circular reference found role inference'. Finally, it stores the results in the file `insights.jl` as text.
