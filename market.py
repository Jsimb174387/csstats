import requests
import json


def percent_change(starting_value, ending_value):
    p_change = ending_value - starting_value
    p_change = 100 * p_change / starting_value
    return p_change


def check_report(min_price=1, max_price=2000, acceptable_range_min=-100, acceptable_range_max=100,
                 m_start="skinport", m_end="buff163"):
    def comparator(skin, item_dict, market_start, market_end):
        try:
            starting_price = item_dict[skin][market_start]
            ending_price = item_dict[skin][market_end]
            if market_start == "buff163":
                starting_price = starting_price["starting_at"]["price"]
            if market_end == "buff163":
                ending_price = ending_price["highest_order"]["price"]
            if market_start == "skinport":
                starting_price = starting_price["starting_at"]
            if market_end == "skinport":
                ending_price = ending_price["suggested_price"]
            if market_start == "steam":
                starting_price = starting_price["last_30d"]
            if market_end == "steam":
                ending_price = ending_price["last_30d"]
        except:
            # not handling right now
            pass
        else:
            if starting_price is not None and ending_price is not None:
                if min_price <= starting_price <= max_price and ending_price != 0:
                    percent_move = percent_change(starting_price, ending_price)
                    if acceptable_range_min < percent_move < acceptable_range_max:
                        return {skin: [percent_move, starting_price, ending_price]}

    response = requests.get("https://prices.csgotrader.app/latest/prices_v6.json")
    # Check if the request was successful
    if response.status_code == 200:
        dictionary = json.loads(response.content)
        price_dict = {}
        for item_name in dictionary.keys():
            compared = comparator(item_name, dictionary, m_start, m_end)
            if compared is not None:
                price_dict.update(compared)
        sorted_items = sorted(price_dict.items(), key=lambda x: x[1], reverse=True)
        return sorted_items

    return "failed to complete analysis"


def check_item(name):
    # {'steam': {'last_24h': 3.57, 'last_7d': 3.3, 'last_30d': 3.22, 'last_90d': 3.04}, 'lootfarm': None,
    # 'csgotm': None, 'skinport': {'suggested_price': 2.87, 'starting_at': 2.6}, 'csgoempire': 3.03, 'swapgg': 3.36,
    # 'csgoexo': None, 'cstrade': None, 'skinwallet': None, 'buff163': {'starting_at': {'price': 3.21},
    # 'highest_order': {'price': 3.04}}}
    response = requests.get("https://prices.csgotrader.app/latest/prices_v6.json")
    if response.status_code == 200:
        dictionary = json.loads(response.content)
        return dictionary[name]
