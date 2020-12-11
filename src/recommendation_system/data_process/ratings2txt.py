from py2neo import Graph, Node, Relationship,NodeMatcher,cypher

def save_rating_triples(username,password):
    graph = Graph('http://localhost:7474', username= username, password=password)
    string_qurey = "match (a)-[r]->(b) where type(r) in ['1','2','3','4','5'] return a.name,type(r),b.name;"
    query_result = graph.run(string_qurey)
    # print(query_result.data())
    for i in query_result:
        result = ""
        head = i[0][5:]
        relation = i[1]
        tail = i[2]
        result += head + "::" + tail + "::" + relation + "\n"
        f = open("../../data/movie/rating.txt", "a")
        f.write(result)
        f.close()

username = "neo4j"
password = "0905"
save_rating_triples("neo4j","0905")


