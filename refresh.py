from download import get_song
from config import args
import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":
    cfg = args.parse_args()
    
    data = pd.read_csv(cfg.source_file).values
    for item in tqdm(data):
        get_song(
            name=item[0],
            url=item[1],
            P=item[2],
            root=cfg.cache_dir
        )
    