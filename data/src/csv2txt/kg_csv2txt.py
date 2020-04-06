import csv

# dict = {"genres":"film.film.genre", "Director":3, "Writer":4, "Stars":5}
content = ""
person_name = {}

def kg2txt(file_path,person_name):
    print(file_path)
    start_num = 3883
    f_txt = open(file_path, encoding="ISO-8859-1")
    lines = f_txt.readlines()  # 读取全部内容 ，并以列表方式返回
    # i = 0
    for line in lines:
        print(line)
        movieid = line.split("::")[0]
        genres = line.split("::")[2][:-1]
        genre = genres.split("|")
        for i in genre:
            if i not in person_name:
                person_name[i] = start_num
                start_num += 1
            content = str(movieid) + "\t" + "film.film.genre" + "\t" + str(person_name[i]) + "\n"
            f = open('kg.txt', 'a')
            print(content)
            f.write(content)
            f.close()


kg_file_path = "/Users/yuhaomao/Downloads/ml-1m/movies.txt"
# kg_file_path = "test.csv"
kg2txt(kg_file_path,person_name)
print(person_name)
