# Textutils-website
I have created this small textutils website for people who work on pdfs and docs using DJango.

So Alright, I have uploaded all the files namely urls.py, settings.py, views.py, views2_bs.py, index.html, analyze.html, index2(bs).html, analyze2(bs).html

Before you clone this repo, read this please, index.html and analyze.html are the basic html files in which bootstrap is not included for styling, whereas in index2(bs).html and analyze2(bs).html bootstrap is included for your ready reference. 

Step1: Create a django project using "django-admin startproject #name_of_your_project". Now locate these files in your computer (if your using PyCharm it must be in PycharmProject). When you'll locate into your project you'll see one folder (#name_of_your_project) and one file (manage.py).

Step2: Now in #name_of_your_project there will be 5 prebuilt python files namely __init__.py, asgi.py, settings.py, urls.py, wsgi.py. Now delete settings.py and urls.py.

Step3: Download/Clone this repo and you'll see urls.py, settings.py, views.py, views2_bs.py, index.html, analyze.html, index2(bs).html, analyze2(bs).html. Here, you copy/cut urls.py, settings.py, views.py, views2_bs.py and paste in #name_of_your_project folder (not where you can see manage.py but the folder which is above manage.py).

Step4: Now you'll need to create a new directory i.e templates (do not change this name unless you have edited settings.py with the same name you want). Now in this templates directory copy/cut and paste all the html files.

#name_of_your_project directory should look like this:

#name_of_your_project
  |
  |
  |
    templates
    #name_of_your_project
      |
      |
      |
        __init__.py
        asgi.py
        settings.py
        urls.py
        views.py
        views2_bs.py
        wsgi.py
    manage.py
