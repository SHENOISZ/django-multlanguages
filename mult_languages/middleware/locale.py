__author__ = 'shenoisz'

from django.utils import translation
from django.conf import settings
from django.http import HttpResponseRedirect


class MultLanguageMiddleware( object ):

    def __init__( self, *args, **kwargs ):
        pass

    def process_view( self, request, view_func, view_args, view_kwargs ):

        if not request.GET.get('language'):
            try:
                domain = str( request.get_host( ) ).split(':')[0]
            except:
                domain = request.get_host( )
        else:
            domain = request.GET.get('language')
            dev = settings.HOSTS_DEV
            return HttpResponseRedirect(dev[0]+ '://'+domain + ':'+ dev[1] )

        langs = settings.MULTLAGUAGES
        request.languages = [ ]
        id = 1

        for gl in langs:
            if gl[1] == domain:
                request.session['django_language'] = gl[0]
                request.LANGUAGE_CODE = gl[0]
                request.id = id
                request.initials = gl[0]
                request.host = gl[1]
                translation.activate( gl[0] )

            id += 1
            request.languages.append( gl )

    # def process_request(self, request):
    #     pass
    # def process_response(self, request, response):
    #     return response

