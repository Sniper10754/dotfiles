#!/usr/bin/env python3

from time import sleep

import subprocess
import sys
import os

DEFAULT_DISPLAY = ":1"
DEFAULT_SCREEN_SIZE = "800x600"

LOG_FILE_PATH = "/tmp/compatibility-server.log"
USAGE = f"Usage: {__file__} [Xephyr|Xwayland] [PROGRAM] [PROGRAM ARGS]"


def main():
    env = os.environ

    try:
        compatibility_server = sys.argv[1]

        if compatibility_server not in ["Xephyr", "Xwayland"]:
            raise RuntimeError()

    except:
        print(USAGE)

        exit(1)

    try:
        program_to_run = sys.argv[2]
    except IndexError:
        print(USAGE)

        exit(1)

    screen_size = env.get("SCREEN_SIZE") or DEFAULT_SCREEN_SIZE

    display = env.get("DISPLAY")
    display = display if display != ":0" else DEFAULT_DISPLAY

    with open(LOG_FILE_PATH, "w") as file:
        xephyr_process = subprocess.Popen(
            [
                f"/usr/bin/env", compatibility_server,

                "-geometry", screen_size, display
            ],

            stdout=file,
            stderr=file
        )

        subprocess.call(
            [program_to_run, *sys.argv[3::]],

            env={
                "DISPLAY": display
            },

            stdout=file,
            stderr=file
        )

    print(f"{compatibility_server} and {program_to_run} logs saved to {LOG_FILE_PATH}")
    print("Terminating compatibility server process")

    xephyr_process.terminate()


if __name__ == "__main__":
    main()
