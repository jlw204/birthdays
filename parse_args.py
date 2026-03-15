import argparse
def return_what():
    parser=argparse.ArgumentParser(
      description = "argument parser")
    parser.add_argument("filename", type=str, help="a filename that exists")
    return parser.parse_args()

def main():
    args = return_what()
    print(args)
    print(type(args))
    print(args.filename)
    # assuming type is correct: Namespace(filename='filename.txt')


if __name__ == '__main__':
    main()
