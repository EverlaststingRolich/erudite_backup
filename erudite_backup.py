import os
import time
import pipes

DATETIME = time.strftime('%Y-%m-%d %H:%M:%S')

host = "host1.miem.vmnet.top"
port = "20005"
username = "equipment_user"
password = "massivePassw0rd28"
db = "Equipment"


print("Starting backup of database " + db)

command = "mongodump -d Equipment"
os.system(command)

gitaddcmd = "git add ."
os.system(gitaddcmd)

gitcommitcmd = "git commit -m 'backup for " + DATETIME + "'"
os.system(gitcommitcmd)

gitpushcmd = "git push origin master"
os.system(gitpushcmd)

print("Backup script completed")
