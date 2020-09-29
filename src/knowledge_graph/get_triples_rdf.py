import rdflib

def get_objectproperty_triple(objectproperty_name,triples,path):
    """
    check all the triples given objectproperty
    """
    g = rdflib.Graph()
    g.parse(path, format="xml")
    q = "SELECT ?subject ?object WHERE { ?subject :" + objectproperty_name + " ?object}"
    x = g.query(q)
    t = list(x)
    for i in t:
        head = i[0].split("#")[1]
        tail = i[1].split("#")[1]
        result = [head,objectproperty_name,tail]
        triples.append(result)

def check_objecrproperty(tmp_list,path):
    """
    check all the objectproperty
    path: rdf file path
    """
    g = rdflib.Graph()
    g.parse(path, format="xml")
    q = """
            SELECT ?x
    	    WHERE {
    	    ?x rdf:type owl:ObjectProperty}
            """
    x = g.query(q)
    t = list(x)
    for i in t:
        a = (str(i).split("#")[1])[:-4]
        tmp_list.append(a)
    print(tmp_list)

def get_all_triples(path):
    tmp_list = []
    triples = []
    check_objecrproperty(tmp_list,path)
    for i in tmp_list:
        get_objectproperty_triple(i,triples,path)
    print(triples)
