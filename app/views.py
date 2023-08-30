from django.shortcuts import render

# Create your views here.
from .models import Product
from .seralizer import Productserializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView

class List_product(GenericAPIView,ListModelMixin):
    queryset=Product.objects.all()
    serializer_class=Productserializer
    def get(self,request):
        return self.list(request)
    
class Create_product(GenericAPIView,CreateModelMixin):
    queryset=Product.objects.all()
    serializer_class=Productserializer
    def post(self,request):
        return self.create(request)
