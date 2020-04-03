import csv

def movieid2txt(file_path):
    print(file_path)
    f = open(file_path, "r")
    lines = f.readlines()
    i = 1
    for row in lines:
        movieid = row.split("::")[0]
        f = open('item_index2entity_id.txt', 'a')
        content = str(movieid) + "\t" + str(i) + "\n"
        print(content)
        f.write(content)
        f.close()
        i += 1


movies_file_path = "../../../data/movies_director2.txt"
movieid2txt(movies_file_path)
