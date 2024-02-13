# python code to find automatically bitcoin rate

import requests


def get_bitcoin_rate():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        rate = data['bpi']['USD']['rate']
        return float(rate.replace(',',''))
    except Exception as e:
        print("Error fetching Bitcoin rate:",e)
        return None
    
bitcoin_rate = get_bitcoin_rate()

if bitcoin_rate is not None:
    print("Current Bitcoin rate: $",bitcoin_rate)
else:
    print("Failed to retrieve Bitcoin rate.")