#!C:\Users\KSB\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
form=cgi.FieldStorage()
title=form['title'].value
description=form['description'].value

opened_file=open('data/'+title,'a')
opened_file.write(description)

print("Location:index.py?id="+title)
print()
