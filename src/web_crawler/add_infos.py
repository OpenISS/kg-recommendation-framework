import requests
from bs4 import BeautifulSoup
from imdb import IMDb


class web_crawler:
    def __init__(self,url,rules):
        self.url = url
        self.rules = rules
        self.directors = []
        self.writers = []
        self.stars = []
        self.count = 1
        
    def crawler(self):
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            source = soup.find_all(class_="credit_summary_item")
            for i in source:
                contents = i.findAll("a")
                for name in contents:
                    str_content = str(name)
                    if str_content[15:17] == self.rules:
                        if self.count == 1:
                            self.directors.append(name.get_text())
                        if self.count == 2:
                            self.writers.append(name.get_text())
                        if self.count == 3:
                            self.stars.append(name.get_text())
                self.count += 1
        except:
            print("failed")
            
        return self.directors, self.writers, self.stars

def imdbid(dict_tmp):
    f = open("/Users/yuhaomao/Downloads/ml-latest/movies.csv", "r")
    lines = f.readlines()
    for row in lines:
        print(row)
        count = row.split(",")[0]
        print(count)
        movie_name = row.split(",")[1]
        imdb_id = "tt" + str(row.split(",")[-1])[:-1].zfill(7)
        print(imdb_id)
        dict_tmp[movie_name] = imdb_id
        url = "https://www.imdb.com/title/" + str(imdb_id)
        rules = "nm"
        web_c = web_crawler(url, rules)
        print(web_c.crawler())
        result = ""
        for director in web_c.directors:
            result += str(count) + "\t" + "directors" + "\t" + str(director) + "\n"
            print(result)

        for writer in web_c.writers:
            result += str(count) + "\t" + "writers" + "\t" + str(writer) + "\n"
            print(result)

        for star in web_c.stars:
            result += str(count) + "\t" + "stars" + "\t" + str(star) + "\n"
            print(result)
        f = open("kg_additional.txt", "a")
        f.write(result)
        f.close()
        print(web_c.directors)
    return dict_tmp

def read_movie(dict_tmp):
    f = open("../data/movie/movie_10m/movies.dat", "r")
    lines = f.readlines()
    for row in lines:
        movie_name = row.split("::")[1]
        print(movie_name)
        print(dict_tmp[movie_name])
        
def search_id(name):
    ia = IMDb()
    search = ia.search_movie(name)
    print(search)
    for i in range(len(search)):
        id = search[i].movieID
        print(search[i]['title'] + " : " + id)

if __name__ == '__main__':
    dict_tmp = {}
    # search_id("The Grief of Others (2015)")
    # imdbid(dict_tmp)
    # read_movie(dict_tmp)
    # url="https://www.imdb.com/title/tt0114709/"
    # rules = "nm"
    # web_c = web_crawler(url,rules)
    # print(web_c.crawler())
