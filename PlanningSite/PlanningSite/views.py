from django.http import HttpResponse, Http404
import numpy as np

#the first parameter to any function MUST be 'request'
def hello(request):
    return HttpResponse("Hello wordd")

def randomGenerator(request, offset):
    try:
        multiplier = int(offset)
    except ValueError:
        raise Http404()
    assert False
    return HttpResponse(str(multiplier * np.random.random()))
