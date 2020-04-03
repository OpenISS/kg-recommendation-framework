import csv

content = ""
person_name = {}

def kg2txt(file_path, content):
    print(file_path)
    f = open(file_path, "r")
    lines = f.readlines()
    num = 3884
    for row in lines:
        movieid = row.split("::")[0]
        moviename = row.split("::")[1]
        genre = row.split("::")[2].split("|")
        Director = row.split("::")[3].split("|")
        Writer = row.split("::")[4].split("|")
        Stars = row.split("::")[5].split("|")

        for g in genre:
            if g == "(no genres listed)":
                pass
            else:
                if g not in person_name:
                    person_name[g] = num
                    num += 1
                content = content + str(movieid) + "\t" + "film.film.genre" + "\t" + str(person_name[g]) + "\n"

        for d in Director:
            if d == "<PAD>":
                pass
            else:
                if d not in person_name:
                    person_name[d] = num
                    num += 1
                content = content + str(movieid) + "\t" + "film.film.director" + "\t" + str(person_name[d]) + "\n"

        for w in Writer:
            if w == "<PAD>":
                pass
            else:
                if w not in person_name:
                    person_name[w] = num
                    num += 1
                content = content + str(movieid) + "\t" + "film.film.writer" + "\t" + str(person_name[w]) + "\n"

        for s in Stars:
            if s == "<PAD>":
                pass
            else:
                if s not in person_name:
                    person_name[s] = num
                    num += 1
                content = content + str(movieid) + "\t" + "film.film.star" + "\t" + str(person_name[s]) + "\n"
        f = open('kg.txt', 'a')
        # content = str(row[0]) + "\t" + str(i) + "\n"
        # print(content)
        f.write(content)
        f.close()
        content = ""

kg_file_path = "../../../data/movies_director2.txt"
# kg_file_path = "test.csv"
kg2txt(kg_file_path,content)
# print(person_name)
