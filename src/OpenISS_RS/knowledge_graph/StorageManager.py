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



from Neo4jManager import Storage_neo4j
from RDFManager import Storage_rdf
import argparse

class StorageManager():
    
    def getManager(self, mode):
        self.current_mode = ""
        if mode == "Neo4j":
            print("Initial Neo4j! ")
            self.current_mode = "Neo4j"
        elif mode == "rdf":
            print("Initial RDF! ")
            self.current_mode = "rdf"
    
    def load(self, dataset):
        if self.current_mode == "Neo4j":
            Storage_neo4j(dataset)
        elif self.current_mode == "rdf":
            Storage_rdf(dataset, "path")



parser = argparse.ArgumentParser()
parser.add_argument('-mode', type=str, default='Neo4j', help='default neo4j')
parser.add_argument('-dataset', type=str, default='all', help='default all')
args = parser.parse_args()

if __name__ == '__main__':
    storage_m = StorageManager()
    if args.mode == "Neo4j":
        storage_m.getManager("Neo4j")
        storage_m.load(args.dataset)
    elif args.mode == "rdf":
        storage_m.getManager("rdf")
        storage_m.load(args.dataset)
    else:
        print("ERROR")