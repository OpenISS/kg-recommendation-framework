# Knowledge Graph-based Recommendation System framework

This code supplement's [Yuhao Mao](https://github.com/myh1234567)'s master's thesis "A Framework Design For Integrating Knowledge Graphs into Recommendation Systems" work and the resulting publication(s).
The framework uses movies as an example and is generalizable into other media types.

- Yuhao Mao, "A Framework Design For Integrating Knowledge Graphs into Recommendation Systems", Master's thesis, Concordia University, 2021
- Yuhao Mao, Serguei A. Mokhov, Sudhir P. Mudur:
Application of Knowledge Graphs to Provide Side Information for Improved Recommendation Accuracy. CoRR [abs/2101.03054](https://arxiv.org/abs/2101.03054) (2021)
- Sudhir Mudur, Serguei Mokhov, and Yuhao Mao. 2021. A Framework for Enhancing Deep Learning Based Recommender Systems with Knowledge Graphs. In IDEAS 2021: 25th International Database Engineering Applications Symposium, July 14–16, 2021, Montreal, Canada. ACM, New York, NY, USA, 10 pages. https://doi.org/10.1145/1122445.1122456

## Background ##

### Motivation ###

A recommendation system is needed as long as there are users, but since users have few ratings on items, there will be problems such as data sparsity. This problem can be solved by adding the knowledge graph as side information, but the existing solution does not include the construction of the knowledge graph. By adding the construction of the knowledge graph can help us better manage the data.

### What type of applications may need it

- Movie RS
- Book RS
- News RS
- User RS

---

### Datasets

- https://grouplens.org/datasets/movielens/

#### Evaluation

- CTR (Click-Through-Rate)

#### Dataset field sources

1. `kg_final.txt`: now_movie_id, relation, xxx
2. `ratings_final.txt`: user_id, user_gender, user_age, user_job, new_movie_id, rating

---

## Software Requirements

1. python3
2. Neo4j: https://neo4j.com/download/?ref=try-neo4j-lp

### Library Requirements

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

```#!bash
brew install python3
pip3 install rdflib
pip3 install urllib.request
pip3 install networkx
pip3 install matplotlib
pip3 install requests
pip3 install bs4
pip3 install IMDbPy
pip3 install py2neo
pip3 install owlready2
pip3 install pandas
pip3 install numpy
pip3 install tensorflow
pip3 install sklearn
pip3 install linecache
```

### Installing on EL7 

1. Clone the repo
2. Install dependencies

```#!bash
yum install python3 gcc python3-devel
pip3 install requests
pip3 install py2neo
pip3 install numpy
pip3 install pandas
...
```

## Running

### Samples

- [Framework usage examples](samples/README.md)

### Questions / FAQ

- How to train a model: go to `src/recommendation_system/` folder and run main.py
- What IDE did we use to develop code? 
Recommend to use PyCharm (any version). Or use any text editing software such as vim or VS Code.
- How to run from command line: `python3 xxxx.py`
- How to run from Google Colab? Upload all the files to colab, and click run.

Tested MacOS version: macOS Mojave 10.14.6 

#### How to start

1. `cd ../web_crawler`,  `python3 add_infos.py` to get the `kg_additional` file. It includes movie director, writer and stars information.
2. Start Neo4j desktop then `cd ../knowledge_graph`  and run `python3 main.py`. It create all triples in Neo4j.
3. `cd ../recommendation_system/data_process` and run `triples2txt.py`, `ratings2txt.py`, `kg_final.py` to get `ratings_final.txt` and `kg_final.txt`
4. `cd ../recommendation_system` and run `main.py`

----

## Future work / TODO

1. Java API wrapper
2. Support different machine learning backends
3. Support more storage methods and more input formats
4. More effective loss function
5. Full-platform support
6. Auto installation

----

## References

1. Frame rate. https://en.wikipedia.org/wiki/Frame_rate. Accessed: 2019- 07-23.
2. Software framework. https://en.wikipedia.org/wiki/Software_framework. Accessed: 2019-06-22.
3. RDF OWL difference https://www.cambridgesemantics.com/blog/semantic-university/learn-owl-rdfs/rdfs-vs-owl/
4. Owlready2 documentation https://pythonhosted.org/Owlready2/
5. Py2neo documentation https://py2neo.org/2.0/
6. Introduce to RS https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada
7. auc&acc https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
8. https://zhuanlan.zhihu.com/p/54325231
9. youtube： https://www.youtube.com/watch?v=BP0IZ1uyUDE
10. https://blog.csdn.net/dreamzuora/article/details/86543157
