## Framework usage examples

- ``crawler_example.py`` -- an example of how to crawl an IMDB data source based on movie name. The example uses add_python.py  to fetch the following movie information: director names, writer names, and star names and saves it in a CSV format file. 
Use this to call:
```#!bash
python3 crawler_example.py
```

- ``get_alltriples.py``  -- an example of how to get all triple from Neo4j format or RDF format. The example uses get_triples_neo4j.py and get_triples_rdf.py  to fetch the triple informations. 
Use this to call:
```#!bash
python3 get_alltriples.py
```

- ``kg_examples.py`` -- an example of how to add new triples to Neo4j format. The example uses add_triples_neo4j.py to add new triple informations. 
Use this to call:
```#!bash
python3 kg_examples.py
```

- ``modify_node.py`` -- an example of how to add relations or delete a node from Neo4j format. The example uses modifiy_information() and query_delet_node() function to modify nodes. 
Use this to call:
```#!bash
python3 modify_node.py
```


- ``neo4j_multilingual.py``-- an example of Neo4j format supports multiple languages. 
Use this to call:
```#!bash
python3 neo4j_multilingual.py
```
