from owlready2 import *
import csv

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# add a class
def add_class(name, parent,path):
    onto = get_ontology(path).load()
    with onto:
        if parent == "Thing" or parent == owl.Thing:
            exec('class {}({}): pass'.format(name, parent))
        else:
            exec('class {}(onto.{}): pass'.format(name, parent))
        onto.save(path)
# add_class("super", Thing)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# add individual belongs to a class
def add_individual(class_name, individual_name,path):
    onto = get_ontology(path).load()
    with onto:
        # print(class_name)
        exec('onto.{class_name}("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
    onto.save(path)
# last_class = "Thing__devices"
# add_individual(last_class, "indsssvu")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# add data_property
def add_dataproperty(dataproperty_name,domain_value,range_value,path):
    onto = get_ontology(path).load()
    with onto:
        exec('class {0}(DataProperty): \n domain=[onto.{1}]  \n range=[{2}]'.format(dataproperty_name,domain_value,range_value))
    # onto.has_for_synonym = ["acetaminophen", "paracétamol"]
    onto.save(path)
# add_dataproperty("hasversion","super","str")

def add_datapproperty_value(individual_name,dataproperty_name,value,path):
    onto = get_ontology(path).load()
    with onto:
        print(type(value))
        if type(value) == str:
            exec('onto.{}.{} = ["{}"]'.format(individual_name,dataproperty_name,value))
        if type(value) == int:
            exec('onto.{}.{} = [{}]'.format(individual_name,dataproperty_name,value))
    onto.save(path)
# add_datapproperty_value("aaa","has_for_synonym",123)
# onto.aaa.has_for_synonym = [123]

# add data_property's value
def add_data_value(individual_name,dataproperty_name,value,path):
    onto = get_ontology(path).load()
    with onto:
        exec('onto.{0}.{1}.append("{2}")'.format(individual_name,dataproperty_name, value))
    onto.save(path)
# add_data_value("my_drug","has_for_synonym","int")
# onto.my_drug.has_for_synonym.append("int")


# find node through id(Not implemented yet)
def find_node_id(node_id):
    print("ERROR")


# find node through name
def find_node_name(name):
    node_exist = exec('onto.{}'.format(name))
    if node_exist != None:
        return True
    else:
        return False

def add_triple(domain_name,objectproprety,range_name,path):
    """
    add a triple to path file
    """
    onto = get_ontology(path).load()
    with onto:
        exec('onto.{0}.{1} = [onto.{2}]'.format(domain_name,objectproprety,range_name))
        # onto.test1.has_for_ingredient = [onto.acetaminophen]
        onto.save(path)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# add object property
def add_objectproperty(domain_name,objectproprety,range_name,path):
    onto = get_ontology(path).load()
    with onto:
        exec('class {0}(ObjectProperty): \n domain=[onto.{1}] \n range = [onto.{2}]'.format(objectproprety,domain_name,range_name))
    onto.save(path)

def movies_file(file_path,movieid_dict,path):
    print(file_path)
    f = open(file_path, "r", encoding="utf-8")
    lines = f.readlines()
    for movie in lines:
        # print(movie)
        movie = movie.replace("\n", "")
        movie_infos = movie.split("::")
        movie_id = movie_infos[0]
        movie_name = movie_infos[1]
        movie_genres_str = movie_infos[2]
        movie_genres_list = movie_genres_str.split("|")
        print(movie_name)
        movieid_dict[movie_id] = movie_name
        add_individual("owl:Thing", movie_name)
        for movie_genres in movie_genres_list:
            onto = get_ontology(path).load()
            with onto:
                relation_exist = exec('onto.{}'.format("gener"))
                tail_exist = exec('onto.{}'.format(movie_genres))
                if relation_exist != None and tail_exist != None:
                    add_triple(head, "genre", movie_genres, path)
                else:
                    if relation_exist == None:
                        add_objectproperty("Thing", "genre", "Thing", path)
                    if tail_exist == None:
                        add_individual("owl:Thing", movie_genres, path)
                    add_triple(head, "genre", movie_genres, path)
            onto.save(path)


def ratings_file(file_path,movieid_dict,path):
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
        onto = get_ontology(path).load()
        with onto:
            head_exist = exec('onto.{}'.format(userid))
            relation_exist = exec('onto.{}'.format("rating"))
            tail_exist = exec('onto.{}'.format(movie_name))
            if head_exist != None and relation_exist != None and tail_exist != None:
                add_triple(userid, rating, movie_name, path)
            else:
                if head_exist == None:
                    add_individual("owl:Thing", userid, path)
                if relation_exist == None:
                    add_objectproperty("Thing", rating, "Thing", path)
                if tail_exist == None:
                    add_individual("owl:Thing", movie_name, path)
                add_triple(head, rating, movie_name, path)
        onto.save(path)

def movie_director(file_path,path):
    print(file_path)

    f = open(file_path, "r", encoding="utf-8")
    lines = f.readlines()
    for triples in lines:
        print(triples)
        triples = triples.replace("\n", "")
        triples_list = triples.split("\t")
        print(triples_list)
        movie_name = triples_list[0]
        relation = triples_list[1]
        person_name = triples_list[2]
        
        onto = get_ontology(path).load()
        with onto:
            head_exist = exec('onto.{}'.format(movie_name))
            relation_exist = exec('onto.{}'.format(relation))
            tail_exist = exec('onto.{}'.format(person_name))
            if head_exist != None and relation_exist != None and tail_exist != None:
                add_triple(movie_name, relation, movie_name, path)
            else:
                if head_exist == None:
                    add_individual("owl:Thing", movie_name, path)
                if relation_exist == None:
                    add_objectproperty("Thing", relation, "Thing", path)
                if tail_exist == None:
                    add_individual("owl:Thing", movie_name, path)
                add_triple(head, relation, movie_name, path)
        onto.save(path)

def user_info(user_info_path,path):
    print(user_info_path)

    f_txt = open(user_info_path, encoding="UTF-8")
    lines = f_txt.readlines()
    onto = get_ontology(path).load()
    with onto:
        add_objectproperty("Thing", "user_gender", "Thing", path)
        add_objectproperty("Thing", "user_age", "Thing", path)
        add_objectproperty("Thing", "user_job", "Thing", path)
    onto.save(path)

    for data in lines:
        data = data.replace("\n", "")
        data = data.split("::")
        print(data)
    
        user_id = "user_" + str(data[0])
        user_gender = data[1]
        user_age = data[2]
        user_job = data[3]
        
        onto = get_ontology(path).load()
        with onto:
            head_exist = exec('onto.{}'.format(user_id))
            tail_gender = exec('onto.{}'.format(user_gender))
            tail_age = exec('onto.{}'.format(user_age))
            tail_job = exec('onto.{}'.format(user_job))
            
            if head_exist != None and tail_gender != None and tail_age != None and tail_job!= None:
                add_triple(user_id, "user_gender", user_gender, path)
                add_triple(user_id, "user_age", user_age, path)
                add_triple(user_id, "user_job", user_job, path)
            else:
                if head_exist == None:
                    add_individual("owl:Thing", user_id, path)
                if tail_gender == None:
                    add_objectproperty("Thing", "user_gender", "Thing", path)
                if tail_age == None:
                    add_individual("owl:Thing", "user_age", path)
                if tail_job == None:
                    add_individual("owl:Thing", "user_job", path)
                add_triple(user_id, "user_gender", user_gender, path)
                add_triple(user_id, "user_age", user_age, path)
                add_triple(user_id, "user_job", user_job, path)
        onto.save(path)

def poster_info(self, path):
    print(path)

    f_txt = open(path, encoding="UTF-8")
    lines = f_txt.readlines()
    onto = get_ontology(path).load()
    with onto:
        add_objectproperty("Thing", "poster", "Thing", path)
    onto.save(path)

    for data in lines:
        data = data.replace("\n", "")
        data = data.split("\t")
        movie_name = data[0]
        movie_poster = data[1]
        onto = get_ontology(path).load()
        with onto:
            head_exist = exec('onto.{}'.format(movie_name))
            tail_exist = exec('onto.{}'.format(movie_poster))
            if head_exist != None and tail_exist != None:
                add_triple(movie_name, "poster", movie_name, path)
            else:
                if head_exist == None:
                    add_individual("owl:Thing", movie_name, path)
                if tail_exist == None:
                    add_individual("owl:Thing", movie_poster, path)
                add_triple(head, "poster", movie_name, path)
        onto.save(path)

def delete_node(path,name):
    onto = get_ontology(path).load()
    exec('destroy_entity(onto.{0})'.format(name))
    onto.save(path)


def create_node(class_name, individual_name, path):
    onto = get_ontology(path).load()
    with onto:
        # print(class_name)
        exec(
            'onto.{class_name}("{individual_name}")'.format(class_name="Thing", individual_name=individual_name))
    onto.save(path)


def create_relation(domain_name, objectproprety, range_name, path):
    onto = get_ontology(path).load()
    with onto:
        exec('onto.{0}.{1} = [onto.{2}]'.format(domain_name, objectproprety, range_name))
        onto.save(path)

def Storage_rdf(parameter,path):
    
    # movies_file_path = "../../data/movie/movies.txt"
    # movieid_dict = {}
    # movies_file(movies_file_path, movieid_dict,path)
    #
    # ratings_file_path = "../../data/movie/ratings.txt"
    # ratings_file(ratings_file_path, movieid_dict,path)
    
    result = parameter.split(",")
    result.sort()
    for i in result:
        if i == "all":
            print("all")
            # kg_sideinforamtion_path = "../../data/movie/kg_additional.txt"
            # movie_director(kg_sideinforamtion_path,path)
            #
            # users_info_path = "../../data/movie/users.dat"
            # user_info(users_info_path,path)
            #
            # poster_path = "../../data/movie/kg_poster.txt"
            # poster_info(poster_path,path)
            break
    
        elif i == "user_info":
            print("user")
            # users_info_path = "../../data/movie/users.dat"
            # user_info(users_info_path,path)
    
        elif i == "poster_info":
            print("poster")
            # poster_path = "../../data/movie/kg_poster.txt"
            # poster_info(poster_path,path)
    
        elif i == "movie_info":
            print("movie_info")
            # kg_sideinforamtion_path = "../../data/movie/kg_additional.txt"
            # movie_director(kg_sideinforamtion_path,path)