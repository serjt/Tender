from django.http.response import JsonResponse
from django.shortcuts import render
from post import find_data


def check_black_list(request):
    fio = request.POST.get('fio')
    day = request.POST.get('day')
    month = request.POST.get('month')
    year = request.POST.get('year')

    return JsonResponse(dict(result=find_data(fio, day, month, year)))