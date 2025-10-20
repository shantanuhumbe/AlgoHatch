from threading import Lock


class GlobalState:

    def __init__(self):
        self._lock = Lock()
        self.state = {
            "market_data": {},
            "orders": {},
            "positions": {},
            "signals": {},
            "config": {},
        }

    def get(self, key):
        with self._lock:
            return self.state.get(key)

    def set(self, key, value):
        with self._lock:
            self.state[key] = value

    def update(self, key, func):
        with self._lock:
            self.state[key] = func(self.state.get(key))


global_state = GlobalState()