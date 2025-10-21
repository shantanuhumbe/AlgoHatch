from core.global_state import GlobalState
from data.historical import historical_data








def main():

    global_state = GlobalState()
    global_state.set("example_key", "example_value")
    print(global_state.get("example_key"))

    historical_data_instance = historical_data.HistoricalData()
    # Example usage of historical_data_instance can be added here
    data = historical_data_instance.collect_data("NSE_EQ|INE040A01034", "2022-01-01", "2022-06-01", "minutes", "1")



if __name__ == "__main__":
    main()