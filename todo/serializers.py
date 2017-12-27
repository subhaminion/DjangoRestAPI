from rest_framework import serializers
from todo.models import TodoElements

class TodoSerializers(serializers.ModelSerializer):
	class Meta:
		model = TodoElements
		fields = 'id', 'todo_text', 'done'