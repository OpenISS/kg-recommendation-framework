import networkx as nx
import matplotlib.pyplot as plt
import rdflib
import pylab

def query_class_type(individual_name,rdf_about,dict):
    """
    查询 individual的content
    dataproperty和value放在result里 存成一个 dictionary
    subindividual存在sub individuals里，存成一个list
    """
    g = rdflib.Graph()
    # print("????????????????????????????")
    # print(individual_name)
    g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")
    q = """
    SELECT ?p
    WHERE
    { ?p </Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf#individual_id0">.
    }
    """
    x = g.query(q)
    t = list(x)
    print("sssss")
    print(t)
    for i in t:
        print(i)
        class_name = i[1].split("#")[-1]
        dict[class_name] = "x"
    
    return dict


dict = {}
rdf_about = "file:///Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf"
list1 = ['individual_id0']
for i in list1:
    dict = query_class_type(i,rdf_about,dict)

print(dict)
# dict['hasThing__devices__Controller__ComputingDevice__parameters__runtime'] = 0
print(dict)