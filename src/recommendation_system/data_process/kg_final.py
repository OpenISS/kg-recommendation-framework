from random import sample

def kg_final(file_path,movie_dict,relation_dict,person_dict):
    f = open(file_path, "r", encoding="utf-8")
    lines = f.readlines()
    movie_count = 0
    relation_count = 0
    person_count = 3884
    for triple in lines:
        triple = triple.replace("\n","")
        triple_list = triple.split("\t")
        movie_name = triple_list[0]
        relation = triple_list[1]
        person = triple_list[2]
        print(triple_list)
        result = ""
        if movie_name not in movie_dict:
            movie_dict[movie_name] = movie_count
            movie_count += 1
        if relation not in relation_dict:
            relation_dict[relation] = relation_count
            relation_count += 1
        if person not in person_dict:
            person_dict[person] = person_count
            person_count += 1

        # result += str(movie_dict[movie_name]) + "\t" + str(relation_dict[relation]) + "\t" + str(person_dict[person]) + "\n"
        # f = open("../../../data/movie/kg_final.txt", "a")
        # f.write(result)
        # f.close()

def rating_final(rating_file_path,movie_dict):
    f = open(rating_file_path, "r", encoding="utf-8")
    lines = f.readlines()
    movies = movie_dict.values()
    movie_list = []
    for i in movies:
        movie_list.append(i)
    positive_list = []
    last_user = lines[0].split("::")[0]
    result = ""
    for triple in lines:
        print(triple)
        triple = triple.replace("\n","")
        triple_list = triple.split("::")

        user_id = triple_list[0]
        movie_name = triple_list[1]
        rating = triple_list[2]
        if user_id != last_user:
            for i in positive_list:
                result += str(user_id) + "\t" + str(i) + "\t" + "1" + "\n"
            negetive = list(set(movie_list) - set(positive_list))
            negitive_list = sample(negetive,len(positive_list))
            for i in negitive_list:
                result += str(user_id) + "\t" + str(i) + "\t" + "0" + "\n"
            positive_list = []

            f = open("../../../data/movie/ratings_final.txt", "a")
            f.write(result)
            f.close()
            result = ""
            
        if int(rating) > 4:
            positive_list.append(movie_dict[movie_name])


def rating_final_user(rating_file_path, movie_dict,user_file_path):
    user_file = open(user_file_path, "r", encoding="utf-8")
    lines = user_file.readlines()
    user_dict = {}
    user_age_dict = {"1":"0","56":"6","25":"2","45":"4","50":"5","35":"3","18":"1"}
    for user in lines:
        user = user.replace("\n","")
        user_list = user.split("::")
        print(user_list)
        user_id = user_list[0]
        user_gender = 1 if user_list[1] == "M" else 0
        user_age = user_age_dict[user_list[2]]
        user_job = user_list[3].zfill(2)
        user_dict[user_id] = str(user_id) + "\t" + str(user_gender) + "\t" + str(user_age) + "\t" + str(user_job)

    f = open(rating_file_path, "r", encoding="utf-8")
    lines = f.readlines()
    movies = movie_dict.values()
    movie_list = []
    for i in movies:
        movie_list.append(i)
    positive_list = []
    last_user = lines[0].split("::")[0]
    result = ""
    for triple in lines:
        print(triple)
        triple = triple.replace("\n", "")
        triple_list = triple.split("::")

        user_id = triple_list[0]
        movie_name = triple_list[1]
        rating = triple_list[2]
        if user_id != last_user:
            for i in positive_list:
                result += str(user_dict[user_id]) + "\t" + str(i) + "\t" + "1" + "\n"
            negetive = list(set(movie_list) - set(positive_list))
            negitive_list = sample(negetive, len(positive_list))
            for i in negitive_list:
                result += str(user_dict[user_id]) + "\t" + str(i) + "\t" + "0" + "\n"
            positive_list = []

            f = open("../../../data/movie/ratings_final.txt", "a")
            f.write(result)
            f.close()
            result = ""

        if int(rating) > 4:
            positive_list.append(movie_dict[movie_name])
    
    


kg_file_path = "../../../data/movie/kg.txt"
movie_dict = {}
relation_dict = {}
person_dict = {}
kg_final(kg_file_path,movie_dict,relation_dict,person_dict)

rating_file_path = "../../../data/movie/rating.txt"
user_file_path = "../../../data/movie/users.dat"
# rating_final(rating_file_path,movie_dict)
rating_final_user(rating_file_path,movie_dict,user_file_path)
