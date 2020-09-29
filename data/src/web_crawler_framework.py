import requests
from bs4 import BeautifulSoup


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
            r = requests.get(url)
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
        movie_name = row.split(",")[1]
        imdb_id = "tt" + str(row.split(",")[-1])[:-1].zfill(7)
        print(imdb_id)
        dict_tmp[movie_name] = imdb_id
    return dict_tmp

if __name__ == '__main__':
    dict_tmp = {}
    imdbid(dict_tmp)
    url="https://www.imdb.com/title/tt0114709/"
    rules = "nm"
    web_c = web_crawler(url,rules)
    print(web_c.crawler())
