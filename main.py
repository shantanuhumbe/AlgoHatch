from core.global_state import GlobalState









def main():

    global_state = GlobalState()
    global_state.set("example_key", "example_value")
    print(global_state.get("example_key"))



if __name__ == "__main__":
    main()