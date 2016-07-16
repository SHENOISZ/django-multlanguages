from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

class Home( View ):

    def get( self, request, *args, **kwargs ):

        context = {
            'id': request.id,
            'host': request.host,
            'initials': request.initials,
            'languages': request.languages
        }

        return render(
        	request, 
        	'index.html',
        	context
        )