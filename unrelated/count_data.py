import argparse
from functools import reduce
import gzip
import json
from pathlib import Path

from joblib import delayed, Parallel

def examine_file(f):
    """
    Helper function. Examines the data in the given file and returns
    some useful statistics about it.
    """
    fname = f.name

    # Grab the filesize.
    filesize = Path(f).stat().st_size

    # Go through the file, counting the tweets.
    failed_tweets = 0
    n_tweets = 0
    with gzip.open(f, "rt") as fp:
        contents = fp.read().split("\n")
        for tweet_text in contents:
            try:
                tweet = json.loads(tweet_text)
            except Exception as e:
                print(e)
                print(f"Problematic file: {fname}")
                failed_tweets += 1
            else:
                n_tweets += 1

    # Return everything.
    #return [fname, n_tweets, failed_tweets, filesize]
    return [n_tweets, failed_tweets, filesize]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Twitter Download Validation',
        epilog = 'lol moar tweetz', add_help = 'How to use',
        prog = 'python count_data.py -i <inputdir>')
    parser.add_argument('-i', '--inputdir', required = True,
        help = 'Path directory containing the json gzipped data.')

    args = vars(parser.parse_args())
    path = Path(args['inputdir'])

    # Get the list of data files.
    file_list = list(path.glob("*.json.gz"))
    print(f"Found {len(file_list)} files.")

    # Go through each one and assemble some statistics.
    out = Parallel(n_jobs = -1)(
        delayed(examine_file)(f)
        for f in file_list)

    results = list(reduce(lambda x, y: [x[0] + y[0], x[1] + y[1], x[2] + y[2]], out))
    print(f"Tweets found: {results[0]}")
    print(f"Total bytes: {results[2]}")
    print(f"Failed tweets: {results[1]}")