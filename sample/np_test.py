# import numpy as np
#
# path = "../src/recommendation_system/model/movie/vocab/user_genders_matrix.txt"
# gender_emb = np.loadtxt(path, dtype=np.float32)
# print(gender_emb.shape)
# print(gender_emb)
# def maxProfit( prices):
# 		# 贪心：只要当天价格比第二天低就买入 在第二天卖出。
#         if bool(prices) == False or len(prices) < 2:
#             return 0
#         maxProfit = 0
#         for i in range(1, len(prices)):
#             maxProfit += max(0, prices[i] - prices[i - 1])
#         return maxProfit
#
# prices = [1, 4, 5,9]
# fee = 2
# print(maxProfit(prices))

# input_all = input()
# input_list = input_all.split(" ")
# print(input_list)
# lingdai_n = int(input_list[0])
# kuzi_n = int(input_list[1])
# maozi_n = int(input_list[2])
# chenshan_n = int(input_list[3])
# lingdai_price = int(input_list[4])
# kuzi_price = int(input_list[5])
# maozi_price = int(input_list[6])
#
# dict_price = {}
# dict_price[maozi_price] = maozi_n
# dict_price[kuzi_price] = kuzi_n
# dict_price[lingdai_price] = lingdai_n
#
# print(dict_price)
# result = 0
# while chenshan_n > 0:
#     if dict_price[maozi_price] > 0:
#         if dict_price[maozi_price] > chenshan_n:
#             result += chenshan_n * maozi_price
#             chenshan_n = 0
#             print(result)
#         else:
#             result = dict_price[maozi_price] * maozi_price
#             chenshan_n -= maozi_n
#             dict_price[maozi_price] = 0
#     elif dict_price[kuzi_price] > 0:
#         # dict_price[kuzi_price] -= 1
#         # result += kuzi_price
#         # chenshan_n -= 1
#         if dict_price[kuzi_price] > chenshan_n:
#             result += chenshan_n * kuzi_price
#             chenshan_n = 0
#             print(result)
#         else:
#             result = dict_price[kuzi_price] * kuzi_price
#             chenshan_n -= kuzi_n
#             dict_price[kuzi_price] = 0
#     elif dict_price[lingdai_price] > 0:
#         # dict_price[lingdai_price] -= 1
#         # result += lingdai_price
#         # chenshan_n -= 1
#         if dict_price[lingdai_price] > chenshan_n:
#             result += chenshan_n * lingdai_price
#             chenshan_n = 0
#             print(result)
#         else:
#             result = dict_price[lingdai_price] * lingdai_price
#             chenshan_n -= kuzi_n
#             dict_price[lingdai_price] = 0

# print(result)

# input_all = input()
# input_list = input_all.split(" ")
# print(input_list)
# lingdai_n = int(input_list[0])
# kuzi_n = int(input_list[1])
# maozi_n = int(input_list[2])
# chenshan_n = int(input_list[3])
# lingdai_price = int(input_list[4])
# kuzi_price = int(input_list[5])
# maozi_price = int(input_list[6])
#
# dict_price = {}
# dict_price[maozi_price] = maozi_n
# dict_price[kuzi_price] = kuzi_n
# dict_price[lingdai_price] = lingdai_n
#
# list_tmp = [lingdai_price,kuzi_price,maozi_price]
# list_tmp.sort()
#
# zuigui = list_tmp[-1]
# dier = list_tmp[1]
# pianyi = list_tmp[0]
#
# result = 0
#
# if chenshan_n - dict_price[zuigui] < 0:
#     result += chenshan_n*zuigui
# else:
#     result += zuigui * dict_price[zuigui]
#     chenshan_n -= dict_price[zuigui]
#     dict_price[zuigui] = 0
#     if chenshan_n - dict_price[dier] < 0:
#         result += chenshan_n*dier
#     else:
#         result += dier * dict_price[dier]
#         chenshan_n -= dict_price[dier]
#         dict_price[dier] = 0
#         if chenshan_n - dict_price[pianyi] < 0:
#             result += chenshan_n*pianyi
#         else:
#             result += pianyi * dict_price[pianyi]
#             chenshan_n -= dict_price[pianyi]
#             dict_price[pianyi] = 0
#
# print(result)

input_all = input()
input_list = input_all.split(" ")
lingdai_n = int(input_list[0])
kuzi_n = int(input_list[1])
maozi_n = int(input_list[2])
chenshan_n = int(input_list[3])
lingdai_price = int(input_list[4])
kuzi_price = int(input_list[5])
maozi_price = int(input_list[6])

dict_price = {}
dict_price[maozi_price] = maozi_n
dict_price[kuzi_price] = kuzi_n
dict_price[lingdai_price] = lingdai_n

list_price = [maozi_price,kuzi_price,lingdai_price]
list_price.sort()
gui = list_price[-1]
zhong = list_price[1]
cha = list_price[0]

result = 0


result = gui*(min(dict_price[gui],chenshan_n)) + zhong*(min(dict_price[zhong],max(0,chenshan_n-dict_price[gui]))) + cha*(min(dict_price[cha],max(0,chenshan_n-dict_price[gui]-dict_price[zhong])))

print(result)