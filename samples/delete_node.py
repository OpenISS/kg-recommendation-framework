import sys
sys.path.append('../src/knowledge_graph')
import main as n
import owl_storage as r


"""
Neo4j:
    input: node name, username, password

RDF:
    input: file path, node name
"""

path = "../samples/hello2222.rdf"
name = "drug111"
username = "neo4j"
password = "0905"
# r.delete_node(path,name)
# n.delete_node(name,username,password)

