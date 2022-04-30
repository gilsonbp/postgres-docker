from time import gmtime, strftime
import subprocess
import os

database_list = [
    "notify_api",
]
USER = "gilson"
PASS = "nenco"
BACKUP_DIR = "/root/Dropbox/backups/"
dumper = """ pg_dump --no-owner -U %s -Z 9 -f %s -F c %s  """
os.putenv("PGPASSWORD", PASS)
for database_name in database_list:
    print(
        strftime("%Y-%m-%d-%H-%M-%S", gmtime())
        + ": dump started for %s" % database_name
    )
    time = str(strftime("%Y-%m-%d-%H-%M"))
    file_name = database_name + "_" + time + ".sql.pgdump"
    command = dumper % (USER, BACKUP_DIR + file_name, database_name)
    subprocess.call(command, shell=True)
    print(strftime("%Y-%m-%d-%H-%M-%S", gmtime()) + ": finished")
