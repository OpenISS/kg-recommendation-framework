import requests
import re
import csv
from py2neo import Graph, Node, Relationship,NodeMatcher
import dask.dataframe as dd
import pandas as pd


graph = Graph('http://localhost:7474', username='neo4j', password='0905')
# graph.delete_all()
# reg = "[^0-9A-Za-z\u4e00-\u9fa5]"  ####### remove symbol rule

def movies_csv(file_path):
    print(file_path)
    with open(file_path) as f:
        data_list = [i for i in csv.reader(f)]  # csv.reader 读取到的数据是list类型
        movie_list = data_list[1:]
        print(movie_list)
    for movie in movie_list:
        movie_id = movie[0]
        movie_name = movie[1]
        movie_genres_str = movie[2]
        movie_genres_list = movie_genres_str.split("|")
        print(movie_id)
        # print(movie_name)
        # print(movie_genres_list)
        movie_node = Node(movie_id,name=movie_name, labels="movie")
        graph.create(movie_node)
        for movie_genres in movie_genres_list:
            if find_node_name(movie_genres) == False:
                genres_node = Node(movie_genres,name=movie_genres)
                graph.create(genres_node)
                genre_call_node = Relationship(movie_node, 'genre', genres_node)
                graph.create(genre_call_node)
            else:
                genres_node = NodeMatcher(graph).match(name=movie_genres).first()
                genre_call_node = Relationship(movie_node, 'genre', genres_node)
                graph.create(genre_call_node)


def ratings_csv(file_path):
    print(file_path)

    data = pd.read_table(file_path,chunksize=1000,header=None,sep=",")
    for chunk in data:
        print(chunk)
        for userid,movieid,rating in zip(chunk[0],chunk[1],chunk[2]):
            print(userid,movieid,rating)
            if find_node_name(str("user_" + str(userid))) == False:
                user_node = Node(str("user_" + str(userid)),name=str("user_" + str(userid)),labels = "user")
                graph.create(user_node)
            else:
                user_node = NodeMatcher(graph).match(name=str("user_" + str(userid))).first()
            user_movie_node = NodeMatcher(graph).match(str(movieid)).first()
            user_call_movie = Relationship(user_node, str(rating), user_movie_node)
            graph.create(user_call_movie)
            
        print("111111111")

       
def movie_director(director_path):
    print(director_path)
    
    with open(director_path) as f:
        data_list = [i for i in csv.reader(f)]  # csv.reader 读取到的数据是list类型
        movie_list = data_list[1:]

        for movie in movie_list:
            movie_id = movie[0]
            movie_director = movie[3]
            movie_writer = movie[4]
            movie_star = movie[5]
            print(movie_id)
            movie_director_split = movie_director.split("|")
            for split_director in movie_director_split:
                if find_node_name(split_director) == False:
                    director_node = Node(split_director, name=split_director,labels = "person")
                    graph.create(director_node)
                    movie_node = NodeMatcher(graph).match(str(movie_id)).first()
                    director_call_node = Relationship(movie_node, 'director', director_node)
                    graph.create(director_call_node)
                else:
                    director_node = NodeMatcher(graph).match(name=split_director).first()
                    movie_node = NodeMatcher(graph).match(str(movie_id)).first()
                    director_call_node = Relationship(movie_node, 'director', director_node)
                    graph.create(director_call_node)

            movie_writer_split = movie_writer.split("|")
            for split_writer in movie_writer_split:
                if find_node_name(split_writer) == False:
                    writer_node = Node(split_writer, name=split_writer, labels="person")
                    graph.create(writer_node)
                    movie_node = NodeMatcher(graph).match(str(movie_id)).first()
                    writer_call_node = Relationship(movie_node, 'writer', writer_node)
                    graph.create(writer_call_node)
                else:
                    writer_node = NodeMatcher(graph).match(name=split_writer).first()
                    movie_node = NodeMatcher(graph).match(str(movie_id)).first()
                    writer_call_node = Relationship(movie_node, 'writer', writer_node)
                    graph.create(writer_call_node)

            movie_star_split = movie_star.split("|")
            for split_star in movie_star_split:
                if find_node_name(split_star) == False:
                    star_node = Node(split_star, name=split_star, labels="person")
                    graph.create(star_node)
                    movie_node = NodeMatcher(graph).match(str(movie_id)).first()
                    star_call_node = Relationship(movie_node, 'star', star_node)
                    graph.create(star_call_node)
                else:
                    star_node = NodeMatcher(graph).match(name=split_star).first()
                    movie_node = NodeMatcher(graph).match(str(movie_id)).first()
                    star_call_node = Relationship(movie_node, 'star', star_node)
                    graph.create(star_call_node)
                    
                    

            
    
def find_node_id(id):
    """
    eg: find_node_id("1")
    find node which id == 1
    result : (_501:`1` {name: 'Toy Story (1995)'})
    """
    matcher = NodeMatcher(graph)
    result = matcher.match(id).first()
    print(result)
    if result == None:
        return False
    else:
        return True


def find_node_name(name):
    """
    eg: find_node_name("Toy Story (1995)"))
    find node which name == "Toy Story (1995)")
    return True
    """
    matcher = NodeMatcher(graph)
    result = matcher.match(name = name).first()
    # print(result)
    if result == None:
        return False
    else:
        return True

if __name__ == '__main__':
    movies_file_path = "../dataset/movies.csv"
    # movies_csv(movies_file_path)

    ratings_file_path = "../dataset/ratings.csv"
    # ratings_csv(ratings_file_path)
    
    director_path = "../dataset/movies_director.csv"
    movie_director(director_path)
    
    
    ############################################################################# test
    # print(find_node_name("Fantasy"))
    # movie_node = NodeMatcher(graph).match(name = "Sudden Death (1995)").first()
    # movie_node1 = NodeMatcher(graph).match(name="Tom and Huck (1995)").first()
    # genre_call_node = Relationship(movie_node1, 'genre', movie_node)
    # graph.create(genre_call_node)
    
    # id = 307
    # movie_node = NodeMatcher(graph).match(str(id)).first()
    # print(movie_node)