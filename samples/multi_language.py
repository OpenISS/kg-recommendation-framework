from py2neo import Graph, Node, Relationship,NodeMatcher,cypher

graph = Graph('http://localhost:7474', username='neo4j', password='0905')

graph.run('match (n) detach delete n')
# movie_node2 = Node("b", name="La_Règle_du_Jeu_(1939)", labels="movie")
# movie_node3 = Node("c", name="疯狂赛车", labels="movie")
# movie_node1 = Node("a", name="かぐや姫の物語", labels="movie")
# movie_node4 = Node("a", name="부산행", labels="movie")
# movie_node5 = Node("a", name="Ahí_va_el_diablo", labels="movie")
# movie_node6 = Node("a", name="Русский_ковчег", labels="movie")
# movie_node7 = Node("a", name="Wie_küsst_man_einen_Millionär", labels="movie")
# movie_node8 = Node("a", name="writer_A", labels="person")
# movie_node9 = Node("a", name="star_A", labels="person")
# movie_node10 = Node("a", name="director_A", labels="person")
#
# graph.create(movie_node3)
# graph.create(movie_node2)
# graph.create(movie_node1)
# graph.create(movie_node4)
# graph.create(movie_node5)
# graph.create(movie_node6)
# graph.create(movie_node7)
# graph.create(movie_node8)
# graph.create(movie_node9)
# graph.create(movie_node10)
#
# movie_node = Node("a", name="Robert_Downey_Jr.", labels="person")
# movie_node2 = Node("a", name="Tom_Holland", labels="person")
#
# movie_node3 = Node("c", name="Iron_Man_(2008)", labels="movie")
# graph.create(movie_node)
# graph.create(movie_node2)
# graph.create(movie_node3)