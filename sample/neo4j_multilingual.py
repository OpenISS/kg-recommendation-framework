from py2neo import Graph, Node, Relationship,NodeMatcher,cypher

graph = Graph('http://localhost:7474', username='neo4j', password='0905')


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