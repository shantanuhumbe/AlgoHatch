from core.global_state import GlobalState
from utils.config_loader import load_config




class HistoricalData:

    def __init__(self):
        config_path = "config/data_config.json"
        self.config = load_config(config_path)


    def collect_data(self):

        data = {}

        return data


