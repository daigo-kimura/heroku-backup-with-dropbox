#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import os
import dropbox
import conf


def res_cmd(cmd):
    return subprocess.Popen(
        cmd, stdout=subprocess.PIPE,
        shell=True).communicate()[0]


def dump(appname, dump_name):
    original_filepath = "latest.dump"
    dump_path = "./backups/{}.sql".format(dump_name).replace(" ", "-")

    if os.path.exists(dump_path):
        raise ValueError("{} already exists!".format(dump_path))

    # Capture
    print("Capturing backup ...")
    cmd = "heroku pg:backups:capture -a {}".format(appname)
    res = res_cmd(cmd)
    print(res)

    # Download a dump file
    print("Downloading the dump file ...")
    cmd = "heroku pg:backups:download -a {}".format(appname)
    res = res_cmd(cmd)
    print(res)

    # Rename the file
    print("Renaming the dump file ...")
    print("{} -> {}".format(original_filepath, dump_path))
    cmd = "mv {} {}".format(original_filepath, dump_path)
    res = res_cmd(cmd)
    print(res)


def get_shared_link(path):
    dbx = dropbox.Dropbox(conf.DROPBOX_TOKEN)
    return dbx.sharing_create_shared_link(path)
