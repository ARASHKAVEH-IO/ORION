from django.http import HttpResponse , JsonResponse


def http_test(request):
    return HttpResponse('<h1>PROJECT-ORION</h1>')

def json_test(request):
    return JsonResponse({'name':'ORION'})