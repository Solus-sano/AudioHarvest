import requests
import re, json
import utils
import subprocess
import os

test_url = "https://www.bilibili.com/video/BV1r2421c7BM/?vd_source=c2f4df9bb2c6b1ce85ec841c737c1f79"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

def get_song(
        name: int, 
        url: int, 
        P: int=1,
        root: str=None,
    ) -> None:
    video_args = utils.get_video_args(url)
    

    headers["Referer"] = re.search(r'(http.*video/BV.+)/.*$',test_url).group(1)

    download_data = requests.get(
        url=utils.get_audio_url(video_args["cid_lst"][P-1],video_args["bvid"]),
        headers=headers,
    ).content
    
    assert root is not None
    song_path = os.path.join(root, name + '.aac')
    
    with open(song_path,'wb') as f:
        f.write(download_data)
        
    utils.convert_aac_to_m4a(song_path, song_path[:-4] + '.m4a')

if __name__ == '__main__':
    video_args = utils.get_video_args("https://www.bilibili.com/video/BV18r421E743/?spm_id_from=333.337.search-card.all.click&vd_source=c2f4df9bb2c6b1ce85ec841c737c1f79")
    print(video_args)