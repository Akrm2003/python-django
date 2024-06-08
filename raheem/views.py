from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def my_endpoint(request):
    name = request.data.get('name')
    if not name:
     return Response({'error:' 'name btch'}, status=status.HTTP_400_BAD_REQUEST)

    data = {
		'message': f'hello, {name}!'
	}
    return Response(data)