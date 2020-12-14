
import os
import time
import pipes

DATETIME = time.strftime('%Y-%m-%d %H:%M:%S')

#host = "host1.miem.vmnet.top"
#port = "20005"
#username = "equipment_user"
#password = "massivePassw0rd28"
#db = "Equipment"


host = os.environ.get("NVR_MONGO_HOST")
port = os.environ.get("NVR_MONGO_PORT")
username = os.environ.get("NVR_MONGO_USERNAME")
password = os.environ.get("NVR_MONGO_PASSWORD")
db = os.environ.get("NVR_MONGO_DB")

print(host)
print("Starting backup of database" + db)

command = "mongodump"
command += " --host " + host
command += " --port " + port
command += " --username " + username
command += " --password " + password
command += " -db " + db

#command = "mongodump -d Equipment"
os.system(command)

gitaddcmd = "git add ."
os.system(gitaddcmd)

gitcommitcmd = "git commit -m 'backup for " + DATETIME + "'"
os.system(gitcommitcmd)

gitpushcmd = "git push origin master"
os.system(gitpushcmd)

print("Backup script completed")
