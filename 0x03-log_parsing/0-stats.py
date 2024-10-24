#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import sys
import re


def extract_data(line: str) -> dict:
    """Extracts sections of a line of HTTP request log."""
    log_format = (
            r'^(?P<ip>\S+) - \[(?P<date>[^\]]+)\] '
            r'"GET /projects/260 HTTP/1.1" (?P<status_code>\d{3}) '
            r'(?P<file_size>\d+)$'
            )
    match = re.match(log_format, line.strip())
    if match:
        return {
                'status_code': match.group('status_code'),
                'file_size': int(match.group('file_size'))
                }
    return None


def print_stats(log_data: dict) -> None:
    """Prints the accumulated statistics"""
    print(f'File size: {log_data["total_file_size"]}', flush=True)
    for code in sorted(log_data['code_frequency']):
        count = log_data['code_frequency'][code]
        if count > 0:
            print(f'{code}: {count}', flush=True)


def update_data(log_data: dict, line: str) -> None:
    """Updates log data from a given log line."""
    data = extract_data(line)
    if data:
        log_data['total_file_size'] += data['file_size']
        log_data['code_frequency'][data['status_code']] += 1


def run():
    """Start the log parser."""
    log_data = {
            'total_file_size': 0,
            'code_frequency': {str(code): 0 for code in [
                200, 301, 400, 401, 403, 404, 405, 500]}
            }
    line_count = 0

    try:
        for line in sys.stdin:
            update_data(log_data, line)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(log_data)

    except KeyboardInterrupt:
        print_stats(log_data)
    finally:
        print_stats(log_data)


if __name__ == '__main__':
    run()
