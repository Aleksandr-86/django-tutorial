from django.http import HttpResponse


def index(request):
    return HttpResponse('Вы находитесь на странице с результатами опроса.')
