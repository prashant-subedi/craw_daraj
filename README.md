# craw_daraj
Crawling using bs4 and requests. Use of Django to save data using models

#Using The Program
#Language : Python3
#Libraries Needed : bs4, lxml, django 

#Using Terminal GoTo the root of project and execute
#Make Migrations
pythone manage.py makemigrations

#Migrate
python3 manage.py migrate

#Create a super usering
python3 manage.py createsuperuser

#Crawl
python3 crawl_daraj.py
