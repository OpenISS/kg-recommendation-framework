from py2neo import Graph, Node, Relationship,NodeMatcher,cypher
import dask.dataframe as dd
import pandas as pd


graph = Graph('http://localhost:7474', username='neo4j', password='0905')
# graph.delete_all()

def modifiy_information():
    movie_node = NodeMatcher(graph).match(name = "https://www.imdb.com/title/tt0851515/mediaviewer/rm1022288896").first()
    user_node = NodeMatcher(graph).match(name = "疯狂赛车").first()
    # print(user_node)
    genre_call_node = Relationship(movie_node, 'poster_link', user_node)
    graph.create(genre_call_node)

def query_delet_node(name):
    string_qurey = "MATCH (a{name:\"" + name + "\"}) DELETE a;"
    result = graph.run(string_qurey)
    for i in result:
        print(i)

def shanchuchongjian():
    graph.delete_all()
    movie_node2 = Node("b", name="La Règle du Jeu (1939)", labels="movie")
    movie_node3 = Node("c", name="疯狂赛车", labels="movie")
    movie_node1 = Node("a", name="かぐや姫の物語", labels="movie")
    movie_node4 = Node("a", name="부산행", labels="movie")
    movie_node5 = Node("a", name="Ahí va el diablo", labels="movie")
    movie_node6 = Node("a", name="Русский ковчег", labels="movie")
    movie_node7 = Node("a", name="Wie küsst man einen Millionär", labels="movie")
    graph.create(movie_node3)
    graph.create(movie_node2)
    graph.create(movie_node1)
    graph.create(movie_node4)
    graph.create(movie_node5)
    graph.create(movie_node6)
    graph.create(movie_node7)
    # p_node2 = Node("b", name="user_b", labels="person")
    # p_node3 = Node("c", name="c_user", labels="person")
    # p_node1 = Node("a", name="user_A", labels="person")
    # graph.create(p_node2)
    # graph.create(p_node3)
    # graph.create(p_node1)

def query_delet_relation(a,b,c):
    string_qurey = """
       MATCH (a{name:"https://www.imdb.com/title/tt0851515/mediaviewer/rm1022288896"})-[r:star]-(b{name:"疯狂赛车"}) DELETE r;
    """
    result = graph.run(string_qurey)

def load_all_triples():
    query = """ MATCH (n)-[r]->(m) RETURN  n.name,type(r),m.name """
    result = graph.run(query)
    for i in result:
        print(i)
        for x in i:
            print(x)
    
if __name__ == '__main__':
    # pass
    # modifiy_information()
    # shanchuchongjian()
    # query_delet_node("c_user")
    # query_delet_relation("user_A","director","movie_A")
    load_all_triples()
    

