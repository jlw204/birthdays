"""Birthdays.py - reformat exported birthday list for sacrament bulletin. 
                     Opens new file in Notepad to ease copy into Word.
     Parameters: filename (birthday list in raw format)
     Output: new_filename (same folder, same filename with new_ prepended)

    HISTORY
    =======
    2026-03-15 - created helper functions, added comments, cleaned code
    2019-05-25 - refactored to remove global variables
                cleanup() now returns namedtuple, includes month
                list_month pulled from first entry in list
                renamed variables
                updated docstrings

    2019-05-09 - Refactored. 
               Can specify input file on command line or be prompted. 
               Some file error checking.
               Comprehension func processes list into bulletin format.
               Added header to formatted list: record count, orig. filename.
               Added Docstrings.
               Added arg parsing and File Exists check.
               Updated header with absolute filename path

"""
# MODULES
from collections import namedtuple # maybe overkill but adds flexibility
from pathlib import Path # for os-neutral filename/path handling
import argparse # to retrieve input filename from command line
import subprocess # to open text editor with formatted list

# NAMED TUPLES
Entry = namedtuple('Entry', "day month last first")

def get_args() -> argparse.Namespace:
    """Exit app with error if filename not specified or doesn't exist.
       Input: (str) full or partial path/filename from CLI
       returns: (Path object) filename
    """
    parser = argparse.ArgumentParser(
        description="Generates formatted birthday lists for church bulletin.")
    parser.add_argument("input_file", type=str, 
        help="birthday list (raw text) exported from Church Office app")
    return parser.parse_args()


def get_input_file(args: argparse.Namespace) -> Path:
    try:
        filename = Path(args.input_file)
        if not filename.is_file():
            print(f"Error: File not found - {filename.absolute()}")
            exit(1)
        return filename
    except Exception as e:
        print(f"Error: {e}")
        exit(1) 


def set_output_file(filename):
    """Set output filename to same folder, same name with _new appended
       Input: (Path object) filename - original filename
       returns: (Path object) filename - new filename"""
    return filename.parent / (filename.stem + "_new" + filename.suffix)


def get_birthday_list(filename) -> list:
    """open and format raw birthday list as a list of raw entries
       Input: (Path object) filename
       returns: (list) birthdays_raw (['day month\nlast_name first_name',])
    """
    birthdays_raw = filename.read_text()
    return birthdays_raw.strip().split('\n\n\n')


def cleanup(entry: str):
    """Reformat a single birthday entry for the sacrament bulletin
       Input: (str) entry - ('day month\nlast_name first_name')
       returns: (namedtuple) Entry(day, month, first, last)
    """
    bday, name = entry.split('\n')
    day, mon = bday.split(' ')
    last_name, first_name = name.split(', ')
    
    return Entry(day=day, month=mon, first=first_name, last=last_name)


def save_formatted_birthday_list(report_file: Path, birthdays: list) -> None:
    """Save formatted birthday list, with header
       Input: (Path) report_file, (list) birthdays
       returns: (none)
    """
   
    with open(report_file, 'w') as f:
        list_month = birthdays[0].month # same month for all; use first entry
        count = len(birthdays) # number of entries for header

        # print the header (filename, list count, month)
        f.write(f"Output File: \n— {report_file.absolute()}\n\n")
        f.write(f"Birthdays for {list_month}: {count}\n\n")

        # print the formatted list, one name/birthday per line
        for entry in birthdays:
            f.write(f"{entry.day} - {entry.first} {entry.last}\n")

def show_formatteed_list(report_file: Path) -> None:
    """Open formatted birthday list in Notepad
       Input: (Path) report_file
       returns: (none)
    """
    subprocess.run("notepad.exe " + report_file.absolute().name)

def main():
    """
    Generate formatted birthday list and open new file in text editor
    """
    # get the filename from the command line arguments
    args = get_args()
    # Get input filename (pathlib object) of unformatted birthday data
    input_file = get_input_file(args) 
    # Define output file (pathlib object) for formatted birthday list
    output_file = set_output_file(input_file)
    # First cleanup pass: generates list of birthdays (raw text)
    birthdays_raw = get_birthday_list(input_file)
    # Second cleanup pass: generates list of Entry (named tuple)
    # list is not sorted, but is in the same (sorted) order as original file
    birthday_list = [cleanup(entry) for entry in birthdays_raw]

    # Save formatted list to file, open in Notepad
    save_formatted_birthday_list(output_file, birthday_list)
    show_formatteed_list(output_file)


if __name__ == "__main__":
    main()