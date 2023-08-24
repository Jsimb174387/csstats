import requests
import json
import config


def createJSON():
    response = requests.get(f"https://www.steamwebapi.com/steam/api/items?key={config.swa_key}")

    if response.status_code == 200:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(json.loads(response.content), f, ensure_ascii=False, indent=4)


def createDict(create=False):
    if create:
        createJSON()
    item_data = None
    item_dict = {}
    with open('data.json', 'r', encoding="utf8") as openfile:
        # Reading from json file
        item_data = json.load(openfile)
    # creating a dictionary converting markethashname to item image link
    for item in item_data:
        item_dict[item["markethashname"]] = item["itemimages"]
    with open('items.json', 'w', encoding='utf-8') as f:
        json.dump(item_dict, f, ensure_ascii=False, indent=4)


def getIcon(markethash):
    # Opens item_data, which takes in a markethashname and returns the steam image link
    item_data = None
    with open('items.json', 'r', encoding="utf8") as openfile:
        # Reading from json file
        item_data = json.load(openfile)
    return item_data[markethash]


def getmanyIcons(hashList, size = 100):
    # similar to above but more performant for multiple hashes.
    item_data = None
    urlList = []
    with open('items.json', 'r', encoding="utf8") as openfile:
        # Reading from json file
        item_data = json.load(openfile)
    for item in hashList:
        urlList.append([item_data[item[0]][0] + f"/{size}fx{size}f", item[1]])
    return urlList
