# f = open("../movie/kg_final_final.txt", "r")
# lines = f.readlines()
# for row in lines:
#     print(row)

# f = open('../movie/kg_final_final.txt', 'a')
count = 13203
for i in range(0,3883):
    f = open('../movie/kg_final_final.txt', 'a')
    result = str(i) + "\t" + str(4) + "\t" + str(count) + "\n"
    f.write(result)
    f.close()
    count += 1