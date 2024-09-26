from django.http import HttpResponse

def index(request):
    return HttpResponse("Nhi's at the polls index.")
