# birthdays
reformat raw birthday list for church bulletin

NEED:
I'm sent a text export of the birthdays for our congregation once a month,
to include in our weekly bulletins. Cleaning it up by hand is a pain, but it's
relatively painless in Python.

The raw input looks like this.

\n\n1 May\nLewis, Huey\n\n\n2 May\nClapton, Eric\n\n\n...\n\n\n31 May\nWonder,
 Stevie\n\n\n\n\n\n\n

The format for the bulletin is more like this:

1 - Huey Lewis
2 - Eric Clapton
...
31 - Stevie Wonder

The number of names varies from month to month, between 50 and 100 birthdays.

FUNCTIONALITY:

This script reduces a 5-10 minute REPL session to a 30 second operation (download file, 
launch command line, run script, copy/paste results). It's also a good place to practice
and explore tips as I learn them (most recently argparse, pathlib) and refine a bit at a time
(make it work, make it fast, make it right).
