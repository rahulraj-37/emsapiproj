from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

#create an instance of the DefaultRouter class
router = DefaultRouter()

#register the mapping for url and views
#r for new raw string - to escape special characters
router.register(r'departments',views.DepartmentViewSet)
router.register(r'employees',views.EmployeeViewSet)
router.register(r'users',views.UserViewSet)

urlpatterns=[
path("signup/",views.SignupAPIView.as_view(), name="user-signup"),
path("login/",views.LoginAPIView.as_view(),name="user-login"),
  ]

#create a urlpatterns list from the router urls
urlpatterns=urlpatterns + router.urls
