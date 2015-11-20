# Dependencies
import sys
import json
import warnings
import wikipedia
import string
import nltk
from stop_words import get_stop_words


def content( title_list, save_path ):
    """Obtain the content of a list of titles of wikipedia articles.
    Store as a list."""

    warnings.simplefilter("ignore")
    print "Cleaning documents"
    content_list = [ get_content( title_list[i], i+1 ) for i in range(len(title_list)) ]
    sys.stdout.write("\n")
    warnings.simplefilter("default")
    with open( save_path, 'w' ) as out_file:
        json.dump( content_list, out_file )

    return content_list


def get_content( title, i=1 ):
    """Obtain summary of a wikipedia title which has been cleaned for LDA"""

    # Print progress
    sys.stdout.write( "%d " %i )
    sys.stdout.flush()

    # Obtain content and clean document
    page_content = wikipedia.page( title )
    page_content = page_content.content
    page_content = clean_document( page_content )

    return page_content


def clean_document( raw_content ):
    """Tokenize, remove stop words and stem words in document"""

    # Lower case, remove apostrophes and hyphens
    document = ''.join( raw_content.split("\'") )
    document = ''.join( raw_content.split("-") )

    # Tokenize
    tokenizer = nltk.tokenize.RegexpTokenizer( r'\w+' )
    document = tokenizer.tokenize( raw_content )

    # Remove stop words
    en_stop_words = get_stop_words('en')
    document = [word for word in document if not( word in en_stop_words ) ]

    # Stem words
    stemmer = nltk.stem.porter.PorterStemmer()
    document = [ stemmer.stem( word ) for word in document ]

    return document
