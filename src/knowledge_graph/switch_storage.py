# from main import *
# from owl_storage import *
# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument('-mode', type=str, default='neo4j', help='default neo4j')
# parser.add_argument('-dataset', type=str, default='all', help='default all')
# args = parser.parse_args()
#
# if __name__ == '__main__':
#     if args.mode == "neo4j":
#         Storage_neo4j(args.dataset)
#     elif args.mode == "rdf":
#         path = "../../samples/hello2222.rdf"
#         Storage_rdf(args.dataset,path)
#     else:
#         print("ERROR" )
from main import StorageManager
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-mode', type=str, default='neo4j', help='default neo4j')
parser.add_argument('-dataset', type=str, default='all', help='default all')
args = parser.parse_args()

if __name__ == '__main__':
    storage_m = StorageManager()
    if args.mode == "neo4j":
        storage_m.getManager("Neo4j")
        storage_m.load(args.dataset)
    elif args.mode == "rdf":
        storage_m.getManager("rdf")
        storage_m.load(args.dataset)
    else:
        print("ERROR")