from py2neo import Graph, Node, Relationship,NodeMatcher
import csv
from main import *
graph = Graph('http://localhost:7474', username='neo4j', password='0905')
# graph.delete_all()


"""
test1 start
测试可不可以两个节点有好多种关系， 比如一个人即是director 又是writer
测试可以，两个节点中间有两条关系
"""
# movie_node = NodeMatcher(graph).match(name="Toy Story (1995)").first()
# print(movie_node)
#
# directorname = "yuhao mao"
# director_node = Node(directorname,name=directorname, labels="person")
# graph.create(director_node)
#
# user_call_movie = Relationship(movie_node, "director", director_node)
# graph.create(user_call_movie)
#
# user_call_movie = Relationship(movie_node, "writer", director_node)
# graph.create(user_call_movie)
"""
test1 end
"""


"""
test2 start
测试 split和加节点
"""
# movie_writer_split = "Allison Anders|Alexandre Rockwell|Robert Rodriguez|Quentin Tarantino".split("|")
# movie_id = 18
#
# # movie_writer_split = movie_writer.split("|")
# for split_writer in movie_writer_split:
#     if find_node_name(split_writer) == False:
#         writer_node = Node(split_writer, name=split_writer, labels="person")
#         graph.create(writer_node)
#         movie_node = NodeMatcher(graph).match(str(movie_id)).first()
#         writer_call_node = Relationship(movie_node, 'writer', writer_node)
#         graph.create(writer_call_node)
#     else:
#         writer_node = NodeMatcher(graph).match(name=split_writer).first()
#         movie_node = NodeMatcher(graph).match(str(movie_id)).first()
#         writer_call_node = Relationship(movie_node, 'writer', writer_node)
#         graph.create(writer_call_node)
"""
test2 end
"""

"""
test3 start
测csv中的空
"""
# def movie_director(director_path):
#     print(director_path)
#
#     with open(director_path) as f:
#         data_list = [i for i in csv.reader(f)]  # csv.reader 读取到的数据是list类型
#         movie_list = data_list[1:]
#
#         for movie in movie_list:
#             movie_id = movie[0]
#             movie1 = movie[1]
#             movie2 = movie[2]
#             movie_director = movie[3]
#             movie_writer = movie[4]
#             movie_star = movie[5]
#             if movie1 == "":
#                 print("Null: ")
#                 print(movie_id)
#             if movie2 == "":
#                 print("Null: ")
#                 print(movie_id)
#             if movie_director == "":
#                 print("Null: ")
#                 print(movie_id)
#             if movie_writer == "":
#                 print("Null: ")
#                 print(movie_id)
#             if movie_star == "":
#                 print("Null: ")
#                 print(movie_id)
#
# director_path = "../dataset/movies_director.csv"
# movie_director(director_path)
"""
test3 end
"""