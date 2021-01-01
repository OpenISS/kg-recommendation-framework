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
    # print(tmp_list)

def get_all_triples(path,result):
    tmp_list = []
    check_objecrproperty(tmp_list,path)
    for i in tmp_list:
        get_objectproperty_triple(i,result,path)
    # print(result)

result = []
get_all_triples("../../samples/hello2222.rdf",result)
for i in result:
    print(i)
# print(result)

# ['Robert_Downey_Jr.', 'director', 'Русский_ковчег']
# ['Jon_Favreau', 'director', 'Iron_Man_(2008)']
# ['star_A', 'star', 'Ahí_va_el_diablo']
# ['Wie_küsst_man_einen_Millionär', 'poster_link', 'imdb_link']



# neo4j
# [' Anthony Russo.', 'director', 'Avengers:_Endgame_(2019)']
# ['Robert_Downey_Jr.', 'star', 'Iron_Man_(2008)']
# ['Robert_Downey_Jr.', 'writer', 'Русский_ковчег']
# ['star_A', 'star', 'Ahí_va_el_diablo']



