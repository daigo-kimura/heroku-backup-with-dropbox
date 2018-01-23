# Heroku Backup with Dropbox
Use your dropbox storage to backup and restore a database on your heroku application

# Installation
1. Get your dropbox app key
2. Set your dropbox home directory to `DROPBOX_PATH`
3. Set a directory path for dump file storage
4. Install packages according to  `requirement.txt`

# Usage
## Backup
 `python dump_db.py -f FILENAME`
## Restore
 `python restore_db.py -f FILENAME`
