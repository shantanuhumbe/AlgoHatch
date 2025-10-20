
from utils.config_loader import load_config
from data.realtime.feed import websocket_feed, api_feed
from core.global_state import global_state
from time import sleep




class MktDataLoader:

    def __init__(self):

        config_path = "config/data_config.json"
        self.config = load_config(config_path)

        if self.config["feed_type"] == "api":
            self.feed = api_feed(self.config)
        else:
            self.feed = websocket_feed(self.config)


    def start_source(self):

        while True:
            data = self.feed.get_data()
            global_state.set("market_data", data)
            sleep(self.config["poll_interval"])





