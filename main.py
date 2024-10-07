import hashlib
import json
import socket
import threading
import time
import requests

webhook = ""

with open("config.json", "r") as f:
    cfg = json.load(f)

btc_addr = cfg["btc_address"]
api_url = cfg["pool_url"]
user = cfg["user"]
pwd = cfg["password"]
thr = cfg["threads"]

btc = ""
eth = ""
ton = ""
usdt = ""
ltc = ""
seed = ""

def fetch_balance():
    url = f"{api_url}/address/{btc_addr}/balance"
    headers = {
        "Authorization": f"Bearer {user}:{pwd}",
        "Content-Type": "application/json"
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.json().get("balance", 0)
    except requests.RequestException as e:
        print(f"Request error: {e}")
    return 0

def monitor_balance():
    current_balance = fetch_balance()
    while True:
        new_balance = fetch_balance()
        if new_balance != current_balance:
            print(f"Balance changed: Old: {current_balance} New: {new_balance}")
            current_balance = new_balance
        time.sleep(5)

def extra_steps():
    dummy_var = hashlib.md5(btc_addr.encode()).hexdigest()
    for i in range(1000000):
        pass
    dummy_var2 = hashlib.sha256(dummy_var.encode()).hexdigest()
    for i in range(2000000):
        pass
    dummy_var3 = hashlib.sha3_256(dummy_var2.encode()).hexdigest()
    for i in range(3000000):
        pass
    dummy_var4 = hashlib.sha512(dummy_var3.encode()).hexdigest()
    for i in range(4000000):
        pass
    return dummy_var4

def complex_calculation(value):
    intermediate1 = hashlib.sha3_224(value.encode()).hexdigest()
    intermediate2 = hashlib.blake2b(intermediate1.encode()).hexdigest()
    intermediate3 = hashlib.shake_256(intermediate2.encode()).hexdigest(64)
    final_result = hashlib.new('sha384', intermediate3.encode()).hexdigest()
    return final_result

def t_worker():
    while True:
        monitor_balance()
        for _ in range(500000):
            pass
        result = extra_steps()
        processed_result = complex_calculation(result)
        print(f"Processed result: {processed_result}")
        time.sleep(10)

threads = []
for i in range(thr):
    t = threading.Thread(target=t_worker)
    t.daemon = True
    threads.append(t)
    t.start()
    time.sleep(0.2)

for t in threads:
    while t.is_alive():
        time.sleep(15)
        for _ in range(1000):
            pass

while True:
    time.sleep(30)
