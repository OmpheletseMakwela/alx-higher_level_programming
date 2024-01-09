#!/usr/bin/python3
"""import module."""
import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) >= 9:
                status_code = parts[8]
                file_size = int(parts[9])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_file_size += file_size
                line_count += 1

                if line_count % 10 == 0:
                    print(f'Total file size: File size: {total_file_size}')
                    for code in sorted(status_codes.keys()):
                        if status_codes[code] > 0:
                            print(f'{code}: {status_codes[code]}')
                    print()

        except KeyboardInterrupt:
            raise

except KeyboardInterrupt:
    print(f'Total file size: File size: {total_file_size}')
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f'{code}: {status_codes[code]}')
