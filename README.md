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
1. Java API wrapper
2. Support different machine learning backend
3. Support more storage methods and more input formats
4. More effective loss function
5. Full-platform support
6. Auto installation


## Software Requirements

1. python3
2. Neo4j  "https://neo4j.com/download/?ref=try-neo4j-lp"

When using the knowledge graph, first open Neo4j desktop, add graph, create a local graph, remember the graph name and password. change the username and password in your code.

```!#python
graph = Graph('http://localhost:7474', username='username', password='password')
```

---

## Dataset explaination

1. item_index2entity_id.txt:  old_movie_id, new_movie_id
2. kg_final.txt:   now_movie_id, relation, xxx
3. ratings_final.txt:   user_id, user_gender, user_age, user_job, new_movie_id, rating

---

## Library Requirements
pip3 install xxxxxxx == version
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

### Installing on MacOS ###

- do we need ``brew``?
- ...

### Installing on EL7 ###

1. Clone the repo
2. Install dependencies
```
yum install python3 gcc python3-devel
pip3 install requests
pip3 install py2neo
pip3 install dask
pip3 install numpy
pip3 install pandas
python3 -m pip install "dask[dataframe]" --upgrade
```

## samples:
[Framework usage examples](https://bitbucket.org/iss-v2-proj/video-recommender-system/src/master/samples/README.md)
---
Questions:

How to train a model:
In src/recommendation_system/ folder.  and run main.py

What IDE did we use to develop code? 
Recommend to use pycharm (any version). Or use text editing software such as vim.

How to run from command line:
python3 xxxx.py

How to run from Google Colab?
upload all the file to colab, and click run.

Tested MacOS version: Mac Mojava 10.14.6 
