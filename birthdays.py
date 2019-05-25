"""Birthdays.py - reformat exported birthday list for sacrament bulletin. 
                     Opens new file in Notepad to ease copy into Word.
     Parameters: filename (birthday list in raw format)
     Output: new_filename (same folder, same filename with new_ prepended)
    History:
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
import argparse
import subprocess
from pathlib import Path
from collections import namedtuple

# NAMED TUPLES
Entry = namedtuple('Entry', "day month last first")


def check_arguments():
    """Exit app with error if filename not specified or doesn't exist.
       Input: (str) full or partial path/filename from CLI
       returns: (Path object) filename
    """
    parser = argparse.ArgumentParser(
        description="Formats birthdays for church bulletin.")
    parser.add_argument("file", type=str, 
        help="birthday list exported from Ward PC")
    args = parser.parse_args()

    filename = Path(args.file)
    if not filename.is_file():
        print(f"Error: File not found - {filename.absolute()}")
        exit(1)
    return filename


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
    last, first = name.split(', ')
    
    return Entry(day=day, month=mon, first=first, last=last)


def save_formatted_birthday_list(filename, birthdays: list) -> str:
    """Save formatted birthday list, with header
       Input: (Path) filename, (list) birthdays
       returns: (str) filename of report
    """
    report_file = str(filename.absolute().parent) + '\\' \
                  + filename.stem + "_new" + filename.suffix
    
    with open(report_file, 'w') as f:
        list_month = birthdays[0].month
        count = len(birthdays)

        f.write(f"{count} Birthdays for {list_month}\n"
                f"Converted from {filename.absolute()}\n\n")
        for entry in birthdays:
            f.write(f"{entry.day} - {entry.first} {entry.last}\n")
    
    print(f"Saved to {report_file}")
    return report_file


def main():
    """Run program: generate formatted list and open in text editor
    """
    filename = check_arguments()
    birthdays_raw = get_birthday_list(filename)
    birthdays = [cleanup(entry) for entry in birthdays_raw]
    bd_report = save_formatted_birthday_list(filename, birthdays)
    subprocess.run("notepad.exe " + bd_report)


if __name__ == "__main__":
    main()