from py2neo import Graph, Node, Relationship,NodeMatcher,cypher
import datetime
import numpy as np
import csv

def find_node_name(name, username, password):
    """
    eg: find_node_name("Toy Story (1995)"))
    find node which name == "Toy Story (1995)")
    return True
    """
    graph = Graph('http://localhost:7474', username="neo4j", password="0905")
    matcher = NodeMatcher(graph)
    result = matcher.match(name=name).first()
    # print(result)
    if result == None:
        return False
    else:
        return True


def add_triples(triples, username, password):
    """
    triples: input triples
    username: Neo4j username
    password: Neo4j password
    """
    graph = Graph('http://localhost:7474', username="neo4j", password="0905")
    for i in triples:
        head = i[0]
        relation = i[1]
        tail = i[2]
        if find_node_name(head, username, password) == True and find_node_name(tail, username, password) == True:
            head_node = NodeMatcher(graph).match(name=head).first()
            tail_node = NodeMatcher(graph).match(name=tail).first()
            head_relation_tail = Relationship(head_node, relation, tail_node)
            graph.create(head_relation_tail)
        else:
            if find_node_name(head, username, password) == False:
                head_node = Node(head, name=head)
                graph.create(head_node)
            else:
                head_node = NodeMatcher(graph).match(name=head).first()
            if find_node_name(tail, username, password) == False:
                tail_node = Node(tail, name=tail)
                graph.create(tail_node)
            else:
                tail_node = NodeMatcher(graph).match(name=tail).first()
            head_relation_tail = Relationship(head_node, relation, tail_node)
            graph.create(head_relation_tail)



def movies_file(file_path):
    graph = Graph('http://localhost:7474', username="neo4j", password="0905")
    graph.run('match (n) detach delete n')
    with open(file_path, 'r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        for row in rows:
            print(row)
            movie_name = row[1]
            movie_genres = row[2]
            movie_genre_list = movie_genres.split("|")
            triples = []
            for movie_genre in movie_genre_list:
                triples.append([str(movie_name),"genre",str(movie_genre)])
            add_triples(triples,"a","a")
            

def movies_file2(file_path):
    graph = Graph('http://localhost:7474', username="neo4j", password="0905")
    with open(file_path, 'r', encoding="utf-8") as of:
        for line in of:
            print(line)
            line_string = line[:-1]
            list_line = line_string.split("::")
            movie_name = list_line[1]
            genres_string = list_line[2]
            genres_list = genres_string.split("|")
            triples = []
            for movie_genre in genres_list:
                triples.append([str(movie_name),"genre",str(movie_genre)])
            add_triples(triples,"a","a")

# starttime = datetime.datetime.now()
file_path1 = "/Users/yuhaomao/Downloads/ml-latest-small/movies.csv"
movies_file(file_path1)

# file_path2 = "/Users/yuhaomao/Downloads/ml-1m-2/movies.dat"
# movies_file2(file_path2)
# endtime = datetime.datetime.now()
# print((endtime - starttime).seconds)