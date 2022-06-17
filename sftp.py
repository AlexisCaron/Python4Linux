#!/usr/bin/python3

from paramiko import SSHClient
import os, time

#Connect to Srv-Web 
client = SSHClient()
client.load_system_host_keys()
client.load_host_keys('/home/user1/.ssh/known_hosts')

client.connect('10.125.27.62', username='user1', password='user1')

#Bring list of backup
sftp = client.open_sftp()
liste_backup = sftp.listdir('/home/backup')

#Store in /archives
for line in liste_backup:
    sftp.get('/home/backup/' + str(line), '/archives/' + str(line))
    

#Delete archive if more than 7 days
liste_archives = os.listdir('/archives/')
date_now = time.time()
for i in liste_archives:
    
    date_cre = os.path.getctime('/archives/' + i)
    if (date_now - date_cre) > 600000:
        os.remove('/archives/' + i)
    

    
