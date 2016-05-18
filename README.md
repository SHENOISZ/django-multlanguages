# Django-muiltlanguages #

# Settings

# Install middleware class

MIDDLEWARE_CLASSES = (<br>
&nbsp;'muiltlanguages.middleware.locale.MultLanguageMiddleware',<br>
)<br>

# Create variable MULTLAGUAGES

MULTLAGUAGES = (<br>
&nbsp;&nbsp;&nbsp;('en', 'en.test.com'),<br>
&nbsp;&nbsp;&nbsp;('es', 'es.test.com'),<br>
&nbsp;&nbsp;&nbsp;('pt-BR', 'pt.test.com')<br>
)<br>

# Create variable HOSTS_DEV
# Port 8000 or any other for localhost test and devs, default 80

HOSTS_DEV = ['http', '8000'] 

# Create yours locale for translations 
Exemplo:

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

# Values in request

c = RequestContext(request, {<br>
&nbsp;&nbsp;&nbsp;'id': request.id,<br>
&nbsp;&nbsp;&nbsp;'host': request.host,<br>
&nbsp;&nbsp;&nbsp;'initials': request.initials,<br>
&nbsp;&nbsp;&nbsp;'languages': request.languages<br>
})<br>


# license

Copyright (c) 2016 Marcelo Rodrigues

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



