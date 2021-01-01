from py2neo import Graph, Node, Relationship,NodeMatcher,cypher

def save_kg_triples(username,password):
    graph = Graph('http://localhost:7474', username= username, password=password)
    string_qurey = "match (a)-[r]->(b) where type(r) in ['writers','stars','directors','genre'] return a.name,type(r),b.name;"
    query_result = graph.run(string_qurey)
    for i in query_result:
        result = ""
        head = i[0]
        relation = i[1]
        tail = i[2]
        result += head + "\t" + relation + "\t" + tail + "\n"
        f = open("../../data/movie/kg.txt", "a")
        f.write(result)
        f.close()

username = "neo4j"
password = "0905"
save_kg_triples("neo4j","0905")


