#! /usr/bin/env python3

# curl https://translate.googleapis.com/translate_a/single\?client\=gtx\&sl\=en\&tl\=es\&dt\=t\&q\=Hello

import argparse
import requests
import time
from pathlib import Path
import sys


def line_translation(source_lang, target_lang, line_to_translated):
    parms = {"client": "gtx", "sl": source_lang,
             "tl": target_lang, "dt": "t", "q": line_to_translated}

    response = requests.get(
        'https://translate.googleapis.com/translate_a/single', params=parms)
    response.raise_for_status()
    line_translated = response.json()
    text_translated = line_translated[0][0][0]
    time.sleep(1)
    return text_translated


def main():
    parser = argparse.ArgumentParser(
        description="This program help to translate a srt file.")
    parser.add_argument("-f", "--file", type=argparse.FileType('r'),
                        help="The srt file to translate")
    parser.add_argument("-l", "--lenguages", type=str,
                        help="The two lenguages of the language we want to translate from")
    args = parser.parse_args()

    in_file = args.file
    in_file_name = in_file.name
    (in_lang, out_lang) = args.lenguages.split(':')

    cwd = Path.cwd()
    file_data = cwd / f"{in_file_name}"
    out_file = file_data.with_suffix(".es.srt")
    file_translated = open(f"{out_file}", "w")

    while True:
        line_1 = in_file.readline().strip()
        if line_1 == "":
            break

        file_translated.write(f"{line_1}\n")
        line_2 = in_file.readline().strip()
        file_translated.write(f"{line_2}\n")

        while True:
            line_tex = in_file.readline()
            if line_tex == "":
                break
            line_tex_strip = line_tex.strip()
            if line_tex_strip == "":
                file_translated.write("\n")
                break

            file_translated.write(line_translation(
                in_lang, out_lang, line_tex_strip) + "\n")

    file_translated.close()


if __name__ == "__main__":
    sys.exit(main())
