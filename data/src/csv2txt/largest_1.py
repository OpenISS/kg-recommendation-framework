import csv



def function1(path):
    print(path)

    f_txt = open(path, encoding="UTF-8")
    lines = f_txt.readlines()  # 读取全部内容 ，并以列表方式返回
    i = 0
    list1 = []
    biggest = 0
    for line in lines:
        # print(line)
        x = line.split("\t")[0]
        # print(x)
        if x not in list1:
            list1.append(x)
        if int(x) > int(biggest):
            # print("xxxxx")
            # print(int(x))
            biggest = x
    print(biggest)
path = "/Users/yuhaomao/Desktop/mkr-recommendation/data/movie/original/kg_final.txt"
function1(path)
