from django.http import HttpResponse

def home(request):
    return HttpResponse('Главная страница')
def data_view(request):
    return HttpResponse("страница с данными")

def test_view(request):
    return HttpResponse("тестовая страница")