from rest_framework.decorators import api_view
from rest_framework.response import Response
from app1.models import *
from app1.api.serializers import *
from rest_framework import status

@api_view(['GET','POST'])
def movie_list(request):
  if request.method=='GET':
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)
  
  if request.method=='POST':
    serializer=MovieSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer._errors)

@api_view(['GET','PUT','DELETE'])
def movie_details(request,pk):
  if request.method=='GET':
    try:
      movies1=Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
      #displaying Custom message with Error code 
      return Response({'Error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer=MovieSerializer(movies1)
    return Response(serializer.data)

  if request.method=='PUT':
    movies1=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movies1,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer._errors)

  if request.method=='DELETE':
    movies1=Movie.objects.get(pk=pk)
    movies1.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  