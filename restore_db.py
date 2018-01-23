#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from datetime import datetime
import re

import utils
import conf


def main():
    appname = conf.APP_NAME
    backup_folder_path = "{}{}".format(conf.DROPBOX_PATH, conf.BACKUP_PATH)
    backup_folder_path = re.sub(r'[^/]+/?$', '', backup_folder_path)

    desc = """[Options]
    Detailed options -h or --help"""

    parser = ArgumentParser(
        prog="heroku restore",
        description=desc,
        add_help=True,
    )

    parser.add_argument(
        "-f", "--file",
        help="target dump file",
        required=True,
    )

    args = parser.parse_args()

    # Backup before restore
    utils.dump(appname, datetime.now())

    backup_file_path = "{}{}".format(backup_folder_path, args.file)[len(conf.DROPBOX_PATH):]
    print("Target backup file: {}".format(backup_file_path))
    shared_link = utils.get_shared_link(backup_file_path).url.replace("dl=0", "dl=1")
    print("Backup file shared link: {}".format(shared_link))

    cmd = "heroku pg:backups:restore --app {} '{}' --confirm {}".format(
        appname, shared_link, appname)

    res = utils.res_cmd(cmd)
    print(res)

    print("Finished")


if __name__ == "__main__":
    main()
