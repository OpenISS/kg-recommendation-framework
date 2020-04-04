import csv

content = ""
person_name = {}
id_dict = {}
def read_item_entity_id(path,dict):
    print(path)
    f = open(path, "r")
    lines = f.readlines()
    for row in lines:
        movie_id = row.split("\t")[0]
        entity_id = row.split("\t")[1].split("\n")[0]
        # print(row)
        # print(movie_id)
        # print(entity_id)
        if movie_id not in id_dict:
            id_dict[movie_id] = entity_id
    print(id_dict)
    
def kg2txt(file_path, content,id_dict):
    print(file_path)
    print(id_dict)
    f = open(file_path, "r")
    lines = f.readlines()
    num = 3883
    for row in lines:
        movieid = row.split("::")[0]
        moviename = row.split("::")[1]
        genre = row.split("::")[2].split("|")
        Director = row.split("::")[3].split("|")
        Writer = row.split("::")[4].split("|")
        Stars = row.split("::")[5].split("|")
        movieid2entity = id_dict[movieid]
        # print(movieid)
        # print(movieid2entity)
        # print("\n")
        for g in genre:
            if g == "(no genres listed)":
                pass
            else:
                if g not in person_name:
                    person_name[g] = num
                    num += 1
                content = content + str(movieid2entity) + "\t" + "film.film.genre" + "\t" + str(person_name[g]) + "\n"

        for d in Director:
            if d == "<PAD>":
                pass
            else:
                if d not in person_name:
                    person_name[d] = num
                    num += 1
                content = content + str(movieid2entity) + "\t" + "film.film.director" + "\t" + str(person_name[d]) + "\n"

        for w in Writer:
            if w == "<PAD>":
                pass
            else:
                if w not in person_name:
                    person_name[w] = num
                    num += 1
                content = content + str(movieid2entity) + "\t" + "film.film.writer" + "\t" + str(person_name[w]) + "\n"

        for s in Stars:
            if s == "<PAD>":
                pass
            else:
                if s not in person_name:
                    person_name[s] = num
                    num += 1
                content = content + str(movieid2entity) + "\t" + "film.film.star" + "\t" + str(person_name[s]) + "\n"
        f = open('kg.txt', 'a')
        # content = str(row[0]) + "\t" + str(i) + "\n"
        # print(content)
        f.write(content)
        f.close()
        content = ""

item_index2entity_id_path = "item_index2entity_id.txt"
read_item_entity_id(item_index2entity_id_path,id_dict)
kg_file_path = "movies_director2.txt"
# kg_file_path = "test.csv"
kg2txt(kg_file_path,content,id_dict)
# print(person_name)
