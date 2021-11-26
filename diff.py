import urllib3
import time
import sys
from colours import colour

http = urllib3.PoolManager(timeout=3.0)

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'r') as ff, open(sys.argv[3], 'w') as l:
        lines = f.readlines()
        linestwo = ff.readlines()
        print("This is variable lines " + str(lines))
        print("This is variable linestwo " + str(linestwo))
        count = 0
        for each in linestwo:
                try:
                        linestwo[count] = each.rstrip("\n")
                        count += 1
                except:
                        print(each + colour.red(" Error"))
                        count += 1
        countlines = 0
        for each in lines:
                try:
                        each = each.rstrip("\n")
                        if each in linestwo:
                                print(each + colour.green(" matches"))
                        else:
                                print(each + colour.red(" || changed to " + linestwo[countlines]))
                                status = (each + " || changed to " + linestwo[countlines])
                                l.writelines(status)
                                l.writelines('\n')
                        countlines += 1
                except:
                        print(each + colour.red(" ERROR"))
                        status = (each + " ERROR")
                        l.writelines(status)
                        l.writelines('\n')
                        countlines += 1
