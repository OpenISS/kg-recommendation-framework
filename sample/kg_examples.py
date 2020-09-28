import sys
sys.path.append('../src/knowledge_graph')
from add_triples_neo4j import *


triples = [['drug111', 'has_xxxxxxxx', 'idontknow']]

add_2neo4j(triples)