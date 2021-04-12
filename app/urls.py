from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from django.urls import path
from app import views
urlpatterns = [
    path('employee/', views.EmployeeUploadView.as_view(), name='employee'),
    # path('userDetails/<int:pk>/',views.userDetails.as_view(),name="userDetails"),
]