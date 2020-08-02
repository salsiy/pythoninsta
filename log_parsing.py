#!/usr/bin/env python3

# Required modules
import sys
import re

log_file = sys.argv[1]
usernames = {}

with open(log_file) as file:
    for line in file:
        if "CRON" not in line:
            continue
        pattern = r"user \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)