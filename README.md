# Django-muiltlanguages #

## Settings

#### Install middleware class

```
MIDDLEWARE_CLASSES = (
    'muiltlanguages.middleware.locale.MultLanguageMiddleware',
)
```

## Create variable MULTLAGUAGES

```
MULTLAGUAGES = (
    ('en', 'en.test.com'),
    ('es', 'es.test.com'),
    ('pt-BR', 'pt.test.com')
)
```

## Create variable HOSTS_DEV
#### Port 8000 or any other for localhost test and devs, default 80

HOSTS_DEV = ['http', '8000'] 

## Create yours locale for translations 
####Exemplo:

python manage.py makemessage -l en<br>
python manage.py makemessage -l es<br>
python manage.py makemessage -l pt_BR<br>

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

## license

Copyright (c) 2016 Marcelo Rodrigues

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



