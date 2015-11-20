import sys
import os
import scrape

def fetch_random( n, dump_path ):
    """Obtain n random wikipedia documents, clean, tokenize and stem ready for LDA.
    JSON dump the content and article titles as files to dump_path.
    n is a positive integer, dump_path is a string which is a path to a directory"""

    # Check inputs
    if ( dump_path[-1] != "/" ):
        dump_path = dump_path + "/"
    os.path.isdir( dump_path )
    is_pos_int( n )
    # Obtain random article titles, dump
    filepath = dump_path + "title"
    title_list = scrape.titles.random( n, filepath )
    # Obtain content, clean and dump
    filepath = dump_path + "content"
    content_list = scrape.clean.content( title_list, filepath )

    return content_list

def is_pos_int( n ):
    if ( not( isinstance( n, int ) ) ):
        ValueError( "Number of documents must be positive integer" )
    if ( n < 0 ):
        ValueError( "Number of documents must be positive integer" )
