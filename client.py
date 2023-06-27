import requests
import string
import random
from time import sleep
from uuid import uuid4
import os
import dotenv
from logger import log

dotenv.load_dotenv()
APP_HOST = os.environ["APP_HOST"] = "localhost"
APP_PORT = os.environ["APP_PORT"] = "8000"

API_URL = f"http://fastapi-app:{APP_PORT}/api/v1"
TEXT_ENTRY_PREFIX = "/text"


def generate_random_string(length: int = 16) -> str:
    letters_and_digits = string.ascii_letters + string.digits
    return "".join(random.choice(letters_and_digits) for _ in range(length))


while True:
    sleep(10)
    count = random.randint(10, 100)
    entries = [
        {"uuid": str(uuid4()), "text": generate_random_string()} for _ in range(count)
    ]
    with requests.post(f"{API_URL}{TEXT_ENTRY_PREFIX}/new", json=entries) as res:
        log(f"Inserted {len(entries)} entries")

    with requests.get(f"{API_URL}{TEXT_ENTRY_PREFIX}/10") as res:
        if res.status_code == 200:
            entries_to_delete = res.json()
        else:
            log(f"ERROR: {res.status_code}")
            break
        for entry in entries_to_delete:
            with requests.delete(f"{API_URL}{TEXT_ENTRY_PREFIX}/{entry['uuid']}"):
                pass
        log(f"Deleted {len(entries_to_delete)} entries")
