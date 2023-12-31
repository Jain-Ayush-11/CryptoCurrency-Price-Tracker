from django.apps import AppConfig
import threading


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        def run_binance_script():
            from task.binance import BinanceWebsocketUtils
            BinanceWebsocketUtils.start_websocket_listener()

        script_thread = threading.Thread(target=run_binance_script)
        script_thread.daemon = True
        script_thread.start()
