import os

from core.utils.env_reader import read_env


def get_int(num: (str, int)) -> int:
    try:
        return int(num)
    except TypeError:
        pass


env = os.environ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

read_env(base_dir=BASE_DIR)

HOST = env.get("HOST") or "0.0.0.0"
PORT = get_int(env.get("PORT")) or 8000
API_KEY = env.get("API_KEY")
TASK_TIME_MINUTES = get_int(env.get("TASK_TIME_MINUTES"))
BROKER = env.get("BROKER")
