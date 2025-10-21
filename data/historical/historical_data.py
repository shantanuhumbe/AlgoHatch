from _datetime import datetime

import pandas as pd

from utils.api_client import get_hist_api
from dateutil.relativedelta import relativedelta


class HistoricalData:

    def __init__(self):
        self.hist_api = get_hist_api()


    def collect_data(self, instrument, start_date, end_date, unit, interval):

        to_dates = self.__get_to_dates(start_date, end_date, unit)
        data = []
        for to_date in to_dates:
            chunk_data = self.__get_data(instrument, to_date, unit, interval)
            data.extend(chunk_data)

        # Make data as dataframe, remove duplicates,trim data till start date and sort by date
        columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'oi']
        data = pd.DataFrame(data, columns=columns)
        data = data.drop_duplicates(subset=['timestamp'])
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        start_timestamp = pd.to_datetime(start_date).tz_localize('UTC').tz_convert('Asia/Kolkata')
        data = data[data['timestamp'] >= start_timestamp]
        data = data.sort_values(by='timestamp').reset_index(drop=True)
        return data


    def __get_data(self, instrument, to_date, unit, interval):

        data = self.hist_api.get_historical_candle_data(instrument,unit,interval,to_date)
        return data.data.candles

    def __get_to_dates(self, start_date, end_date, unit):

        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        to_dates = []
        decrement = self.__get_decrement(unit)
        to_dates.append(end_date.strftime("%Y-%m-%d"))
        while end_date > start_date:
            end_date = end_date - relativedelta(months=decrement)
            to_dates.append(end_date.strftime("%Y-%m-%d"))
        return to_dates



    @staticmethod
    def __get_decrement(unit, ):

        if unit == "minutes":
            return 1
        elif unit == "hours":
            return 3
        elif unit == "days":
            return 10*12
        else :
            return 12