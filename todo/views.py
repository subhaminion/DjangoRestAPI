from rest_framework.response import Response
from rest_framework.views import APIView
from todo.serializers import TodoSerializers
from .models import TodoElements

class TodoView(APIView):
	def get(self, request):
		todos = TodoElements.objects.all()
		serializers = TodoSerializers(todos, many=True)
		return Response(serializers.data)