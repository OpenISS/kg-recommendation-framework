from py2neo import Graph, Node, Relationship,NodeMatcher,cypher

def get_all_triples(list_result,username,password):
    graph = Graph('http://localhost:7474', username=username, password=password)
    query = """ MATCH (n)-[r]->(m) RETURN  n.name,type(r),m.name """
    result = graph.run(query)
    for i in result:
        # print(i)
        tmp = []
        for x in i:
            tmp.append(x)
        list_result.append(tmp)

result = []
get_all_triples(result,"neo4j","0905")
for i in result:
    print(i)
# print(result)