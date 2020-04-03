import csv


def movieid2txt(file_path):
    print(file_path)
    f = open(file_path, "r")
    lines = f.readlines()
    i = 0
    for row in lines:
        movieid = row.split("::")[1]

        if int(movieid) > i:
            i = int(movieid)
    print(i)


path = "ratings.txt"
movieid2txt(path)