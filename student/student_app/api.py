from rest_framework import generics
from rest_framework.response import Response
from .serializer import studenttableSerializer
from .models import studenttable
class studenttableCreateApi(generics.CreateAPIView):
    queryset = studenttable.objects.all()
    serializer_class = studenttableSerializer

class studenttableApi(generics.ListAPIView):
    queryset = studenttable.objects.all()
    serializer_class = studenttableSerializer

class DeleteApi(generics.DestroyAPIView):

    queryset = studenttable.objects.all()
    serializer_class = studenttableSerializer