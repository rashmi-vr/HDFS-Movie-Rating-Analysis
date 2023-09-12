#!/usr/bin/env python3

import sys
import string
from collections import defaultdict


# Student ID: 3122831

def eprint(*args, **kwargs):
    print(args, file=sys.stderr, **kwargs)


combined = defaultdict(int)

for line in sys.stdin:
    genre, title, rating, count = line.strip().split('\t')
    # initiated the key as a tuple of genre, title, rating and value as the count of the combinations
    key = (genre, title, rating)
    combined[key] += int(count)

for key, value in combined.items():
    genre, title, rating = key
    print(f"{genre}\t{title}\t{float(rating):.1f}\t{value}")
