import upstox_client as ucs
import requests


def get_auth_token(config):
    url = config["mktdata_creds"]["auth_url"]
    payload = {
        "code": config["mktdata_creds"]["auth_token"],
        "client_id": config["mktdata_creds"]["api_key"],
        "client_secret": config["mktdata_creds"]["api_secret"],
        "redirect_uri": config["mktdata_creds"]["redirect_uri"],
        "grant_type": "authorization_code"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()
    return response.json()["access_token"]


def get_api_client(config):

    auth_token = get_auth_token(config)
    configuration = ucs.Configuration()
    configuration.client_id = config["mktdata_creds"]["api_key"]
    configuration.client_secret = config["mktdata_creds"]["api_secret"]
    configuration.redirect_uri = config["mktdata_creds"]["redirect_uri"]
    configuration.access_token = auth_token

    api_client = ucs.ApiClient(configuration)
    return api_client

def get_quote_api(config):
    api_client = get_api_client(config)
    quote_api = ucs.MarketQuoteApi(api_client)
    return quote_api

def get_hist_api():

    hist_api = ucs.HistoryV3Api()
    return hist_api