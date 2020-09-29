import csv
import urllib.request
from bs4 import BeautifulSoup
from imdb import IMDb
import base64

# movie_id = 'tt0095016'
# movie_url = "https://www.imdb.com/title/" + movie_id
# domain = 'http://www.imdb.com'

def get_poster(movie_id,movie_url):
  with urllib.request.urlopen(movie_url) as response:
      html = response.read()
      soup = BeautifulSoup(html, 'html.parser')
      # Get url of poster image
      try:
          image_url = soup.find('div', class_='poster').a.img['src']
          # TODO: Replace hardcoded extension with extension from string itself
          extension = '.txt'
          image_url = ''.join(image_url.partition('_')[0]) + extension
          filename =  str(movie_id) + extension
          with urllib.request.urlopen(image_url) as response:
              with open(filename, 'wb') as out_image:
                  out_image.write(base64.b64encode(response.read()))
              # with open('movie_poster.csv', 'a', newline='') as out_csv:
              #     writer = csv.writer(out_csv, delimiter=',')
              #     writer.writerow([movie_id, image_url])
      # Ignore cases where no poster image is present
      except AttributeError:
          pass

def search_id(name):
    ia = IMDb()
    search = ia.search_movie(name)
    # print(search)
    if search == []:
        return
    else:
        id = "tt" + str(search[0].movieID)
        return id
    # for i in range(len(search)):
    #     id = search[i].movieID
    #     print(search[i]['title'] + " : " + id)

# movie_path = "/Users/yuhaomao/Downloads/ml-1m/movies.txt"
# f_txt = open(movie_path, encoding="ISO-8859-1")
# lines = f_txt.readlines()  # 读取全部内容 ，并以列表方式返回
# for line in lines:
#     movie_name = line.split("::")[1]
#     search_id(movie_name)
get_poster(1,"https://www.imdb.com/title/tt0371746/")
# id = search_id("Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)")
# if id == None:
#     print("Ssss")
# else:
#     print("aa")