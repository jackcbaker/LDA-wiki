# Dependencies
import sys
import json
import warnings
import wikipedia


def random( n, save_path ):
    """Generate a list of n random document titles from wikipedia,
    provided they are not disambiguation pages.
    Save to given path."""

    warnings.simplefilter("ignore")
    print "Fetching articles"
    title_list = [ get_title( i+1 ) for i in range(n) ]
    warnings.simplefilter("default")
    sys.stdout.write("\n")
    with open( save_path, 'w' ) as out_file:
        json.dump( title_list, out_file )

    return title_list


def get_title( progress_count ):
    """Obtain title of a random wikipedia article, checking it's not a disambiguation."""

    # Print progress
    sys.stdout.write( "%d " %progress_count )
    sys.stdout.flush()

    # Get title, try to load page. Pick another if there's a disambiguation error.
    while True:
        try:
            title = wikipedia.random()
            wikipedia.page( title )
            break
        except ( wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError ):
            title = wikipedia.random()

    return title
