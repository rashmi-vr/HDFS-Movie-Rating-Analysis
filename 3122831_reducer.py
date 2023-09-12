#!/usr/bin/env python3
import sys


# Student ID: 3122831

def eprint(*args, **kwargs):
    print(args, file=sys.stderr, **kwargs)


def getMax(counts):
    max = 0
    maxName = "?"  # "?" may also represent None or an empty string
    for m in counts:
        if counts[m] > max:
            max = counts[m]
            maxName = m
    return (maxName, max)


minVotes = 15

movie_ratings_dict = {}

for line in sys.stdin:
    # parse the input we got from our mapper or combiner
    genre, title, rating, count = line.strip().split('\t')
    if int(count) >= minVotes:
        # consider only ratings which has more count than minVotes
        # the key and value has been initiated as tuple so that its immutable
        key = (genre, title)
        value = (rating, count)
        if key in movie_ratings_dict:
            # the value 'ratings & count' has been saved to a tuple(immutable) inside a list for easy computation
            arr.append(value)
            movie_ratings_dict[key] = arr
            # eg : ('adventure', 'commando '): [('3.0', '3'), ('3.5', '2')]
        else:
            arr = [value]
            movie_ratings_dict[key] = arr

avg_ratings_dict = {}  # created a new dictionary

for key, value in movie_ratings_dict.items():
    avg_rating = 0
    total_rating = 0
    total_count = 0
    genre, title = key

    for item in value:
        rating, count = item
        rating, count = float(rating), float(count)
        total_rating = total_rating + (rating * count)
        total_count += count
    avg_rating = round(total_rating / total_count, 2)

    # average rating of the movie in particular genre will be taken
    # initiated the key of new dict as genre
    new_key = genre
    if new_key in avg_ratings_dict:
        new_arr.append((title, avg_rating))
        avg_ratings_dict[new_key] = new_arr  # the avg. rating eg: animation: [('bolt ', 3.3), ('brave ', 3.7)]
    else:
        new_arr = [(title, avg_rating)]
        avg_ratings_dict[new_key] = new_arr

# to calculate the highest avg. rating movie in each genre
for key, value in avg_ratings_dict.items():
    temp = dict(value)  # temp eg: {'bolt ': 3.3, 'brave ': 3.7, 'zootopia ': 3.06}
    max_rating = getMax(temp)
    avg_ratings_dict[key] = max_rating  # output eg: action: ('yojimbo ', 4.64)

for key, value in avg_ratings_dict.items():
    # unpacked the value into title and rating
    title, rating = value
    print(f"{key}\t{title}\t{rating}")
