# LDA-wiki
Scrape wikipedia for random articles and clean, tokenize and stem document for Latent Dirichlet Allocation.

    def fetch_random( n, dump_path ):

        """Obtain n random wikipedia documents, clean, tokenize and stem ready for LDA.
        JSON dump the content and article titles as files to dump_path.
        n is a positive integer, dump_path is a string which is a path to a directory"""
