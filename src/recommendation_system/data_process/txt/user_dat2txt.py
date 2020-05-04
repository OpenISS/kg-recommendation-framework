import csv

def userdat2txt(file_path):
    print(file_path)
    f = open(file_path, "r")
    lines = f.readlines()
    i = 0
    
    for row in lines:
        userid = row.split("::")[0]
        gender = row.split("::")[1]
        age = row.split("::")[2]
        job = row.split("::")[3]
        f = open('users_info.txt', 'a')
        content = str(userid) + "\t" + str(gender)+ "\t" + str(age) + "\t" + str(job) + "\n"
        print(content)
        f.write(content)
        f.close()
        i += 1


users_dat_file_path = "../../../../data/movie/users.dat"
userdat2txt(users_dat_file_path)
