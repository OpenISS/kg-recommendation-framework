import sys
sys.path.append('../src/knowledge_graph')

import main as StorageManager
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-mode', type=str, default='neo4j', help='default neo4j')
parser.add_argument('-dataset', type=str, default='all', help='default all')
args = parser.parse_args()

if __name__ == '__main__':
    storage_m = StorageManager()
    if args.mode == "neo4j":
        StorageManager.Neo4jManager(args.dataset)
    elif args.mode == "rdf":
        StorageManager.RDFManager(args.dataset)
    else:
        print("ERROR")