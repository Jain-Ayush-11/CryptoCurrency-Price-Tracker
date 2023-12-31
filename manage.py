#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')

    def run_binance_script():
        from task.binance import BinanceWebsocketUtils
        BinanceWebsocketUtils.start_websocket_listener()

    script_thread = threading.Thread(target=run_binance_script)
    script_thread.daemon = True
    script_thread.start()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
