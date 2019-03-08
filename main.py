#!/usr/bin/env python3
import argparse
from tasks import *
import files

if __name__ == '__main__':
    files.init()
    parse = argparse.ArgumentParser()
    parse.add_argument("-s", type=str, help="search task with key", required=False)
    parse.add_argument("-a", type=str, help="add a new task", required=False)
    parse.add_argument("-d", type=int, help="delete a task", required=False)
    parse.add_argument("-c", type=int, help="copy a task to clipboard", required=False)
    args = parse.parse_args()
    if args.s is not None:
        show_task(key=args.s)
    elif args.a is not None:
        add_task(args.a)
    elif args.d is not None:
        delete_task(args.d)
    elif args.c is not None:
        copy_task(args.c)
    else:
        show_task(key=None)
