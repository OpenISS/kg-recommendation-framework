import urllib.request
from bs4 import BeautifulSoup
import base64

def get_poster(movie_name,movie_url):
    with urllib.request.urlopen(movie_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        try:
            image_url = soup.find('div', class_='poster').a.img['src']
            extension = '.txt'
            image_url = ''.join(image_url.partition('_')[0]) + extension
            filename =  str(movie_name) + extension
            with urllib.request.urlopen(image_url) as response:
                result = str(movie_name) + "\t" + str(base64.b64encode(response.read()))
                f = open("../../data/movie/kg_poster.txt", "a")
                f.write(result)
                f.close()
                # with open(filename, 'wb') as out_image:
                #     out_image.write(base64.b64encode(response.read()))
        except AttributeError:
            pass

# url = "https://www.imdb.com/title/" + imdb_id +"/"
# get_poster(1,"https://www.imdb.com/title/tt0371746/")