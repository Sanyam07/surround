import os
import argparse

from ..linter import DataLinter

def is_valid_file(parser, x):
    if not os.path.exists(x):
        parser.error('Unable to locate the file!')
        return False

    if not os.path.isfile(x):
        parser.error('The path specified must be to a file!')
        return False

    splitext = os.path.splitext(x)
    if ".data" not in splitext[0] or splitext[1] != ".zip":
        parser.erorr("The file specified must be a data container (.data.zip)")
        return False

    return x

def is_valid_check_id(parser, x):
    try:
        x = int(x)
    except Exception:
        parser.error('The check id value must be a number!')
        return False

    if x < 1 or x > len(DataLinter().stages):
        parser.error("There is no linter stage with that ID!")
        return False

    return x

def get_data_lint_parser():
    parser = argparse.ArgumentParser(description='Check the validity of a data container', add_help=False)

    parser.add_argument("container_path", help="Path to the container to perform checks on", type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-l", "--list", action='store_true', help="List the checks the linter will perform")
    parser.add_argument("-c", "--check-id", help="Specify a single check to perform (get id from --list)", type=lambda x: is_valid_check_id(parser, x))

    return parser

def execute_data_lint_tool(parser, args):
    linter = DataLinter()

    if args.list:
        linter.list_stages()
    elif args.check_id:
        linter.lint(args.container_path, verbose=True, check_id=args.check_id)
    else:
        linter.lint(args.container_path, verbose=True)

def main():
    parser = get_data_lint_parser()
    args = parser.parse_args()

    execute_data_lint_tool(parser, args)

if __name__ == "__main__":
    main()
