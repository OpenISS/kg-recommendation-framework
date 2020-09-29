from main import *
from owl_storage import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-mode', type=str, default='neo4j', help='default neo4j')
parser.add_argument('-delet', type=str, default='no', help='default no')
args = parser.parse_args()

print(args)
if __name__ == '__main__':
    if args.mode == "neo4j":
        neo4j_test(args.delet)
    elif args.mode == "rdf":
        RDFtest()
    else:
        print("ERROR")

# if __name__ == '__main__':
#     storage_m = storage_mode()
#     movies_file_path = "/Users/yuhaomao/Downloads/ml-latest/movies.csv"
#     # owl_storage.movie_csv(movies_file_path)
#     # owl_storage.just4test()
#     neo4j_test()