import requests
import json


def DollarPrice():
    currencies_url = "https://marshalbackend.com/coinbit/v2wyy3v9ptdrv27uqug2phxaqhggbwdx/"
    currencies = requests.get(currencies_url).json()
    currencies = json.loads(currencies)
    return(int(currencies[0]["Price"]))


def GetDate():
    update_date_url = "https://marshalbackend.com/coinbit/v2wyy3v9ptdrv27uqug2phxaqhggbwdx/"
    update_date = requests.get(update_date_url).json()
    update_date = json.loads(update_date)
    return(update_date[0]["DateFa"])
