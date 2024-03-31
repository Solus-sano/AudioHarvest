import requests
import re, json
import subprocess

def get_video_args(url):
    api_url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + re.search(r'/BV(.+)\/.*', url).group(1)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    web_interface_response = requests.get(
        url=api_url,
        headers=headers
    )
    assert web_interface_response.status_code == 200
    
    web_interface_data = web_interface_response.json()
    aid = web_interface_data["data"]["aid"]
    bvid = web_interface_data["data"]["bvid"]
    cid_lst = [item['cid'] for item in web_interface_data["data"]["pages"]]
    
    video_args = {
        "aid": aid,
        "bvid": bvid,
        "cid_lst": cid_lst
    }
    return video_args

def get_audio_url(cid, bvid):
    play_url = f"https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&fnval=16"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    play_respnose = requests.get(
        url=play_url,
        headers=headers
    )
    assert play_respnose.status_code == 200
    play_json = play_respnose.json()
    audio_url = play_json["data"]["dash"]["audio"][0]["baseUrl"]
    return audio_url

def convert_aac_to_m4a(input_acc_path, output_m4a_path):
    command = [
        'ffmpeg',
        '-i', input_acc_path,  
        output_m4a_path  
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f'转换成功: {input_acc_path} -> {output_m4a_path}')
    except subprocess.CalledProcessError:
        print('转换失败')