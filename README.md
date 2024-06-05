
---
> Install Virtual Environment:
- pip install virtualenv
> Create a Virtual Environment:
- python -m virtualenv env
- python3.6 -m virtualenv env
> Run Virtual Environment on Windows:
- env\Scripts\Activate
> Run Virtual Environment on Linux:
- source env/bin/activate

> other way to install module:
- python.exe -m pip install -U xhtml2pdf

> Create Lib List (Should be inside Virtual ENV were it is running and all lib or app installed)
- pip freeze > requirements.txt

> Install (Run inside Virtual Env and locate the file)
- pip install -r requirements.txt


> Reinstall clear cache
- pip freeze > pip-freeze.txt
- pip install -r pip-freeze.txt --force-reinstall --no-cache-dir

---

> Migrate
- python manage.py makemigrations <APP>
- python manage.py migrate <APP>
- python manage.py migrate <APP> --database=digixlog
---




______________________API______________________



>to add new movie 


http://127.0.0.1:8000/movie_display_create_update

set headers:

Content-Type header as multipart/form-data


Set body:
{"movie_name":"TITANIC",
'image':   upload from your local system
}



>to update existing movie

http://127.0.0.1:8000/movie_display_create_update

set headers:

Content-Type header as multipart/form-data


Set body:

{
    "display_id":1,
    
    "movie_name":"TITANIC",
    'image':   upload from your local system,

}




