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

# result = []
# load_all_triples(result)
# print(result)


# head_node = Node("my_drug", name="my_drug")
# graph.create(head_node)
#
# head1_node = Node("new_drug", name="new_drug")
# graph.create(head1_node)
#
# head_relation_tail = Relationship(head_node, "new_relation", head1_node)
# graph.create(head_relation_tail)