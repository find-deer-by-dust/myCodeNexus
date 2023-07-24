import os
ssh = os.popen("ssh 192.168.0.104").read()
print(ssh)

