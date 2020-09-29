from owlready2 import *
import uuid
import csv
# path = "/Users/yuhaomao/Desktop/AES-CN/owlready_test/hello.rdf"
# # iri= "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17"
# onto = get_ontology(path).load()

path = "../samples/hello2222.rdf"
# iri= "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17"
onto = get_ontology(path).load()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 添加单独一个class
def add_class(name, parent):
    with onto:
        # print("parent:")
        # print(parent)
        # print("name;")
        # print(name)
        if parent == "Thing" or parent == owl.Thing:
            # print("thingthingthing:")
            # print(parent)
            exec('class {}({}): pass'.format(name, parent))
        else:
            # print("else:")
            # print(parent)
            exec('class {}(onto.{}): pass'.format(name, parent))
        onto.save("hello2222.rdf")
# add_class("super", Thing)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 创建individual 属于某个class
def add_individual(class_name, individual_name):
    with onto:
        # print(class_name)
        exec('onto.{class_name}("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
        # exec('("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
    onto.save("hello2222.rdf")
# last_class = "Thing__devices"
# add_individual(last_class, "indsssvu") # parent应该是写thing就可以, 参考objectproperty，可以改成onto.classname


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 创建data_property
# plan1
def add_dataproperty1(dataproperty_name,domain,range):
    with onto:
        onto_data_property = types.new_class(dataproperty_name, (DataProperty,))
        onto_data_property.domain = [domain]
        onto_data_property.range = [range]
# add_dataproperty("name1",Drug,str)

# plan2
# with onto:
#     class has_for_synonym(DataProperty):
#         domain = [Thing]
#         range = [int]
# onto.has_for_synonym = ["acetaminophen", "paracétamol"] # []里的两个参数没什么用好像

# plan3 推荐第三个
def add_dataproperty(dataproperty_name,domain_value,range_value):
    with onto:
        exec('class {0}(DataProperty): \n domain=[onto.{1}]  \n range=[{2}]'.format(dataproperty_name,domain_value,range_value))
    # onto.has_for_synonym = ["acetaminophen", "paracétamol"]
    onto.save("hello2222.rdf")
# add_dataproperty("hasversion","super","str")

def add_datapproperty_value(individual_name,dataproperty_name,value):
    with onto:
        print(type(value))
        if type(value) == str:
            exec('onto.{}.{} = ["{}"]'.format(individual_name,dataproperty_name,value))
        if type(value) == int:
            exec('onto.{}.{} = [{}]'.format(individual_name,dataproperty_name,value))
    onto.save("hello2222.rdf")
# add_datapproperty_value("aaa","has_for_synonym",123)
# onto.aaa.has_for_synonym = [123]


# onto.has_for_synonym = ["individual_id0", "ssss"]
# onto.save("hello2222.rdf")
# def add_dataproperty_value(data)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 添加 data_property 的value
def add_data_value(individual_name,dataproperty_name,value):
    exec('onto.{0}.{1}.append("{2}")'.format(individual_name,dataproperty_name, value))
# add_data_value("my_drug","has_for_synonym","int")
# onto.my_drug.has_for_synonym.append("int")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 添加 object property
# def add_objectproperty(domain_name,objectproprety,range_name):
def add_objectproperty(domain_name,objectproprety,range_name):
    with onto:
        exec('class {0}(ObjectProperty): \n domain=[onto.{1}] \n range = [onto.{2}]'.format(objectproprety,domain_name,range_name))
        onto.save("hello2222.rdf")
        # class has_for_ingredient111111(ObjectProperty):
        #     domain = [onto.xxx]
        #     range = [onto.Ingredient]
# add_objectproperty("super","has_for_ingredient111111","Thing__devices")

# onto.save("hello2222.rdf")
# onto.aaa.has_for_synonym = [123]
# onto.save("hello2222.rdf")

def movie_csv(file_path):
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
        print(movie_name)
        # print(movie_name)
        # print(movie_genres_list)
        add_individual("Drug",str(movie_name))
        # graph.create(movie_node)
        for movie_genres in movie_genres_list:
            add_individual("Drug",movie_genres)
            # graph.create(genres_node)
            # genre_call_node = add_data_value(movie_id,"genre",genres_node)
            # graph.create(genre_call_node)
            # else:
            #     genres_node = NodeMatcher(graph).match(name=movie_genres).first()
            #     genre_call_node = Relationship(movie_node, 'genre', genres_node)
            #     graph.create(genre_call_node)

def delete_node(path,name):
    onto = get_ontology(path).load()
    exec('destroy_entity(onto.{0})'.format(name))
    onto.save(path)

def RDFtest():
    print("owl test")