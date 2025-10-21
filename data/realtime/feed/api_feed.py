from utils.api_client import get_quote_api



class ApiFeed(object):

    def __init__(self, config):

        self.quote_api = get_quote_api(config)
        self.instruments = config["instruments"]

    def get_data(self):

        data = self.quote_api.get_quote(self.instruments,3)

        return data