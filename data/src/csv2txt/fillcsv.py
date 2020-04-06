import csv

def kg2txt(csv_file,txt_file):
    print(csv_file)
    f_txt = open(txt_file, encoding="ISO-8859-1")
    f_csv = open(csv_file, encoding="UTF-8")
    txt_lines = f_txt.readlines()  # 读取全部内容 ，并以列表方式返回
    csv_lines = f_csv.readlines()  # 读取全部内容 ，并以列表方式返回
    # i = 0
    for line in txt_lines:
        print(line)
        movie_id = line.split("::")[0]
        print("txt movie id:")
        print(movie_id)
        for csv in csv_lines:
            if csv.split(",")[0] == movie_id:
                print("csv file :")
                print(csv)
                # print(type(csv))
                content = csv.replace(",","::")
                f = open('kg111111.txt', 'a')
                # print(content)
                f.write(content)
                f.close()
                break
        
        

csv_file = "/Users/yuhaomao/Desktop/movie-recommendation-system-/dataset/movies_director2.csv"
txt_file = "/Users/yuhaomao/Downloads/ml-1m/movies_copy.txt"
kg2txt(csv_file,txt_file)