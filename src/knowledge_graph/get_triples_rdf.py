# from owlready2 import *
import rdflib

# def add_datapproperty_value(individual_name,dataproperty_name,value):
#     path = "/Users/yuhaomao/master/sample/hello2222.rdf"
#     onto = get_ontology(path).load()
#     with onto:
#         print(type(value))
#         if type(value) == str:
#             exec('onto.{}.{} = ["{}"]'.format(individual_name,dataproperty_name,value))
#         if type(value) == int:
#             exec('onto.{}.{} = [{}]'.format(individual_name,dataproperty_name,value))
#     onto.save("hello2222.rdf")
#
# # add_datapproperty_value("aaa","has_for_synonym",123)
#
# def check_individual():
#     """
#     检查individual是否存在
#     """
#     path = "/Users/yuhaomao/master/sample/hello2222.rdf"
#     onto = get_ontology(path).load()
#     with onto:
#         print(onto.my_drug)



def get_objectproperty_triple(objectproperty_name,triples):
    """
    检查给定的objectproperty的所有三元组
    """
    g = rdflib.Graph()
    g.parse("/Users/yuhaomao/master/sample/hello2222.rdf", format="xml")
    # q = """
    #     SELECT ?subject ?object
	#     WHERE { ?subject :has_whatever ?object}
    #     """
    q = "SELECT ?subject ?object WHERE { ?subject :" + objectproperty_name + " ?object}"
    x = g.query(q)
    t = list(x)
    for i in t:
        head = i[0].split("#")[1]
        tail = i[1].split("#")[1]
        result = [head,objectproperty_name,tail]
        triples.append(result)

def check_objecrproperty(tmp_list):
    """
    查询所有的objectproperty
    """
    g = rdflib.Graph()
    g.parse("/Users/yuhaomao/master/sample/hello2222.rdf", format="xml")
    q = """
            SELECT ?x
    	    WHERE {
    	    ?x rdf:type owl:ObjectProperty}
            """
    x = g.query(q)
    t = list(x)
    for i in t:
        # print(i)
        a = (str(i).split("#")[1])[:-4]
        tmp_list.append(a)

def get_all_triples():
    tmp_list = []
    triples = []
    check_objecrproperty(tmp_list)
    for i in tmp_list:
        get_objectproperty_triple(i,triples)
    # for i in triples:
    #     print(i)
    print(triples)


get_all_triples()