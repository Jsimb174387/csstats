import json
import os
import requests
from PIL import Image

from icon import display, serve_pil_image
from flask import Flask, render_template

from market import check_report, check_item

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/image")
def serve_img():
    return display("RevolutionCase",
                   "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQNqhpOSV-fRPasw8rsUFJ5KBFZv668FFQynaHMJT9B74-ywtjYxfOmMe_Vx28AucQj3brAoYrz3Fay_kY4MG_wdYeLMlhpLMaM-1U")


@app.route('/data')
def data():
    # Create a Market instance
    # Specify the name of the item you're interested in
    response = requests.get("https://prices.csgotrader.app/latest/prices_v6.json")
    return response.content


@app.route('/test/<m_start>')
def back(m_start):
    # Create a Market instance
    # Specify the name of the item you're interested in
    return m_start


@app.route('/market/<start>/<end>/<amount>')
def market(start, end, amount):
    # def check_report(min_price=1, max_price=2000, acceptable_range_min=-100, acceptable_range_max=100,
    # m_start="skinport", m_end="buff163"):
    info = json.dumps(check_report(m_start=str(start), m_end=str(end))[0:int(amount)])
    # return str(check_report(m_start=str(start), m_end=str(end))[0:int(amount)])
    return info


@app.route('/market/<item_name>')
def item_info(item_name):
    return check_item(item_name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
