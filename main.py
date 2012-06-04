#!/usr/bin/env python

# Python main function boilerplate, based on the original work:
# "Python main() functions" by Guido van van Rossum
# http://www.artima.com/weblogs/viewpost.jsp?thread=4829
#
# For code style guidelines see:
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

"""
<<Description of what the program does:
will be displayed by the -h/--help option.>>

Usage: <<usage-description>>
"""
import sys
import getopt

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ArgumentError(Error):
    """Problem with a supplied argument."""
    def __init__(self, msg):
        self.msg = msg

class Usage(Exception):
    """Display program usage."""
    def __init__(self, msg):
        self.msg = msg

def process_arg(arg):
    #handle arguments here
    raise ArgumentError("Not implemented.")

def main(argv=None):

    if argv is None: argv = sys.argv

    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
             raise Usage(msg)

        # process options
        for o, a in opts:
            if o in ("-h", "--help"):
                raise Usage(__doc__)

        # process arguments
        for arg in args:
            process_arg(arg)

        # start the real program here
        #

    # Error handling for the actual program.
    except Error, err:
        print err.msg

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
