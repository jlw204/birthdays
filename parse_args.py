import argparse

def return_what() -> argparse.Namespace:
    """"
        Return the commandline arguments as a Namespace object
        Input: none
        returns: (Namespace) args - with attributes filename, silent, debug
    """
    parser=argparse.ArgumentParser(
      description = "argument parser")
    parser.add_argument("filename", type=str, help="a filename that exists")
    parser.add_argument("-s", "--silent", action="store_true", help="suppress output")
    parser.add_argument("-d", "--debug", action="store_true", help="print debug info")
    return parser.parse_args()


def return_flag_state(flag: bool) -> str:
    """
        Return a string indicating whether a flag is ON or OFF
        Input: (bool) flag
        returns: (str) "ON" if flag is True, "OFF" if flag is False
    """ 
    return "ON" if flag else "OFF"


def main():
    """
        Main function to demonstrate argument parsing and flag state
        Input: none
    """
    args = return_what()
    print(args)
    print(type(args))
    print(args.filename)
    print(f"Silent mode is {return_flag_state(args.silent)}")
    print(f"Debug mode is {return_flag_state(args.debug)}")


if __name__ == '__main__':
    main()
