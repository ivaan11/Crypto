import requests
import time
import os

def fetch_book_data(exchange, crypto):
    if exchange == "coinbase_pro":
        url = "https://api.pro.coinbase.com/products/" + crypto + "/book?level=2"
        # url = "https://api.pro.coinbase.com/products/{crypto}/book?level=2"
        print( "URL:-", url)
    else:
        print("Failed to fetch book data")
        return None

    response = requests.get(url)
    if response.status_code == 200:
        print("Fetch completed")
        return response.json()
    else:
        print("failed to Fetch")
        return None



def extract_data(order_book, amount):
    # bids = order_book['bids']
    # asks = order_book['asks']
    # total_bid_amount = 0
    # total_ask_amount = 0
    # extracted_bids = []
    # extracted_asks = []
    # for bid in bids:
    #     print(bid)
    #     total_bid_amount += float(bid[1])
    #     extracted_bids.append(bid)
    #     print("total_bid_amount", total_bid_amount)
    #     if total_bid_amount >= amount:
    #         break
    # for ask in asks:
    #     total_ask_amount += float(ask[1])
    #     extracted_asks.append(ask)
    #     print("total_ask_amount", total_ask_amount)
    #     if total_ask_amount >= amount:
    #         break
    # return extracted_bids, extracted_asks

    bids = []
    asks = []
    total_bid_volume = 0
    total_ask_volume = 0
    for bid in order_book['bids']:
        if total_bid_volume + float(bid[1]) > amount:
            bids.append((bid[0], amount - total_bid_volume))
            break
        bids.append((bid[0], bid[1]))
        total_bid_volume += float(bid[1])
    for ask in order_book['asks']:
        if total_ask_volume + float(ask[1]) > amount:
            asks.append((ask[0], amount - total_ask_volume))
            break
        asks.append((ask[0], ask[1]))
        total_ask_volume += float(ask[1])
    return bids, asks

def append_data(data, exchange, crypto):
    time_frame = time.strftime('%Y%m%d%H%M%S')
    filename = "" + exchange + "_" + crypto + "_" + time_frame + ".json"
    print("Filename Path", filename)
    with open(filename, "w") as file:
        file.write(str(data))

if __name__ == "__main__":
    exchanges = ["coinbase_pro"]
    symbols = ["BTC-USD", "ETH-USD"]
    amount = 100000.00
    poll_interval = 60

    while True:
        for exchange in exchanges:
            for crypto in symbols:
                order_book = fetch_book_data(exchange, crypto)
                if order_book:
                    bids, asks = extract_data(order_book, amount)
                    data = {"bids": bids, "asks": asks}
                    append_data(data, exchange, crypto)
        time.sleep(poll_interval)
