import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread
from concurrent.futures import Future

import requests

def get_quote(num):
    print(f"Getting quote {num}")
    time.sleep(1)
    response = requests.get("https://api.kanye.rest")
    # if num % 2 == 0:
    #     raise Exception('error')
    if response.status_code < 400:
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")

def print_quote(future: Future):
    print(future.result())


# 13 sec
if __name__ == '__main__':
    # s = time.perf_counter()
    # results = []
    # for i in range(100):
    #     results.append(get_quote(i))
    # print(f"Synchronious: {time.perf_counter() - s}")

    futures = []
    s = time.perf_counter()
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(30):
            # not blocking
            future = executor.submit(get_quote, i)
            # future.add_done_callback(print_quote)
            # if i % 2 == 0:
            #     future.add_done_callback(print_quote)
            futures.append(future)
            # future.
            # blocking
            # future.result()

    with open("d.txt", "w") as f:
        for future in as_completed(futures):
            f.write(future.result()['quote']+'\n')
            f.flush()


    # results = []
    # for future in futures:
    #     try:
    #         results.append(future.result())
    #     except:
    #         print('error occured')
    # with open("d.json", "w") as f:
    #     json.dump(results, f)
    print(f"Asynchronious: {time.perf_counter() - s}")
    # results2 = []
    # futures = []

# s = time.perf_counter()
# with ThreadPoolExecutor() as executor:
#     for i in range(100):
#         futures.append(executor.submit(get_quote, i))
# t =Thread(target=get_quote, args=(3,))
# t.start()
# t.join()