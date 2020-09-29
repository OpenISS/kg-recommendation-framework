import sys
sys.path.append('../src/knowledge_graph')
import add_triples_neo4j as n
import add_triples_rdf as r

"""
add triples to Neo4j or RDF
input: triples
"""


triples = [['drug111', 'has_xxxxxxxx', 'idontknow']]

# username = "neo4j"
# password = "0905"
# n.add_triples(triples,username,password)

path = "../samples/hello2222.rdf"
r.add_triples(triples,path)