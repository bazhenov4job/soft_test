"""softlogic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from get_ids.views import PesonsIdView
from create_person.views import CreatePersonView
from get_object_info.views import ReturnInfoView
from delete_object.views import DeleteObjectView
from add_vector.views import AddVectorView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_ids/', PesonsIdView.as_view()),
    path('create_person/', CreatePersonView.as_view()),
    path('get_object_info/<int:pk>/', ReturnInfoView.as_view()),
    path('delete_object/<int:pk>/', DeleteObjectView.as_view()),
    path('add_vector/', AddVectorView.as_view()),

]
