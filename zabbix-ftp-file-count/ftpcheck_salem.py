#!/usr/bin/env python
#encoding:utf8
#
# Zabbix agent checks file count on FTP server
# Place in /usr/lib/zabbix/externalscripts
# 

import os
import ftplib

ftpServer = os.environ.get('FTP_SALEM_SERVER')
ftpUsername = os.environ.get('FTP_SALEM_USERNAME')
ftpPassword = os.environ.get('FTP_SALEM_PASSWORD')
ftpDirectory = os.environ.get('FTP_SALEM_DIRECTORY')

# Open FTP server
ftp = ftplib.FTP(ftpServer)
ftp.login(ftpUsername, ftpPassword)
cwd = ftp.cwd(ftpDirectory)


count =  len(ftp.nlst())
    
ftp.quit()

print(count)