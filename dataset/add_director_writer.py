import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/title/tt0371746/"
try:
    r=requests.get(url)
    r.raise_for_status()
    # print (r.encoding)
    html = r.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.body)
    source = soup.find_all(class_="credit_summary_item")
    # print(source)
    for i in source:
        print("wwwwwww")
        print(i)
        print("aaaaa")
        contents = i.findAll("a")
        print(contents)
        for ii in contents:
            str_content = str(ii)
            if str_content[15:17] == "nm":
                print("name")
            else:
                print("bushi name")

except:
    print ("failed")