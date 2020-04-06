import csv

def rating2txt(file_path):
    print(file_path)
    with open(file_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            userid = row[0]
            movieid = row[1]
            rating = row[2]
            timestamp = row[3]
            f = open('rating.txt', 'a')
            content = str(userid) + "::" + str(movieid) + "::"+ str(rating) + "::"+ str(timestamp)+"\n"
            # print(content)
            f.write(content)
            f.close()

rating_file_path = "../../../data/ratings.csv"
# kg_file_path = "test.csv"
rating2txt(rating_file_path)
# print(person_name)
