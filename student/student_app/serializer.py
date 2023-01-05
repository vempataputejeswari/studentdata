from rest_framework import  serializers
from .models import classtable,studenttable
class studenttableSerializer(serializers.ModelSerializer):
    class Meta:
        model = studenttable
        fields = '__all__'