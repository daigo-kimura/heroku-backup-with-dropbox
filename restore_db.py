#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from datetime import datetime

import utils
import conf


def main():
    appname = conf.APP_NAME
    backup_folder_path = conf.BACKUP_PATH

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
    print(args)

    # Backup before restore
    dump_name = datetime.now()
    utils.dump(appname, dump_name)

    # cmd = "heroku pg:backups:restore"
    backup_path = "{}{}".format(backup_folder_path, args.file)
    print("Target backup file: {}".format(backup_path))
    shared_link = utils.get_shared_link(backup_path).url.replace("dl=0", "dl=1")
    print("Backup file shared link: {}".format(shared_link))

    cmd = "heroku pg:backups:restore --app {} '{}' --confirm {}".format(
        appname, shared_link, appname)

    res = utils.res_cmd(cmd)
    print(res)

    print("Finished")


if __name__ == "__main__":
    main()
