import requests, json, datetime
import pandas as pd
import datetime

url_assets = "http://api.coincap.io/v2/assets"
data_format = '%Y-%m-%d'


def get_assets_symbol():
    assets = requests.get(url_assets).json()
    assets_symbol = [i['symbol'] for i in assets['data']]
    return assets_symbol

def get_assets():
    assets = requests.get(url_assets).json()
    currency = {}
    for i in assets['data']:
        currency[i['symbol']] = i['id']
    return currency

def get_milliseconds(data):
    # dt_obj = datetime.strptime(data, data_format)
    millisec = data.timestamp() * 1000
    return millisec

def get_df(asset, start_date, end_date):
    data1 = get_milliseconds(datetime.datetime.strptime(start_date, data_format))
    data2 = get_milliseconds(datetime.datetime.strptime(end_date, data_format) + datetime.timedelta(days=1))
    url = f"http://api.coincap.io/v2/assets/{asset}/history?interval=d1&start={data1}&end={data2}"
    data = requests.get(url).json()
    if 'data' in data:
        price = [float(i['priceUsd']) for i in data['data']]
        t = [i['date'] for i in data['data']]
        d = {'price': price, 'time': t}
        df = pd.DataFrame(data=d)
    else:
        d = {'price': [], 'time': []}
        df = pd.DataFrame(data=d)
    return df

