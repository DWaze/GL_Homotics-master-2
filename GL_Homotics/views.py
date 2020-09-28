from django.shortcuts import render
from rest_framework import generics

#from GL_Homotics.models import Blogpost


def home(HttpRequest):
    return render(HttpRequest, "index.html")


#class capteurs(generics.RetrieveUpdateDestroyAPIView):
    #    lookup_field = 'pk'

    #def get_queryset(self):
#return Blogpost.objects.all()
