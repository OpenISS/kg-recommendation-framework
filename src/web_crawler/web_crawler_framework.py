import requests
from bs4 import BeautifulSoup


class web_crawler:
    def __init__(self,url,rules,class_name):
        self.url = url
        self.rules = rules
        self.class_name = class_name
        self.directors = []
        self.writers = []
        self.stars = []
        self.count = 1
        
    def crawler(self):
        try:
            r = requests.get(url)
            r.raise_for_status()
            html = r.text
            soup = BeautifulSoup(html,'html.parser')
            source = soup.find_all(class_= self.class_name)
            # source = soup.find_all(class_="titleReviewBarItem titleReviewbarItemBorder")
            for i in source:
                # print(i)
                contents = i.findAll("a")
                for name in contents:
                    # soup2.select('a')[0]['href']
                    str_content = str(name)
                    if str(name['href'])[0:6] == self.rules:
                    # if str_content[15:17] == self.rules:
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


if __name__ == '__main__':
    url="https://www.imdb.com/title/tt0371746/"
    href_rules = "/name/"
    class_name = "credit_summary_item"
    web_c = web_crawler(url,href_rules,class_name)
    print(web_c.crawler())

