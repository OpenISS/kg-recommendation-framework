import csv

def movieid2txt(file_path):
    print(file_path)
    f_txt = open(file_path,encoding="UTF-8")
    lines = f_txt.readlines()      #读取全部内容 ，并以列表方式返回
    i = 0
    list1 = []
    biggest = 0
    for line in lines:
        print(line)
        x = line.split("\t")[1]
        print(x)
        if x not in list1:
            list1.append(x)
        if int(x) > int(biggest):
            print("xxxxx")
            print(int(x))
            biggest = x
        # f = open('item_index2entity_id.txt', 'a')
        # content = str(line.split("::")[0]) + "\t" + str(i) + "\n"
        # print(content)
        # f.write(content)
        # f.close()
        # i += 1
    print(len(list1))
    print(sorted(list1)[-650:-400])
    print(biggest)


movies_file_path = "/Users/yuhaomao/Desktop/mkr-recommendation/data/movie/original/ratings_final.txt"
movieid2txt(movies_file_path)
