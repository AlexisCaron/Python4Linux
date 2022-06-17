#!/usr/bin/python3

#Import modules
import os, shutil, datetime, mysql.connector, time

#Create backup repo if not exists
if not os.path.exists('/home/backup'):
    os.makedirs('/home/backup')

#Connect to DB to check if database classicmodels exists
'''my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)

my_cursor = my_db.cursor()
my_cursor.execute("SHOW DATABASES")

for i in my_cursor:
    if 'classicmodels' not in my_cursor:
        print("La base de données est inexistante, veuillez contacter l'administrateur !")
'''

destination = "/home/backup/backup_database.sql"
os.system('mysqldump -u root -p classicmodels > ' + destination)

#Set date & time
date = datetime.datetime.today().isoformat()

#Compress file & Delete for space
shutil.make_archive('/home/backup/database_' + str(date), 'tar', '.', destination)
os.remove(destination)

#Delete backup if more than 3 days
liste_backup = os.listdir('/home/backup/')
date_now = time.time()
for i in liste_backup:
    date_cre = os.path.getctime('/home/backup/' + i)
    
    if (date_now - date_cre) > 260000:
        os.remove('/home/backup/' + i)
