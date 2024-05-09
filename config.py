import argparse
import pandas as pd
import numpy as np
import os

args = argparse.ArgumentParser()

args.add_argument('--source_file', type=str, default='./source.csv')
args.add_argument('--cache_dir', type=str, default='/Users/aesir/normal_data/F_data/songs')


cfg = args.parse_args()

if __name__ == "__main__":
    init_data = pd.read_csv('./source.csv')
    data = init_data.values
    print(data)