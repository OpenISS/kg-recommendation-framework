## Motivation ##

A recommendation system is needed as long as there are users, but since users have few ratings on items, there will be problems such as data sparsity. This problem can be solved by adding the knowledge graph as side information, but the existing solution does not include the construction of the knowledge graph. By adding the construction of the knowledge graph can help us better manage the data.

----

## What application need it:

- Movie RS
- Book RS
- News RS
- User RS

----

## Datasets

1. https://grouplens.org/datasets/movielens/

----

## Evaluation

1. CTR (Click-Through-Rate)

----

## References

1.	Frame rate. https://en.wikipedia.org/wiki/Frame_rate. Accessed: 2019- 07-23.
2.	Software framework. https://en.wikipedia.org/wiki/Software_framework. Accessed: 2019-06-22.
3.	RDF OWL difference https://www.cambridgesemantics.com/blog/semantic-university/learn-owl-rdfs/rdfs-vs-owl/
4.	Owlready2 documentation https://pythonhosted.org/Owlready2/
5.	Py2neo documentation https://py2neo.org/2.0/
6.	Introduce to RS https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada
7.	auc&acc https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
8.    知乎：https://zhuanlan.zhihu.com/p/54325231(交替学习)
9.    youtube： https://www.youtube.com/watch?v=BP0IZ1uyUDE （协同过滤）
10.  https://blog.csdn.net/dreamzuora/article/details/86543157（cf 优缺点）

----

## Future work
-1. Java API wrapper
-2. Support different machine learning backend
-3. Support more storage methods and more input formats
-4. More effective loss function
-5. Full-platform support
-6. Auto installation


## Software Requirements

1. python3
2. Neo4j  "https://neo4j.com/download/?ref=try-neo4j-lp"

When using the knowledge graph, first open neo4j desktop, add graph, create a local graph, remember the graph name and password. change the username and password in your code.

```!#python
graph = Graph('http://localhost:7474', username='neo4j', password='0905')
```

---

## Dataset explaination

item_index2entity_id.txt:  old_movie_id, new_movie_id
kg_final.txt:   now_movie_id, relation, xxx
ratings_final.txt:   user_id, user_gender, user_age, user_job, new_movie_id, rating

---

## Library Requirements

1. rdflib.  Version: 4.2.2 
2. urllib.request.   '3.7'
3. networkx.  '2.4'
4. matplotlib.  '3.1.2'
5. requests.  '2.22.0'
6. bs4.  '4.8.0'
7. imdb.  '6.8'
8. py2neo.  "2.0"
9. owlready2   "0.22"
10. pandas.  '0.25.0'
11. numpy.  '1.17.0'
12. tensorflow.  '1.14.0'
13. sklearn.  '0.21.3'
14. linecache.  '3.5'
---

## samples:

crawler_example.py :  craw movie infomations  How to run: python3 crawler_example.py
get_alltriples.py: get all triples      How to run: python3 get_alltriples.py: 
hello2222.rdf: RDF format sample 
kg_examples.py:  add triples to neo4j     How to run: kg_examples.py
modify_node.py: modify node     How to run: python3 modify_node.py
neo4j_multilingual.py:  test neo4j multilingual      How to run: python3 neo4j_multilingual.py

---


How to train a model:
In src/recommendation_system/ folder.  and run main.py

What IDE did we use to develop code? 
Recommend to use pycharm (any version). Or use text editing software such as vim.

How to run from command line:
python3 xxxx.py

How to run from Google Colab?
upload all the file to colab, and click run.

Tested MacOS version: Mac Mojava 10.14.6 
