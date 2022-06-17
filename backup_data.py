#!/usr/bin/python3

#Import modules
import os, shutil, datetime, time

#Create backup repo if not exists
if not os.path.exists('/home/backup'):
    os.makedirs('/home/backup')


#Copy to Backup
source=('/var/www/basic_website/')
destination=('/home/backup/basic_website/')
shutil.copytree(source, destination)

#Set date & time
date = datetime.datetime.today().isoformat()

#Compress repositery & Delete for space
shutil.make_archive('/home/backup/website_' + str(date), 'tar', '.', destination)
shutil.rmtree(destination)


#Delete backup if more than 3 days
liste_backup = os.listdir('/home/backup/')
date_now = time.time()
for i in liste_backup:
    date_cre = os.path.getctime('/home/backup/' + i)
    
    if (date_now - date_cre) > 260000:
        os.remove('/home/backup/' + i)


