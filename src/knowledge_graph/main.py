import csv
from py2neo import Graph, Node, Relationship,NodeMatcher
import pandas as pd
import datetime

graph = Graph('http://localhost:7474', username='neo4j', password='0905')
# graph.delete_all()
# reg = "[^0-9A-Za-z\u4e00-\u9fa5]"  ####### remove symbol rule

class storage_mode():
    
    def movies_csv(self,file_path):
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
                if self.find_node_name(movie_genres) == False:
                    genres_node = Node(movie_genres,name=movie_genres)
                    graph.create(genres_node)
                    genre_call_node = Relationship(movie_node, 'genre', genres_node)
                    graph.create(genre_call_node)
                else:
                    genres_node = NodeMatcher(graph).match(name=movie_genres).first()
                    genre_call_node = Relationship(movie_node, 'genre', genres_node)
                    graph.create(genre_call_node)
    
    
    def ratings_csv(self,file_path):
        print(file_path)
    
        data = pd.read_table(file_path,chunksize=1000,header=None,sep=",")
        for chunk in data:
            print(chunk)
            for userid,movieid,rating in zip(chunk[0],chunk[1],chunk[2]):
                print(userid,movieid,rating)
                if self.find_node_name(str("user_" + str(userid))) == False:
                    user_node = Node(str("user_" + str(userid)),name=str("user_" + str(userid)),labels = "user")
                    graph.create(user_node)
                else:
                    user_node = NodeMatcher(graph).match(name=str("user_" + str(userid))).first()
                user_movie_node = NodeMatcher(graph).match(str(movieid)).first()
                user_call_movie = Relationship(user_node, str(rating), user_movie_node)
                graph.create(user_call_movie)
                
            print("111111111")
    
           
    def movie_director(self,director_path):
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
                    if self.find_node_name(split_director) == False:
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
                    if self.find_node_name(split_writer) == False:
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
                    if self.find_node_name(split_star) == False:
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
# if __name__ == '__main__':
#     storage_m = storage_mode()
#     begin = datetime.datetime.now()
#     print("begin time:", begin)
#     print(storage_m.find_node_name("Tom Hanks"))
#     end = datetime.datetime.now()
#     print("end time:", end)
#     a = ((end - begin).microseconds)  # 29522
#     print(a)
#     movies_file_path = "/Users/yuhaomao/Downloads/ml-latest/movies.csv"
#     storage_m.movies_csv(movies_file_path)
#
#     ratings_file_path = "../dataset/ratings.csv"
#     # ratings_csv(ratings_file_path)
#
#     director_path = "../dataset/movies_director.csv"
    # storage_m.movie_director(director_path)
    
    
    ############################################################################# test
    # print(find_node_name("Fantasy"))
    # movie_node = NodeMatcher(graph).match(name = "Sudden Death (1995)").first()
    # movie_node1 = NodeMatcher(graph).match(name="Tom and Huck (1995)").first()
    # genre_call_node = Relationship(movie_node1, 'genre', movie_node)
    # graph.create(genre_call_node)
    
    # id = 307
    # movie_node = NodeMatcher(graph).match(str(id)).first()
    # print(movie_node)
# storage_m = storage_mode()
# user_info_path = "/Users/yuhaomao/Downloads/ml-1m/users.dat"
# storage_m.user_info(user_info_path)