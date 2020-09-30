import csv
from py2neo import Graph, Node, Relationship,NodeMatcher
import pandas as pd
import datetime

graph = Graph('http://localhost:7474', username='neo4j', password='0905')

class storage_mode():
    
    def movies_file(self,file_path,movieid_dict):
        print(file_path)
        f = open(file_path, "r", encoding="utf-8")
        lines = f.readlines()
        for movie in lines:
            # print(movie)
            movie = movie.replace("\n","")
            movie_infos = movie.split("::")
            movie_id = movie_infos[0]
            movie_name = movie_infos[1]
            movie_genres_str = movie_infos[2]
            movie_genres_list = movie_genres_str.split("|")
            print(movie_name)
            movieid_dict[movie_id] = movie_name
            movie_node = Node(movie_id,name=movie_name, labels="movie")
            graph.create(movie_node)
            for movie_genres in movie_genres_list:
                if self.find_node_name(movie_genres) == False:
                    genres_node = Node(movie_genres,name=movie_genres)
                    graph.create(genres_node)
                    genre_call_node = Relationship(movie_node, 'genre', genres_node)
                    graph.create(genre_call_node)
                else:
                    genres_node = NodeMatcher(graph).match(name=movie_genres).first()
                    genre_call_node = Relationship(movie_node, 'genre', genres_node)
                    graph.create(genre_call_node)
    
    
    def ratings_csv(self,file_path,movieid_dict):
        print(file_path)
        f = open(file_path, "r", encoding="utf-8")
        lines = f.readlines()
        for ratings in lines:
            ratings_list = ratings.split("::")
            print(ratings_list)
            userid = ratings_list[0]
            movieid = ratings_list[1]
            rating = ratings_list[2]
            movie_name = movieid_dict[movieid]
            print(movie_name)
            if self.find_node_name(str("user_" + str(userid))) == False:
                user_node = Node(str("user_" + str(userid)),name=str("user_" + str(userid)),labels = "user")
                graph.create(user_node)
            else:
                user_node = NodeMatcher(graph).match(name=str("user_" + str(userid))).first()
            user_movie_node = NodeMatcher(graph).match(name = movie_name).first()
            print("ssssssss")
            print(user_movie_node)
            user_call_movie = Relationship(user_node, str(rating), user_movie_node)
            graph.create(user_call_movie)
    
           
    def movie_director(self,file_path):
        print(file_path)
        
        f = open(file_path, "r", encoding="utf-8")
        lines = f.readlines()
        for triples in lines:
            print(triples)
            triples = triples.replace("\n","")
            triples_list = triples.split("\t")
            print(triples_list)
            movie_name = triples_list[0]
            relation = triples_list[1]
            person_name = triples_list[2]
            print(movie_name)
            print(relation)
            print(person_name)
            movie_node = NodeMatcher(graph).match(name=movie_name).first()
            if self.find_node_name(person_name) == False:
                person_node = Node(person_name, name=person_name, labels="person")
                graph.create(person_node)
            else:
                person_node = NodeMatcher(graph).match(name=person_name).first()
            print(movie_node)
            print(person_node)
            person_call_node = Relationship(movie_node, relation, person_node)
            graph.create(person_call_node)

    def user_info(self, director_path):
        print(director_path)

        f_txt = open(director_path, encoding="UTF-8")
        lines = f_txt.readlines()
        
        for data in lines:
            data = data.split("::")
            print(data)

            user_id = data[0]
            user_gender = data[1]
            user_age = data[2]
            user_job = data[3]
            if self.find_node_name(user_id) == False:
                user_id_node = Node(user_id, name=user_id)
                graph.create(user_id_node)
            else:
                user_id_node = NodeMatcher(graph).match(name=user_id).first()
            if self.find_node_name(user_gender) == False:
                user_gender_node = Node(user_gender, name=user_gender)
                graph.create(user_gender_node)
            else:
                user_gender_node = NodeMatcher(graph).match(name=user_gender).first()
            if self.find_node_name(user_age) == False:
                user_age_node = Node(user_age, name=user_age)
                graph.create(user_age_node)
            else:
                user_age_node = NodeMatcher(graph).match(name=user_age).first()

            if self.find_node_name(user_job) == False:
                user_job_node = Node(user_job, name=user_job)
                graph.create(user_job_node)
            else:
                user_job_node = NodeMatcher(graph).match(name=user_job).first()
            userid_relation_usergender = Relationship(user_id_node, 'gender', user_gender_node)
            graph.create(userid_relation_usergender)
            userid_relation_userage = Relationship(user_id_node, 'gender', user_age_node)
            graph.create(userid_relation_userage)
            userid_relation_userjob = Relationship(user_id_node, 'gender', user_job_node)
            graph.create(userid_relation_userjob)
    
    
    def find_node_id(self,id):
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
    
    
    def find_node_name(self,name):
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

def delete_node(name,username,password):
    graph = Graph('http://localhost:7474', username=username, password=password)
    storage_m = storage_mode()
    if storage_m.find_node_name(name) == False:
        return
    else:
        string_qurey = "MATCH (a{name:\"" + name + "\"}) DETACH DELETE a;"
        result = graph.run(string_qurey)

def neo4j_test(parameter):
    if parameter == "no":
        print("all")
        # storage_m = storage_mode()
        # movies_file_path = "/Users/yuhaomao/Downloads/ml-latest/movies.csv"
        # storage_m.movies_csv(movies_file_path)
        #
        # ratings_file_path = "../dataset/ratings.csv"
        # storage_m.ratings_csv(ratings_file_path)
        #
        # director_path = "../dataset/movies_director.csv"
        # storage_m.movie_director(director_path)
        #
        # user_info_path = "/Users/yuhaomao/Downloads/ml-1m/users.dat"
        # storage_m.user_info(user_info_path)
        
    if parameter == "director":
        print("delet director")
        # storage_m = storage_mode()
        # movies_file_path = "/Users/yuhaomao/Downloads/ml-latest/movies.csv"
        # storage_m.movies_csv(movies_file_path)
        #
        # ratings_file_path = "../dataset/ratings.csv"
        # storage_m.ratings_csv(ratings_file_path)
        # user_info_path = "/Users/yuhaomao/Downloads/ml-1m/users.dat"
        # storage_m.user_info(user_info_path)
        
    if parameter == "user":
        print("user")
        # storage_m = storage_mode()
        # movies_file_path = "/Users/yuhaomao/Downloads/ml-latest/movies.csv"
        # storage_m.movies_csv(movies_file_path)
        #
        # ratings_file_path = "../dataset/ratings.csv"
        # storage_m.ratings_csv(ratings_file_path)
        #
        # director_path = "../dataset/movies_director.csv"
        # storage_m.movie_director(director_path)
        
    print("neo4j test finish")
if __name__ == '__main__':
    storage_m = storage_mode()
    movies_file_path = "../../data/movie/movies.txt"
    movieid_dict = {}
    storage_m.movies_file(movies_file_path,movieid_dict)

    ratings_file_path = "../../data/movie/ratings.txt"
    storage_m.ratings_csv(ratings_file_path,movieid_dict)

    kg_sideinforamtion_path = "../../data/movie/kg_additional.txt"
    storage_m.movie_director(kg_sideinforamtion_path)