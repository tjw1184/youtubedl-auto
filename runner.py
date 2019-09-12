#!/usr/bin/env python3

# Simple Script to replace cron for Docker

import argparse
import sys
import time
from subprocess import run


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("interval", type=float, help="Time in seconds between jobs")
    args = parser.parse_args()

    print(f"Running youtubedl-auto every {args.interval}s", file=sys.stderr)
    while True:
        start_time = time.time()
        run(["pip", "install", "--upgrade", "youtube-dl"])
        run(["/usr/local/bin/youtube-dl", "--config-location", "/youtubedl/youtube-dl.conf"])
        run_time = time.time() - start_time
        if run_time < args.interval:
            sleep_time = args.interval - run_time
            print(f"Ran for {run_time}s", file=sys.stderr)
            print(f"Sleeping for {sleep_time}s", file=sys.stderr)
            time.sleep(sleep_time)


if __name__ == "__main__":
    main()
