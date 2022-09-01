import requests
from bs4 import BeautifulSoup
from imdb import IMDb
import urllib.request
import base64

class IMDB_extractor:
    def __init__(self,url,rules):
        self.url = url
        self.rules = rules
        self.directors = []
        self.writers = []
        self.stars = []
        self.count = 1
        
    def extractor(self):
        try:
#            r = requests.get(self.url)
#            r.raise_for_status()
#            html = r.text
#            soup = BeautifulSoup(html, 'html.parser')
#            source = soup.find_all(class_="credit_summary_item")
            page = requests.get(self.url)
            page.raise_for_status()
            soup = BeautifulSoup(page.content, 'html.parser')
            data = json.loads(soup.find('script', type='application/ld+json').text)
            try:
                director_qt = len(data["director"])
            except KeyError:
                director_qt = 0
            try:
                writer_qt = len(data["creator"])
            except KeyError:
                writer_qt = 0
            try:
                actor_qt = len(data["actor"])
            except KeyError:
                actor_qt = 0
            for x in range(director_qt):
                if (data["director"][x]["@type"] == "Person"):
                    self.directors.append(data["director"][x]["name"])
            for y in range(writer_qt):
                if (data["creator"][y]["@type"] == "Person"):
                    self.writers.append(data["creator"][y]["name"])
            for z in range(actor_qt):
                if (data["actor"][z]["@type"] == "Person"):
                    self.stars.append(data["actor"][z]["name"])

#            for i in source:
#                contents = i.findAll("a")
#                for name in contents:
#                    str_content = str(name)
#                    if str_content[15:17] == self.rules:
#                        if self.count == 1:
#                            self.directors.append(name.get_text())
#                        if self.count == 2:
#                            self.writers.append(name.get_text())
#                        if self.count == 3:
#                            self.stars.append(name.get_text())
#                self.count += 1
        except:
            print("failed")
            
        return self.directors, self.writers, self.stars

def imdb_extractor(dict_tmp,path):
    f = open(path, "r",encoding="utf-8")
    lines = f.readlines()
    for row in lines:
        old_movie_id = row.split("::")[0]
        movie_name = row.split("::")[1]
        imdb_id = search_id(movie_name)
        imdb_id = "tt" + imdb_id
        print(imdb_id)
        dict_tmp[movie_name] = imdb_id
        url = "https://www.imdb.com/title/" + str(imdb_id) + '/'
        get_poster(movie_name, url)
        rules = "nm"
        IMDB_e = IMDB_extractor(url, rules)
        print(IMDB_e.extractor())
        result = ""
        for director in IMDB_e.directors:
            result += str(movie_name) + "\t" + "directors" + "\t" + str(director) + "\n"
            print(result)

        for writer in IMDB_e.writers:
            result += str(movie_name) + "\t" + "writers" + "\t" + str(writer) + "\n"
            print(result)

        for star in IMDB_e.stars:
            result += str(movie_name) + "\t" + "stars" + "\t" + str(star) + "\n"
            print(result)
        f = open("../../../data/movie/kg_additional.txt", "a")
        f.write(result)
        f.close()

    return dict_tmp



def get_poster(movie_name,movie_url):
    with urllib.request.urlopen(movie_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        try:
#            image_url = soup.find('div', class_='poster').a.img['src']
            image_url = soup.find('div', class_='ipc-poster__poster-image').img['src']
            extension = '.txt'
            image_url = ''.join(image_url.partition('_')[0]) + extension
            filename =  str(movie_name) + extension
            with urllib.request.urlopen(image_url) as response:
                result = str(movie_name) + "\t" + str(base64.b64encode(response.read())) + "\n"
                f = open("../../../data/movie/kg_poster.txt", "a")
                f.write(result)
                f.close()
        except TypeError:
            pass
        
def search_id(name):
    ia = IMDb()
    search = ia.search_movie(name)
    # print(search)
    if search == []:
        return None
    else:
#        return search[0].movieID
        return search[0].getID()

if __name__ == '__main__':
    dict_tmp = {}
    imdb_extractor(dict_tmp,"../../../data/movie/movies.txt")
