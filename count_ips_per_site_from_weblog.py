#!/usr/bin/python
import re

file1="/var/log/httpd/access_log"
fh1 = open(file1,"rb")
ips_sites = []
for line in fh1.readlines():
	sObj = re.search( r'(.*) - - (.*) (.*.html) (.*)', line, re.M|re.I)
	if sObj:
		ips_sites.append((sObj.group(1), sObj.group(3)))

u_ips_sites = set(ips_sites)
for visit in u_ips_sites:
	print "{:12} visited the site: {:15} {:5d} timess".format(visit[0],visit[1],ips_sites.count(visit))
