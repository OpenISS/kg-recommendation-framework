import csv

def movieid2txt(file_path):
    print(file_path)
    f_txt = open(file_path,encoding="ISO-8859-1")
    lines = f_txt.readlines()      #读取全部内容 ，并以列表方式返回
    i = 0
    for line in lines:
        # print(line)
        f = open('item_index2entity_id.txt', 'a')
        content = str(line.split("::")[0]) + "\t" + str(i) + "\n"
        print(content)
        f.write(content)
        f.close()
        i += 1

movies_file_path = "/Users/yuhaomao/Downloads/ml-1m/movies.txt"
movieid2txt(movies_file_path)
