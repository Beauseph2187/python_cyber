#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-p",
    "--port",
    help="A port flag for scanning",
    type=int
)
parser.add_argument(
    "-n",
    "--name",
    help="Tell me a name!"
)
# this is a first mandatory arg for the program
# parser.add_argument("ip")


args = parser.parse_args()
if args.port:
    print(args.port)
else:
    print("using default options for port")

print(args.name)
# print(args.ip)