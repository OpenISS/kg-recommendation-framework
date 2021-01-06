from py2neo import Graph, Node, Relationship,NodeMatcher,cypher
import csv





def check_triple(head,tail):
    new_head = ""
    for i in head:
        if i == "'":
            new_head += "\\'"
        else:
            new_head += i
    new_tail = ""
    for i in tail:
        if i == "'":
            new_tail += "\\'"
        else:
            new_tail += i
    graph = Graph('http://localhost:7474', username="neo4j", password="0905")
    query = "MATCH(a {name: '" + new_head + "'})-[r]->(b {name: '" + new_tail + "'}) RETURN type(r)"
    # query = """
    # MATCH(a {name: 'Toy Story (1995)'})-[r]->(b {name: 'Children\\'s'}) RETURN type(r)
    # """
    
    result = graph.run(query)

    if result.data() == []:
        print("false")
        return False
    else:
        print("pass")
        return True



def movies_file(file_path):
    with open(file_path, 'r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        for row in rows:
            movie_name = row[1]
            movie_genres = row[2]
            movie_genre_list = movie_genres.split("|")
            for movie_genre in movie_genre_list:
                if check_triple(str(movie_name),str(movie_genre)) == False:
                    print(movie_name)
                    return
        # triples = [str(movie_name), "genre", str(movie_genre)]
        # print(triples)


def movies_file2(file_path):
    graph = Graph('http://localhost:7474', username="neo4j", password="0905")
    with open(file_path, 'r', encoding="utf-8") as of:
        for line in of:
            print(line)
            line_string = line[:-1]
            list_line = line_string.split("::")
            movie_name = list_line[1]
            genres_string = list_line[2]
            genres_list = genres_string.split("|")
            for movie_genre in genres_list:
                check_triple(str(movie_name),str(movie_genre))
                # triples.append([str(movie_name), "genre", str(movie_genre)])
            


file_path1 = "/Users/yuhaomao/Downloads/ml-latest-small/movies.csv"
movies_file(file_path1)

file_path2 = "/Users/yuhaomao/Downloads/ml-1m-2/movies.dat"
movies_file2(file_path2)


# check_triple("Toy Stry (1995)","Children\\'s")