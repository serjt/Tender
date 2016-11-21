from django.http.response import JsonResponse
from django.shortcuts import render
from post import find_data


def check_black_list(request):
    fio = request.GET.get('fio')
    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')

    return JsonResponse(dict(result=find_data(fio, day, month, year)))