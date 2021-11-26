# hostchecks
Http status checker

This script (hostchecks.py) will get the http status of any host/url contained in the input file.

Input file should be a .txt file with each entry on a seperate line. No empty lines in the file including at the start or end.

When run it will print the status of each host/url to the console, and will write the status to the output file.

#python hostchecks.py hosts.txt prechecks.txt

example output:
www.google.com Status is 200
www.cisco.com status is 200
www.facebook.com Status is 200
www.asdke.co.uk failed to get a status

if you run the checks again post change activity
#python hostchecks.py hosts.txt postchecks.txt

you can compare the pre and post check output files to see if the status has changed for any of the hosts/urls.
#python diff.py prechecks.txt postcheck.txt diffoutput.txt

example output:
www.google.com Status is 200 matches
www.cisco.com Status is 200 matches
www.facebook.com Status is 200 || changed to www.facebook.com Status is 403
www.asdke.co.uk failed to get a status matches


