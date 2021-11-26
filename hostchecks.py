import urllib3
import urllib3
import time
import sys
from colours import colour

http = urllib3.PoolManager(timeout=3.0)

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as l:
        lines = f.readlines()

        for each in lines:
                try:
                        each = each.rstrip("\n")
                        time.sleep(1)
                        resp = http.request('GET', each)
                        print(each + " Status is " + colour.green(str(resp.status)))
                        status = (each + " Status is " + str(resp.status))
                        l.writelines(status)
                        l.writelines('\n')
                except:
                        print(each + colour.red(" failed to get a status"))
                        status = (each + " failed to get a status")
                        l.writelines(status)
                        l.writelines('\n')
