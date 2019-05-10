"""lb10Birthday.py - reformat exported birthday list for sacrament bulletin. 
                     Opens new file in Notepad to ease copy into Word.
     Parameters: filename (birthday list in raw format)
     Output: new_filename (same folder, same filename with new_ prepended)
    History:
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

# GLOBALS
filename = None    # Path object
list_month = None  # str ('May')


def check_arguments():
    """Exit app with error if filename not specified or doesn't exist.
       Modifies: filename (global, pathlib Path object)"""
    global filename

    parser = argparse.ArgumentParser(
        description="Formats birthdays for church bulletin.")
    parser.add_argument("filename", type=str, 
        help="birthday list exported from Ward PC")
    args = parser.parse_args()

    filename = Path(args.filename)  # check file exists
    if not filename.is_file():
        print(f"Error: File not found - {filename.absolute()}")
        exit(1)


def get_birthday_list() -> list:
    """open and format raw birthday list as a list of raw entries
    Input: None
    Output: birthdays_raw (list): 'day month\nlast_name first_name'
    globals used: filename
    """
    birthdays_raw = filename.read_text()
    return birthdays_raw.strip().split('\n\n\n')


def cleanup(entry: str) -> str:
    """Reformat a single birthday entry for the sacrament bulletin
    Input: (str) entry - imported format (day month\nlast_name first_name)
    Output: (str) entry - preferred export format (day - first_name last_name)
    globals modified: list_month (str)
    """
    global list_month
    
    bday, name = entry.split('\n')
    day, mon = bday.split(' ')
    last, rest = name.split(', ')
    
    if not list_month: 
        list_month = mon  # Update month name for formatted file header

    return f"{day} - {rest} {last}\n"


def save_formatted_birthday_list(birthdays: list) -> str:
    """Save formatted birthday list with header, then launch
    Input: None
    Output: list - birthdays in format 'day month\nlast_name first_name'
    globals used: filename, list_month
    """
    output_file = str(filename.absolute().parent) + '\\' \
                  + filename.stem + "_new" + filename.suffix
    
    with open(output_file, 'w') as f:
        count = len(birthdays)
        f.write(f"{count} Birthdays for {list_month}\n"
                f"Converted from {filename.absolute()}\n\n")
        for entry in birthdays:
            f.write(entry)

    print(f"Saved to {output_file}")
    return output_file


def main():
    """Run program"""
    check_arguments()
    birthdays = [cleanup(entry) for entry in get_birthday_list()]
    new_list = save_formatted_birthday_list(birthdays)
    subprocess.run("notepad.exe " + new_list)


if __name__ == "__main__":
    main()