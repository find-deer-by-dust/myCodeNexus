import time
import os
while True:
        ping = os.popen("ping 192.168.0.104")

        print('最短' in ping.read())
        time.sleep(10)