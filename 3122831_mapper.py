#!/usr/bin/env python3

import sys
import string
from collections import defaultdict


# Student ID: 3122831

def eprint(*args, **kwargs):
    print(args, file=sys.stderr, **kwargs)


# Get a set of words from a file
def loadYears(filename):
    items = set()
    f = open(filename)
    for line in f:
        words = line.split()
        for word in words:
            items.add(word)
    f.close()
    return items

# Start of the program
years = loadYears("years.txt")

movie_data = []
uid_dict = defaultdict(int) # referred [3]

threshold_reviews = 1500  # threshold says the number of reviews provided by a specific user

for line in sys.stdin:
    # remove leading, trailing whitespace and force to lower case
    line = line.strip().lower()
    #  Split up the line
    (uid, title, genres, year, rating) = line.split('\t')
    # removes any punctuations from the title of the movie
    title = title.translate(str.maketrans("", "", string.punctuation))
    # referred [1], [2] for the operators
    if not years or year in years:
        movie_data.append((uid, title, genres, year, rating))
        # used only to take the count of UID and analyse threshold
        uid_dict[uid] += 1

for movie in movie_data:
    uid, title, genres, year, rating = movie
    count_ = uid_dict[uid]
    # Only prints the line if the count of UIDs is less than or equal to the threshold. 
    if count_ <= threshold_reviews:
        for genre in genres.split('|'):
            print(f"{genre}\t{title}\t{float(rating):.1f}\t{1}")
