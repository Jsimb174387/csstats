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


createDict()