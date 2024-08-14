#!/usr/bin/python3
import sys
import re
import signal

# Initialize counters
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

def signal_handler(sig, frame):
    """Handle SIGINT (CTRL+C) to print statistics and exit."""
    print_stats()
    sys.exit(0)

def print_stats():
    """Print the collected statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Set up signal handler
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line_count += 1
    # Parse the line using regular expressions
    match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        
        # Update metrics
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_file_size += file_size
        
    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Final stats before exiting
print_stats()
