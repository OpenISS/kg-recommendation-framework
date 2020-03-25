import argparse
import numpy as np
from data_loader import load_data
from train import train

np.random.seed(555)

parser = argparse.ArgumentParser()

# movie
parser.add_argument('-dataset', type=str, default='movie', help='which dataset to use')

show_loss = False
show_topk = False

args = parser.parse_args()
data = load_data(args)
train(args, data, show_loss, show_topk)