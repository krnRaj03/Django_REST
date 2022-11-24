# from django.shortcuts import render
# from .models import *
# from django.http import JsonResponse


# # Create your views here.
# def movie_list(request):
#   movs=Movie.objects.all()
#   data={'movs':list(movs.values())}
#   # print(movs.values())
#   return JsonResponse(data)

# def movie_detail(request,pk):
#   movs1=Movie.objects.get(pk=pk)
#   data={
#     'name':movs1.name,
#     'desc':movs1.description,
#     'active':movs1.active,
#   }
#   return JsonResponse(data)