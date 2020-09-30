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

def imdbid(dict_tmp,path):
    f = open(path, "r",encoding="utf-8")
    lines = f.readlines()
    for row in lines:
        # print(row)
        old_movie_id = row.split("::")[0]
        # print(old_movie_id)
        movie_name = row.split("::")[1]
        # print(movie_name)
        imdb_id = search_id(movie_name)
        # print(imdb_id)
        imdb_id = "tt" + imdb_id
        print(imdb_id)
        dict_tmp[movie_name] = imdb_id
        url = "https://www.imdb.com/title/" + str(imdb_id)
        rules = "nm"
        web_c = web_crawler(url, rules)
        print(web_c.crawler())
        result = ""
        for director in web_c.directors:
            result += str(movie_name) + "\t" + "directors" + "\t" + str(director) + "\n"
            print(result)

        for writer in web_c.writers:
            result += str(movie_name) + "\t" + "writers" + "\t" + str(writer) + "\n"
            print(result)

        for star in web_c.stars:
            result += str(movie_name) + "\t" + "stars" + "\t" + str(star) + "\n"
            print(result)
        f = open("../../data/movie/kg_additional.txt", "a")
        f.write(result)
        f.close()

    return dict_tmp
        
def search_id(name):
    ia = IMDb()
    search = ia.search_movie(name)
    # print(search)
    if search == []:
        return None
    else:
        return search[0].movieID
    # for i in range(len(search)):
    #     id = search[i].movieID
    #     print(search[i]['title'] + " : " + id)

if __name__ == '__main__':
    dict_tmp = {}
    imdbid(dict_tmp,"../../data/movie/movies.txt")
