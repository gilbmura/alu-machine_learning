#!/usr/bin/env python3
"""Display a GitHub user's location."""

import requests
import sys
import time


if __name__ == "__main__":
    res = requests.get(sys.argv[1])

    if res.status_code == 403:
        rate_limit = int(res.headers.get("X-Ratelimit-Reset", 0))
        current_time = int(time.time())
        diff = max(0, (rate_limit - current_time) // 60)
        print("Reset in {} min".format(diff))

    elif res.status_code == 404:
        print("Not found")

    elif res.status_code == 200:
        data = res.json()
        print(data["location"])
