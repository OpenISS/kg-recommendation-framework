import csv

def movieid2txt(file_path):
    print(file_path)
    with open(file_path,encoding="utf-8") as f:
        reader = csv.reader(f)
        i = -1
        for row in reader:
            if i != -1:
                f = open('item_index2entity_id.txt', 'a')
                content = str(row[0]) + "\t" + str(i) + "\n"
                print(content)
                f.write(content)
                f.close()
            i += 1

movies_file_path = "../../../data/movies_director2.csv"
movieid2txt(movies_file_path)
