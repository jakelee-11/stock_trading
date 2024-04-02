# https://apiportal.koreainvestment.com/apiservice/apiservice-domestic-stock#L_aade4c72-5fb7-418a-9ff2-254b4d5f0ceb
# https://github.com/sharebook-kr/book-korea-us-stock-trading
import mojito 
import pprint

with open("../한투.key") as f: # api keys
    lines = f.readlines()
    
key = lines[0].strip()
secret = lines[1].strip()
acc_no = lines[2].strip()

broker = mojito.KoreaInvestment(api_key=key, api_secret=secret, acc_no=acc_no)

# # 잔고 조회
# resp = broker.fetch_balance()
# pprint.pprint(resp)

# # 현재가 조회 dictionaries in a dictionary
# resp = broker.fetch_price("005930")
# pprint.pprint(resp)

# # 종목코드 조회
# symbols = broker.fetch_symbols()
# print(symbols[symbols["그룹코드"] == "ST"])

# # 종목 조회 in detail
# symbols = broker.fetch_kospi_symbols()
# symbols = broker.fetch_kosdaq_symbols()
# print(symbols.head())

# # 지정가 매수
# resp = broker.create_limit_buy_order(
#     symbol="005930",
#     price=65000,
#     quantity=1
# )
# pprint.pprint(resp)

# # 시장가 매수
# resp = broker.create_market_buy_order(
#     symbol="005930",
#     quantity=10
# )

# # 지정가 매도
# resp = broker.create_limit_sell_order(
#     symbol="005930",
#     price=67000,
#     quantity=1
# )

# # 시장가 매도
# resp = broker.create_market_sell_order(
#     symbol="005930",
#     quantity=1
# )


# # 주문 취소, 전체 수량
# resp = broker.cancel_order(
#     org_no="91252",
#     order_no="0000119206",
#     quantity=4,  # 잔량전부 취소시 원주문 수량과 일치해야함
#     total=True   # 잔량전부를 의미
# )

# # 주문 취소, 일부 수량
# resp = broker.cancel_order(
#     org_no="91252",
#     order_no="0000120154",
#     quantity=2,     # 취소하고자하는 수량
#     total=False     # 잔량일부
# )
# pprint.pprint(resp)

# # 주문 정정, 전체 수량
# resp = broker.modify_order(
#     org_no="91252",
#     order_no="0000138450",
#     order_type="00",
#     price=60000,
#     quantity=4,
#     total=True
# )

# # 주문 정정, 일부 수량
# resp = broker.modify_order(
#     org_no="91252",
#     order_no="0000143877",
#     order_type="00",
#     price=60000,
#     quantity=2,
#     total=False
# )
# pprint.pprint(resp)


