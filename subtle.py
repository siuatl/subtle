#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    description="This program help to translate a srt file.")
parser.add_argument("-f", "--file", type=str, help="The srt file to translate")
parser.add_argument("-l", "--lenguages", type=str,
                    help="The two lenguages of the language we want to translate from")
args = parser.parse_args()
