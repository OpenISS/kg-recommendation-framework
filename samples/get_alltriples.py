import sys
sys.path.append('../src/knowledge_graph')
import get_triples_neo4j as n
import get_triples_rdf as r

# path = "../samples/hello2222.rdf"
# r.get_all_triples(path)

result = []
username = "neo4j"
password = "0905"
n.get_all_triples(result,username,password)
print(result)
