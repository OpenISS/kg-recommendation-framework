import networkx as nx
import matplotlib.pyplot as plt
import rdflib

class networkx_viewer:
    def __init__(self,individual_list,total_class_dict,rdf_about):
        self.individual_list = individual_list
        self.total_class_dict = total_class_dict
        self.rdf_about = rdf_about
    
    def query_individual_content(self,individual_name,path):
        """
        query individual contents
        store as a dictionary
        """
        g = rdflib.Graph()
        g.parse(path, format="xml")
        q = "SELECT ?p ?o  WHERE { <" + self.rdf_about + "#" + individual_name + "> ?p ?o .}"
        x = g.query(q)
        t = list(x)
        result = {}
        sub_individuals = {}
        current_class = {}
        for i in t:
            # print("========")
            # print(i)
            dataproperty = i[0].split("#")[-1]
            dataproperty_value = i[1].split("#")[-1]
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            # print(dataproperty)
            # print(dataproperty_value)
            if dataproperty_value != "NamedIndividual" and dataproperty != "type":
                if dataproperty_value in individual_list:
                    if dataproperty in sub_individuals :
                        if type(sub_individuals[dataproperty]) == str:
                            copy = sub_individuals[dataproperty]
                            tmp = [copy,dataproperty_value]
                            sub_individuals[dataproperty] = tmp
                        if type(sub_individuals[dataproperty]) == list and dataproperty_value not in sub_individuals[dataproperty]:
                            sub_individuals[dataproperty].append(dataproperty_value)
                    else:
                        sub_individuals[dataproperty] = dataproperty_value
                else:
                    a = str(i[1])
                    result[dataproperty] = a
            if dataproperty_value != "NamedIndividual" and dataproperty == "type":
                current_class["classtype"] = dataproperty_value
        # print("--------------------")
        # print(result)
        # print(sub_individuals)
        # print(current_class)
        return result,sub_individuals,current_class

    def query_class_type(self,individual_name,dict):
        """
        query individual's class
        return a dict
        
        for example:
        return {'star': 'x', 'director': 'x', 'poster_link': 'x', 'writer': 'x'}
        """
        g = rdflib.Graph()
        g.parse("../../../samples/hello2222.rdf", format="xml")
        q = "SELECT ?p ?o  WHERE { ?p ?o <" + self.rdf_about + "#" + individual_name + ">.}"
        x = g.query(q)
        t = list(x)
        for i in t:
            class_name = i[1].split("#")[-1]
            dict[class_name] = class_name
            
        return dict



    def individual_classes(self,individual_list,total_class_dict):
        for i in individual_list:
            total_class_dict = self.query_class_type(i,total_class_dict)
        return total_class_dict
        

def query_all_individuals(path):
    """
    query all the individuals in file.
    return a list.
    """
    g = rdflib.Graph()
    g.parse(path, format="xml")
    q = "SELECT ?individual  WHERE {?individual rdf:type owl:NamedIndividual.}"
    x = g.query(q)
    t = list(x)
    result = []
    for i in t:
        result.append(i[0].split("#")[1])
    return result

def query_rdf_about(path):
    """
    query rdf about value
    return string
    """
    g = rdflib.Graph()
    result = g.parse(path, format="xml")
    for i in result:
        rdf_about = i[0].split("#")[0]
        break
    return rdf_about

if __name__ == "__main__":
    a = {}
    G = nx.DiGraph()
    path = "../../../samples/hello2222.rdf"
    rdf_about = query_rdf_about(path)
    individual_list = query_all_individuals(path)
    total_class_dict = {}
    network_v = networkx_viewer(individual_list,total_class_dict,rdf_about)
    network_v.individual_classes(individual_list,total_class_dict)
    
    dict = {}
    for i in individual_list:
        if str(i) in dict:
            individual_name = dict[str(i)]
        else:
            G.add_node(i, name=str(i))
            dict[i] = i
            individual_name = i
        dataproperty_dict = network_v.query_individual_content(str(i),path)[0]
        subindividual_dict = network_v.query_individual_content(str(i),path)[1]
        current_class_type = network_v.query_individual_content(str(i),path)[2]
        for dataproperty in dataproperty_dict:
            dataproperty_name = dataproperty_dict[dataproperty].split("#")[-1]
            G.add_node(individual_name, name=dataproperty_name)
            dict[dataproperty_name] = dataproperty_name

            G.add_edge(individual_name, dataproperty_name, dataproperty=str(dataproperty))

        for subindividual in subindividual_dict:
            if type(subindividual_dict[subindividual]) == str:
                if subindividual_dict[subindividual] in dict:
                    sub_individual = dict[subindividual_dict[subindividual]]
                else:
                    sub_individual = subindividual
                    
                    G.add_node(sub_individual,name = sub_individual)
                    dict[sub_individual] = sub_individual

                G.add_edge(individual_name, sub_individual, property=str(subindividual.split("__")[-1]))

            if type(subindividual_dict[subindividual]) == list:
                for x in subindividual_dict[subindividual]:
                    if x in dict:
                        tmp4 = dict[str(x)]
                    else:
                        G.add_node(x, name=str(x))
                        dict[str(x)] = x
                    G.add_edge(individual_name, x, property=str(x))
        for class_type in current_class_type:
            if "has"+current_class_type[class_type] not in total_class_dict:
                current_class_name = "has"+current_class_type[class_type]
                G.add_node(current_class_name, classname="hassuper")
                tmp5 = "has"+current_class_type[class_type]
            else:
                if type(total_class_dict["has"+current_class_type[class_type]]) == int:
                    tmp5 = total_class_dict["has"+current_class_type[class_type]]
                else:
                    tmp5 = "has"+current_class_type[class_type]
                    total_class_dict["has"+current_class_type[class_type]] = tmp5
                    G.add_node(tmp5, classname=current_class_type[class_type])
      
            G.add_edge(tmp5, individual_name, property="class")

    nx.draw_networkx(G)
    plt.show()
