from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from todo.serializers import TodoSerializers
from .models import TodoElements

class TodoView(APIView):
	def get(self, request):
		todos = TodoElements.objects.all()
		serializers = TodoSerializers(todos, many=True)
		return Response(serializers.data)

	def put(self, request):
		serializers = TodoSerializers(data=request.POST)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data)
		return Response(serializers.data, status = status.HTTP_400_BAD_REQUEST)