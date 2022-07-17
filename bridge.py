import json
import requests
import base64


def SaveOrigin(url: str, text):
    with open("./origin/"+base64.b64encode(url.encode("utf-8")).decode("utf-8"), "w") as f:
        f.write(text)


def SaveBridge(url: str, text):
    with open("./bridge/"+base64.b64encode(url.encode("utf-8")).decode("utf-8"), "w") as f:
        f.write(text)


def BaiduPan(url):
    text = requests.get(url).text
    SaveOrigin(url, text)
    bridge = text.replace(
        "t.wasmPlayer=", "window.VideoTogetherBaiduPan=t.wasmPlayer=")
    SaveBridge(url, bridge)


player_list = {}
with open("player_list.json") as f:
    player_list = json.loads(f.read())

for url in player_list["pan.baidu.com"]:
    BaiduPan(url)
