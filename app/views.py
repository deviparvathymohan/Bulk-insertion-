from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
# from rest_framework.generics import GenericAPIView
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
# from .serializers import BulkSerializer
from rest_framework import viewsets,views,permissions,authentication
# from drf_yasg import openapi
# from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from rest_framework import status
# from rest_framework.authtoken.views import obtain_auth_token
from .models import Article
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from django.views import View
from datetime import datetime
import io,csv
# 
class EmployeeUploadView(View):
    def get(self, request):
        template_name = 'user.html'
        return render(request, template_name)
    def post(self, request):
        user = request.user #get the current login user details
        paramFile = io.TextIOWrapper(request.FILES['employeefile'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        print(list_of_dict)
        objs = [
            Article(
                id=row['id'],
                title=row['title'],
                author=row['author'],
                email=row['email'],
            # date=row['date'],
            )
            for row in list_of_dict
        ]
        try:
            msg = Article.objects.bulk_create(objs)
            returnmsg = {"status_code": 200}
            # print(list_of_dict)
            print('imported successfully')
        except Exception as e:
            print('Error While Importing Data: ',e)
            returnmsg = {"status_code": 500}
        return JsonResponse(returnmsg)
        # def handle_files(f):
        #     list_of_dict = csv.DictReader(open('employeefile'))
        #     for row in reader:
        # id=row['id']
        # age=row['age']
        # height=row['height']
        # my_object = MyObject(id=id, age=age,height=height)
        # my_object.save()
        def delete(self,request,pk,*args,**kwargs):
            objs=self.get_object(pk)
            objs.delete()
            return Response(status=status.HTTP_200_OK) 
