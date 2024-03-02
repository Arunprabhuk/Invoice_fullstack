from django.http import HttpResponse

def firstApi(req):
    html = "<html><body>My first api</body></html>"
    return HttpResponse(html)

def dynamicApi(req,name):
    return HttpResponse("my name is " +name+" >>>>")