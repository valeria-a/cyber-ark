import time
from concurrent.futures import ThreadPoolExecutor, Future, as_completed

# send many concurrent requests
import requests

quotes = []
# lock = Lock()
def get_quote(num):
    # print(f"Getting quote {num}")
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        quotes.append(response)
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")


if __name__ == '__main__':

    results2 = []
    futures = []

    s = time.perf_counter()
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(100):
            futures.append(executor.submit(get_quote, i))

    # for future in as_completed(futures):
    #     results2.append(future.result())
    print(f"Asynchronious: {time.perf_counter() - s}")