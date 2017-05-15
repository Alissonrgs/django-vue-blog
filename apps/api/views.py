import django
from django.http import JsonResponse


def get_csrf_token(request):
    csrftoken = django.middleware.csrf.get_token(request)
    return JsonResponse({'csrftoken': csrftoken})
