import websocket
import json
from core.models import UserAlert
from core.tasks import send_price_alerts
from core.constants import *

class BinanceWebsocketUtils:

    @classmethod
    def on_message(cls, ws, message):
        data = json.loads(message)
        if 'p' in data:
            qs = UserAlert.objects.filter(price=data['p'], triggered=False)
            if qs.exists():
                emails = qs.values_list('user__email', flat=True)
                send_price_alerts.delay(list(emails), data['p'])
                qs.update(triggered=True)

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

class CacheUtils:

    @classmethod
    def get_user_alerts_cache_key(cls, request):
        if request.query_params.get('status', None):
            cache_key = USER_ALERT_STATUS_CACHE_KEY.format(user_id=request.user.id, status=request.query_params.get('status'))
        else:
            cache_key = USER_ALERT_CACHE_KEY.format(user_id=request.user.id)
        return cache_key
