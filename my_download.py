import requests
import re, json
import utils
import subprocess

test_url = "https://www.bilibili.com/video/BV1r2421c7BM/?vd_source=c2f4df9bb2c6b1ce85ec841c737c1f79"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}


if __name__ == '__main__':
    
    video_args = utils.get_video_args(test_url)
    

    headers["Referer"] = re.search(r'(http.*video/BV.+)/.*$',test_url).group(1)

    download_data = requests.get(
        url=utils.get_audio_url(video_args["cid_lst"][0],video_args["bvid"]),
        headers=headers,
    ).content
    with open('使一颗心免于哀伤.aac','wb') as f:
        f.write(download_data)
        
    utils.convert_acc_to_m4a('使一颗心免于哀伤.aac','使一颗心免于哀伤.m4a')