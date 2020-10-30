import requests
import humanize
import time
import pytz
import datetime
from persiantools.jdatetime import JalaliDateTime
from coins import CoinsPrice, GetTime
from dollar import DollarPrice, GetDate
import os
import json

# create function that get last_update


def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]

# create function that let bot send messages


def send_message(chat_id, message_text):
    dir = '%s/secrets.json' % (os.path.dirname(__file__))
    with open(dir) as json_file:
        secret = json.load(json_file)
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(secret['bot_token'] + "sendMessage", data=params)
    return response


def main():

    day = GetDate()
    hour = GetTime()

    dollar_price = DollarPrice()
    coins = CoinsPrice()

    bitcoin_price_rial = int(coins[0] * dollar_price)
    bitcoin_sell_price_rial = humanize.intcomma(int((bitcoin_price_rial +
                                                     ((3 * bitcoin_price_rial) / 100)) / 10))
    ethereum_price_rial = int(coins[1] * dollar_price)
    ethereum_sell_price_rial = humanize.intcomma(int((ethereum_price_rial +
                                                      ((3 * ethereum_price_rial) / 100)) / 10))
    tether_price_rial = int(coins[2] * dollar_price)
    tether_sell_price_rial = humanize.intcomma(int((tether_price_rial +
                                                    ((3 * tether_price_rial) / 100)) / 10))
    xrp_price_rial = int(coins[3] * dollar_price)
    xrp_sell_price_rial = humanize.intcomma(int((xrp_price_rial +
                                                 ((3 * xrp_price_rial) / 100)) / 10))
    bitecoincash_price_rial = int(coins[4] * dollar_price)
    bitecoincash_sell_price_rial = humanize.intcomma(int((bitecoincash_price_rial +
                                                          ((3*bitecoincash_price_rial) / 100)) / 10))
    litecoin_price_rial = int(coins[5] * dollar_price)
    litecoin_sell_price_rial = humanize.intcomma(int((litecoin_price_rial +
                                                      ((3*litecoin_price_rial) / 100)) / 10))
    cardano_price_rial = int(coins[6] * dollar_price)
    cardano_sell_price_rial = humanize.intcomma(int((cardano_price_rial +
                                                     ((3*cardano_price_rial) / 100)) / 10))
    tron_price_rial = int(coins[7] * dollar_price)
    tron_sell_price_rial = humanize.intcomma(int((tron_price_rial +
                                                  ((3*tron_price_rial) / 100)) / 10))
    monero_price_rial = int(coins[8] * dollar_price)
    monero_sell_price_rial = humanize.intcomma(int((monero_price_rial +
                                                    ((3*monero_price_rial) / 100)) / 10))

    # update_id = last_update(bot_url)['message']["chat"]["id"]
    allowed_chat_ids = [965851315, -1001331723254]
    while True:

        message_text = '\U0001F514' + "اعلام نرخ لحظه ارزهای دیجیتال" + \
            '\n' + '\U0001F5D3' + " تاریخ: " + day + '\n' + '\U0000231A' + " ساعت: " + \
            hour + "\n" + '--------------------------------------------------' + '---------------------------------------------------' + \
            "\n\n" + '\U00000031' '\U0000FE0F' '\U000020E3' + " بیت کوین - Bitcoin" + "\n" + "       قیمت به دلار: " + \
            str(coins[0]) + "$" + "\n" + "       قیمت فروش: " + \
            str(bitcoin_sell_price_rial) + " تومان" + "\n\n" + '\U00000032' '\U0000FE0F' '\U000020E3' + " اتریوم - Ethereum" + "\n" + \
            "       قیمت به دلار: " + \
            str(coins[1]) + "$" + "\n" + "       قیمت فروش: " + \
            str(ethereum_sell_price_rial) + " تومان" + "\n\n" + '\U00000033' '\U0000FE0F' '\U000020E3' + " تتر - Tether" + "\n" + \
            "       قیمت به دلار: " + \
            str(coins[2]) + "$" + "\n" + "       قیمت فروش: " + \
            str(tether_sell_price_rial) + " تومان" + "\n\n" + '\U00000034' '\U0000FE0F' '\U000020E3' + " ریپل - XRP" + "\n" + \
            "       قیمت به دلار: " + \
            str(coins[3]) + "$" + "\n" + "       قیمت فروش: " + \
            str(xrp_sell_price_rial) + " تومان" + "\n\n" + '\U00000035' '\U0000FE0F' '\U000020E3' + " ببیت کوین کش - Bitcoin Cash" + "\n" + "       قیمت به دلار: " + str(coins[4]) + "$" + "\n" + "       قیمت فروش: " + str(bitecoincash_sell_price_rial) + " تومان" + "\n\n" + '\U00000036' '\U0000FE0F' '\U000020E3' + " لایت کوین - Litecoin" + "\n" + "       قیمت به دلار: " + str(coins[5]) + "$" + "\n" + "       قیمت فروش: " + str(litecoin_sell_price_rial) + " تومان" + "\n\n" + '\U00000037' '\U0000FE0F' '\U000020E3' + "کاردانو - Cardano" + "\n" + "       قیمت به دلار: " + str(coins[6]) + "$" + "\n" + "       قیمت فروش: " + str(cardano_sell_price_rial) + " تومان" + "\n\n" + '\U00000038' '\U0000FE0F' '\U000020E3' + " ترون - TRON" + "\n" + "       قیمت به دلار: " + str(coins[7]) + "$" + "\n" + "       قیمت فروش: " + str(
                tron_sell_price_rial) + " تومان" + "\n\n" + '\U00000039' '\U0000FE0F' '\U000020E3' + " مونرو - Monero" + "\n" + "       قیمت به دلار: " + str(coins[8]) + "$" + "\n" + "       قیمت فروش: " + str(monero_sell_price_rial) + " تومان" + "\n" + '--------------------------------------------------' + '---------------------------------------------------' + "\n\n" + "       برای مشاهده لیست کامل رمز ارزها لطفا از سایت ما دیدن فرمائید." + "\n\n" + '--------------------------------------------------' + '---------------------------------------------------' + "\n\n" + "کانال اعلام قیمت لحظه ای و سایر اخبار ارزهای دیجیتال " + '\U0001F447' + "\n\n" + "@coinbitiran_exchange" + "\n\n" + '\U0001F310' + " لینک سایت صرافی کوین بیت:" + "\n\n" + "https://coinbit-exchange.com/" + "\n\n" + "آسایش و اطمینان شما، هدف ماست!"
        for i in allowed_chat_ids:
            send_message(i, message_text)
        time.sleep(300.0)
        main()


main()
