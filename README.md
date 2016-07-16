# Django-mult-languages #

## Install

```
pip install django-mult-languages
```

## Settings

```
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGE_CODE = 'en-us'
```

#### Install middleware class

```
MIDDLEWARE_CLASSES = (
    'mult_languages.middleware.locale.MultLanguageMiddleware',
)
```

## Create variable MULTLAGUAGES

```
MULTLAGUAGES = (
    ('en-us', 'www.test.com'),
    ('en-us', 'en.test.com'),
    ('es', 'es.test.com'),
    ('pt-BR', 'pt.test.com')
)
```

## Create variable HOSTS_DEV
#### Port 8000 or any other for localhost test and devs, default 80

HOSTS_DEV = ['http', '8000'] 

## Create their locale for translations 
####Exemplo:

python manage.py makemessages -l en-us<br>
python manage.py makemessages -l es<br>
python manage.py makemessages -l pt_BR<br>

configure the django.po<br>

run the command:

python manage.py compilemessages<br>

or<br>

python manage.py compilemessages -l en<br>
python manage.py compilemessages -l es<br>
python manage.py compilemessages -l pt_BR<br>

## Values in request

```
c = RequestContext(request, {
    'id': request.id,
    'host': request.host,
    'initials': request.initials,
    'languages': request.languages
})
```

## Template

```
<form action="/" method="get">
    <select name="language">
        {% for lang in languages %}
            <option   value="{{ lang.1 }}">{{ lang.0 }}</option>
        {% endfor %}<br>
    </select>
    <input type="submit" value="Send">
</form>
```


