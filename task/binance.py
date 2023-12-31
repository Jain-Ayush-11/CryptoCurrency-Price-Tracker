import websocket
import json

class BinanceWebsocketUtils:

    @classmethod
    def on_message(cls, ws, message):
        data = json.loads(message)
        # if 'p' in data:
        #     print(f"price is: {data['p']}")

    @classmethod
    def on_error(cls, ws, error):
        print("error reported: ", error)

    @classmethod
    def on_close(cls, ws, close_status_code, close_msg):
        print("websocket closed")

    @classmethod
    def on_open(cls, ws):
        ws.send(json.dumps({"method": "SUBSCRIBE", "params": ["btcusdt@trade"]}))

    @classmethod
    def start_websocket_listener(cls):
        # websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@trade",
                                    on_message=cls.on_message,
                                    on_error=cls.on_error,
                                    on_close=cls.on_close)
        ws.on_open = cls.on_open
        ws.run_forever()
