import requests
import json


def CoinsPrice():
    coins_url = "https://marshalbackend.com/coinbit/e71234d056b056c794a321e54fffc92f/?getall=0"
    coins = requests.get(coins_url).json()
    coins = json.loads(coins)
    Bitcoin = round(coins[0]["Price"], 2)
    Ethereum = round(coins[1]["Price"], 2)
    Tether = round(coins[2]["Price"], 2)
    XRP = round(coins[3]["Price"], 2)
    BitcoinCash = round(coins[4]["Price"], 2)
    Litecoin = round(coins[5]["Price"], 2)
    Cardano = round(coins[6]["Price"], 2)
    Tron = round(coins[8]["Price"], 2)
    Monero = round(coins[9]["Price"], 2)
    return(Bitcoin, Ethereum, Tether, XRP, BitcoinCash, Litecoin, Cardano, Tron, Monero)


def GetTime():
    get_time_url = "https://marshalbackend.com/coinbit/e71234d056b056c794a321e54fffc92f/?getall=0"
    get_time = requests.get(get_time_url).json()
    get_time = json.loads(get_time)
    return(get_time[0]["TimeFa"])
