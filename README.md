# README.md - 

**birthdays.py - reformat raw birthday list for church bulletin**

## USAGE (command line)

```python birthdays.py [filename]```

**INPUT**: the full path to the raw birthday list (see below), e.g. birthdays.txt 
* if no path specified, will use the current folder

**OUTPUT**: the same filename, with **_new** appended, e.g. birthdays_new.txt
* filename_new.txt will be saved to the source file folder
* Program ends by launching the _new file into the default text editor (e.g. Notepad)

## USE CASE

I'm sent a monthly text export of the congregation's birthdays for the current month,
to include in our weekly bulletins. 

Cleaning it up by hand is a pain. I could use text editor macros, but it's painless in Python.

The **raw input** looks like this. (end of line seen as '\n' by Python but it might show as whitespace in a text editor).

```
\n\n1 May\nLewis, Huey\n\n\n2 May\nClapton, Eric\n\n\n ... \n\n\n31 May\nWonder,
Stevie\n\n\n\n\n\n\n
```

The **output file** that can be pasted into the bulletin looks like this (no formatting)

```
3 Birthdays for May
Converted from C:\dev\py\birthdays\birthdays.txt

1 - Huey Lewis
2 - Eric Clapton
31 - Stevie Wonder
```
The number of names varies from month to month, between 50 and 100 birthdays.

## PURPOSE

What would normally take 5-10 minutes cleaning up manually occurs in seconds with this script. 

It's also a good place to practice and explore tips as I learn them (most recently argparse, pathlib) and refine a bit at a time (make it work, make it fast, make it right).

## MODULES

argparse - to accept arguments from the commandline 
subprocess - 
pathlib - for handling file object from command line
collections - for namedtuple (Entry: (day month last first))

## FUNCTIONS

### get_args
* Sets up the CLI parser ( description, input file argument)
* No arguments: shows Usage and exits cleanly (TODO: clean part)
* 1 argument: returns pathlib object, absolute path/filename
* Doesn't check if file is valid, just that input is a file
* filename.absolute() returns ```WindowsPath('c:/dev/py/birthdays/birthdays.txt')```
* filename.name returns just the filename ```'birthdays.txt')```
>
> Input: (None)
> 
> Output: pathlib.WindowsPath object (full path/filename) or exit with descriptive error text

### check_arguments
* Sets up the CLI parser ( description, input file argument)
* No arguments: shows Usage and exits cleanly (TODO: clean part)
* 1 argument: returns pathlib object, absolute path/filename
* Doesn't check if file is valid, just that input is a file
* filename.absolute() returns ```WindowsPath('c:/dev/py/birthdays/birthdays.txt')```
* filename.name returns just the filename ```'birthdays.txt')```
>
> Input: (None)
> 
> Output: pathlib.WindowsPath object (full path/filename) or exit with descriptive error text

### get_birthday_list
* reads full input file with filename.read_text()
* strips out leading and trailing whitespace
* removes whitespace ("\n\n\n") between records
* leaves whitespace ("\n") between fields within records
* exports a list of unformatted records ```"day month\nLast, First"```
>
> Input: filename (pathlib object)
> 
> Output: list object ([record1, record2, etc])

### cleanup
* retrieves a single raw record ```"day month\nLast, First"```
* splits the birthday ("day month") and the name ("Last, First")
* Splits the birthday into **day** and **month**
* Splits the name into **Last Name** and **First Name**
* feeds day, month, last, and first into Entry named tuple
* returns Entry object with named fields

> Input: entry (str: "day month\nLast_Name, First_name) ("1 Mar\nJones, Tom")
> 
> Output: (named tuple) Entry(day=day, month=mon, first=first, last=last)

## save_formatted_birthday_list
* takes the source filename (pathlib object) and birthdays (list object of Entry namedtuple)
* constructs the output filename from the 
> Input: filename (pathlib object), birthdays: list of namedtuples
> 
> Output: list object

main
> 
>
> Input: filename (pathlib object: full path/filename)
> 
> Output: list object
