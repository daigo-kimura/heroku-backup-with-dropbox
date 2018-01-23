#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser

import conf
import utils


def main():
    appname = conf.APP_NAME

    desc = """[Options]
    Detailed options -h or --help"""

    parser = ArgumentParser(
        prog="heroku backup",
        description=desc,
        add_help=True,
    )

    parser.add_argument(
        "-f", "--file",
        help="output file",
        required=True,
    )

    args = parser.parse_args()

    utils.dump(appname, args.file)

    print("Finished")


if __name__ == "__main__":
    main()
