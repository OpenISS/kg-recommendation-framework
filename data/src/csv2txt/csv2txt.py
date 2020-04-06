import csv


def kg2txt(file_path):
    print(file_path)
    f_txt = open(file_path, encoding="UTF-8")
    lines = f_txt.readlines()  # 读取全部内容 ，并以列表方式返回
    for line in lines:
        print(line)
        content = line.replace(",","::")
        f = open('csv2txt.txt', 'a')
        print(content)
        f.write(content)
        f.close()


kg_file_path = "/Users/yuhaomao/Desktop/movie-recommendation-system-/dataset/movies_director2.csv"
kg2txt(kg_file_path)
