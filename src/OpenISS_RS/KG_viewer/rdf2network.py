import networkx as nx
import matplotlib.pyplot as plt
import rdflib

class kg_viewer:
    def __init__(self,individual_list,total_class_dict):
        self.individual_list = individual_list
        self.total_class_dict = total_class_dict
    
    def query_individual_content(self,a,individual_name,rdf_about):
        """
        查询 individual的content
        dataproperty和value放在result里 存成一个 dictionary
        subindividual存在sub individuals里，存成一个list
        """
        g = rdflib.Graph()
        # print("????????????????????????????")
        # print(individual_name)
        g.parse("/Users/yuhaomao/Desktop/AES_CN_knowledge-graph/json2rdf/hello2222.rdf", format="xml")
        q = "SELECT ?p ?o  WHERE { <" + rdf_about + "#" + individual_name + "> ?p ?o .}"
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

    def query_class_type(self,a,individual_name,rdf_about,dict):
        """
        查询 individual的content
        dataproperty和value放在result里 存成一个 dictionary
        subindividual存在sub individuals里，存成一个list
        """
        g = rdflib.Graph()
        # print("????????????????????????????")
        # print(individual_name)
        g.parse("/Users/yuhaomao/Desktop/AES_CN_knowledge-graph/json2rdf/hello2222.rdf", format="xml")
        q = "SELECT ?p ?o  WHERE { ?p ?o <" + rdf_about + "#" + individual_name + ">.}"
        x = g.query(q)
        t = list(x)
        for i in t:
            class_name = i[1].split("#")[-1]
            dict[class_name] = "x"
            
        return dict



    def kg_classes(self,individual_list,total_class_dict):
        for i in individual_list:
            total_class_dict = self.query_class_type("a",i,rdf_about,total_class_dict)
        
def query_individual(a,path):
    g = rdflib.Graph()
    g.parse("../../samples/hello2222.rdf", format="xml")
    SELECT * WHERE
    {
    ?s ?p ?o
    }
    q = "SELECT *  WHERE { <" + rdf_about + "#" + individual_name + "> ?p ?o .}"
    x = g.query(q)
    t = list(x)

if __name__ == "__main__":
    a = {}
    G = nx.DiGraph()
    rdf_about = "../../samples/hello2222.rdf"
    individual_list = query_individual(a,rdf_about)
    individual_list = ['individual_id10', 'individual_id29', 'individual_id40', 'individual_id92', 'individual_id43', 'individual_id93', 'individual_id84', 'individual_id23', 'individual_id69', 'individual_id31', 'individual_id17', 'individual_id48', 'individual_id24', 'individual_id85', 'individual_id21', 'individual_id41', 'individual_id58', 'individual_id82', 'individual_id12', 'individual_id88', 'individual_id55', 'individual_id9', 'individual_id51', 'individual_id3', 'individual_id94', 'individual_id14', 'individual_id60', 'individual_id32', 'individual_id59', 'individual_id16', 'individual_id53', 'individual_id70', 'individual_id38', 'individual_id67', 'individual_id63', 'individual_id89', 'individual_id33', 'individual_id6', 'individual_id95', 'individual_id11', 'individual_id77', 'individual_id19', 'individual_id28', 'individual_id83', 'individual_id86', 'individual_id96', 'individual_id30', 'individual_id78', 'individual_id0', 'individual_id20', 'individual_id42', 'individual_id71', 'individual_id5', 'individual_id56', 'individual_id75', 'individual_id74', 'individual_id39', 'individual_id73', 'individual_id7', 'individual_id4', 'individual_id64', 'individual_id26', 'individual_id22', 'individual_id65', 'individual_id47', 'individual_id81', 'individual_id27', 'individual_id66', 'individual_id2', 'individual_id68', 'individual_id1', 'individual_id62', 'individual_id76', 'individual_id52', 'individual_id72', 'individual_id15', 'individual_id46', 'individual_id8', 'individual_id18', 'individual_id34', 'individual_id36', 'individual_id87', 'individual_id13', 'individual_id35', 'individual_id57', 'individual_id44', 'individual_id50', 'individual_id80', 'individual_id45', 'individual_id37', 'individual_id79', 'individual_id90', 'individual_id61', 'individual_id54', 'individual_id49', 'individual_id25', 'individual_id91']
    total_class_dict = {}
    kg_v = kg_viewer(individual_list,total_class_dict)
    kg_v.kg_classes(individual_list,total_class_dict)
    dict = {}
    
    count = 0
    for i in individual_list:
        if str(i) in dict:
            tmp = dict[str(i)]
        else:
            G.add_node(count, name=str(i))
            dict[i] = count
            tmp = count
            count += 1
        dataproperty_dict = kg_v.query_individual_content(a,str(i),rdf_about)[0]
        subindividual_dict = kg_v.query_individual_content(a,str(i),rdf_about)[1]
        current_class_type = kg_v.query_individual_content(a,str(i),rdf_about)[2]
        for dataproperty in dataproperty_dict:
            tmp2 = count
            G.add_node(count, name=dataproperty_dict[dataproperty].split("#")[-1])
            dict[dataproperty_dict[dataproperty].split("#")[-1]] = count
            count += 1
            G.add_edge(tmp, tmp2, dataproperty=str(dataproperty))

        for subindividual in subindividual_dict:
            if type(subindividual_dict[subindividual]) == str:
                if subindividual_dict[subindividual] in dict:
                    tmp3 = dict[subindividual_dict[subindividual]]
                else:
                    tmp3 = count
                    G.add_node(tmp3,name = subindividual_dict[subindividual])
                    dict[subindividual_dict[subindividual]] = count
                    count += 1

                G.add_edge(tmp, tmp3, property=str(subindividual.split("__")[-1]))

            if type(subindividual_dict[subindividual]) == list:
                for x in subindividual_dict[subindividual]:
                    if x in dict:
                        tmp4 = dict[str(x)]
                    else:
                        tmp4 = count
                        G.add_node(count, name=str(x))
                        dict[str(x)] = count
                        count += 1
                    G.add_edge(tmp, tmp4, property=str(x))
        for class_type in current_class_type:
            if "has"+current_class_type[class_type] not in total_class_dict:
                tmp5 = count
                G.add_node(tmp5, classname="hassuper")
                count += 1
            else:
                if type(total_class_dict["has"+current_class_type[class_type]]) == int:
                    tmp5 = total_class_dict["has"+current_class_type[class_type]]
                else:
                    tmp5 = count
                    total_class_dict["has"+current_class_type[class_type]] = tmp5
                    G.add_node(tmp5, classname=current_class_type[class_type])
                    count += 1
            G.add_edge(tmp5, tmp, property="class")

    nx.draw_networkx(G)
    plt.show()
