import os
from urllib.request import urlretrieve
from tqdm import tqdm
import zipfile


class Progress(tqdm):
    tmp = 0
    def load(self, num=1, size=1, total_size=None):
        self.total = total_size
        self.update((num - self.tmp) * size)
        self.tmp = num

def download_data(database_name, data_path):
    url = "http://files.grouplens.org/datasets/movielens/" + database_name + ".zip"
    extract_path = os.path.join(data_path, database_name)
    data_zip = database_name + ".zip"
    save_path = os.path.join(data_path, data_zip)
    extract_function = _unzip

    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    if os.path.exists(extract_path):
        print('{} already download.'.format(database_name))
        return
    
    if not os.path.exists(save_path):
        with Progress(desc='Downloading {}'.format(database_name)) as pg:
            urlretrieve(url, save_path, pg.load)

    os.makedirs(extract_path)
    extract_function(save_path, database_name, data_path)
    print('Done.')

def _unzip(save_path, database_name, data_path):
    print('Unzip file: {}'.format(database_name))
    with zipfile.ZipFile(save_path) as zf:
        zf.extractall(data_path)
    print("Unzip finish")

data_dir = '../data'
download_data('ml-1m', data_dir)