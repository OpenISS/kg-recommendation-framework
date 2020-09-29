from py2neo import Graph, Node, Relationship,NodeMatcher,cypher

def find_node_name(name,username,password):
    """
    eg: find_node_name("Toy Story (1995)"))
    find node which name == "Toy Story (1995)")
    return True
    """
    graph = Graph('http://localhost:7474', username= username, password=password)
    matcher = NodeMatcher(graph)
    result = matcher.match(name=name).first()
    # print(result)
    if result == None:
        return False
    else:
        return True
    
def add_triples(triples,username,password):
    """
    triples: input triples
    username: Neo4j username
    password: Neo4j password
    """
    graph = Graph('http://localhost:7474', username=username, password=password)
    for i in triples:
        head = i[0]
        relation = i[1]
        tail = i[2]
        if find_node_name(head,username,password) == True and find_node_name(tail,username,password) == True:
            head_node = NodeMatcher(graph).match(name=head).first()
            tail_node = NodeMatcher(graph).match(name=tail).first()
            head_relation_tail = Relationship(head_node, relation, tail_node)
            graph.create(head_relation_tail)
        else:
            if find_node_name(head,username,password) == False:
                head_node = Node(head, name=head)
                graph.create(head_node)
            else:
                head_node = NodeMatcher(graph).match(name=head).first()
            if find_node_name(tail,username,password) == False:
                tail_node = Node(tail, name=tail)
                graph.create(tail_node)
            else:
                tail_node = NodeMatcher(graph).match(name=tail).first()
            head_relation_tail = Relationship(head_node, relation, tail_node)
            graph.create(head_relation_tail)


# triples = [['drug111', 'has_xxxxxxxx', 'idontknow']]
#
# add_triples(triples)


