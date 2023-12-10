#!/usr/bin/env python3

from io import StringIO
from time import sleep

import subprocess
import logging
import sys
import os

DEFAULT_DISPLAY = ":1"
DEFAULT_SCREEN_SIZE = "800x600"

LOG_FILE_PATH = "/tmp/compatibility-server.log"
USAGE = f"Usage: {__file__} [Xephyr|Xwayland] [PROGRAM] [PROGRAM ARGS]"

ENV = os.environ

logging.basicConfig(
    format="%(filename)s:%(lineno)d %(levelname)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE_PATH),
    ]
)

logging.getLogger().setLevel(logging.DEBUG)

def select_available_display() -> str:
    env_display = ENV.get("display")
    
    new_display = None

    if env_display != None:
        new_display_number = int(env_display.lstrip(':'))

        new_display_number =+ 1

        new_display = f":{new_display_number}"
    else:
        new_display = DEFAULT_DISPLAY

    logging.debug(f"chosen display: {new_display}")

    return new_display

def main():

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

    screen_size = ENV.get("SCREEN_SIZE") or DEFAULT_SCREEN_SIZE

    display = select_available_display()

    env = dict()

    env.update(os.environ)
    env["DISPLAY"] = display

    buffer = StringIO()

    xephyr_process = subprocess.Popen(
        [
            f"/usr/bin/env", compatibility_server,
            "-geometry", screen_size, env["DISPLAY"]
        ],
        env=env,

        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    program_to_run_call = subprocess.Popen(
        [program_to_run, *sys.argv[3::]],

        env=env,

        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    program_to_run_call.wait()
    xephyr_process.terminate()

    buffer.write(xephyr_process.stdout.read().decode("utf-8"))
    buffer.write(xephyr_process.stderr.read().decode("utf-8"))

    buffer.write(program_to_run_call.stdout.read().decode("utf-8"))
    buffer.write(program_to_run_call.stderr.read().decode("utf-8"))

    logging.debug(f"Xephyr and window manager output: {buffer.read()}")

    logging.info(f"{compatibility_server} and {program_to_run} logs saved to {LOG_FILE_PATH}")
    logging.info("Terminating compatibility server process")

    xephyr_process.terminate()


if __name__ == "__main__":
    main()
