
def userinfos2txt(file_path,dict):
    result = ""
    print(file_path)
    f_txt = open(file_path, encoding="UTF-8")
    lines = f_txt.readlines()  # 读取全部内容 ，并以列表方式返回
    for line in lines:
        print("linelineline")
        print(line)
        # id = line.split("\t")[0]
        # content = line.split("\t")[1:]
        # print("sss")
        # print(content)
        # result = dict[int(id)] + "\t"
        # for i in content:
        #     result += i
        #     result += "\t"
        # print("resultresultresultresultresult")
        # print(result)
        delet_n = line.rstrip('\n')
        print("zz")
        print(delet_n)
        content = delet_n.split("\t")
        print("Xxx")
        print(content)
        result = ""
        for i in range(len(content)):
            if i == 0:
                result += dict[int(content[i])] + "\t"
            if i == 1:
                result = result + content[i] + "\t"
            if i == 2:
                result = result + content[i] + "\n"
        print("zzzzzzz")
        print(result)
        f = open('../../movie/ratings_final_new.txt', 'a')
        f.write(result)
        f.close()
def convert(file_path,dict):
    txt = open(file_path, encoding="UTF-8")
    lines = txt.readlines()
    count = 0
    for line in lines:
        delet_n = line.rstrip('\n')
        # print(line)
        dict[count] = delet_n
        count += 1
    print(dict)

def delet_t(file_path):
    print(file_path)
    f_txt = open(file_path, encoding="UTF-8")
    lines = f_txt.readlines()  # 读取全部内容 ，并以列表方式返回
    for line in lines:
        print(line)
        line = line[1:]
        print(line)
        
        f = open('../../movie/users_info_final_new.txt', 'a')
        f.write(line)
        f.close()

def read(file_path):
    print(file_path)
    f_txt = open(file_path, encoding="UTF-8")
    lines = f_txt.readlines()  # 读取全部内容 ，并以列表方式返回
    for line in lines:
        delet_n = line.rstrip('\n')
        xxx = delet_n.split("\t")
        print(xxx)
        content = ""
        for i in range(len(xxx)):
            if i == 3:
                content += xxx[i].zfill(2) + "\n"
            else:
                content += xxx[i] + "\t"
        print(content)
        f = open('../../movie/users_info_final_new.txt', 'a')
        f.write(content)
        f.close()
        
        
        
dict = {}
kg_file_path = "../../movie/ratings_final.txt"
file_path = "../../movie/users_info_final.txt"
convert(file_path,dict)
userinfos2txt(kg_file_path,dict)

# read(file_path)

