#!/usr/bin/python3
"""
This is the append_write function.
"""


import sys
import signal


total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """
    Prints the computed statistics.
    """

    print("Total file size:", total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")
    print()

def signal_handler(signal, frame):
    """
    Handles the keyboard interruption (CTRL + C).
    """

    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    components = line.split()

    file_size = int(components[-1])
    status_code = int(components[-2])

    total_file_size += file_size
    status_code_counts[status_code] += 1

    line_count += 1

    if line_count % 10 == 0:
        print_statistics()
