"""
URL configuration for EducationaLoan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from bhanu.views import *

urlpatterns = [
    
    path('apply-educationalLoan',create_EducationLoan,name="createEducationloan"),
    path('loan-records/', loan_records, name='loan_records'),
    path('update-record/<int:id>/', update_record, name='update_record'),
    path('view-EducationLoan/<int:id>',viewEducationLoan,name='view-educationloan'),
    path('create-Doc',createDocuments,name="create-doc"),
    path('showAll-docs',document_list,name='showall-docs'),
    path('update-docs/<str:application_id>',updateDocument,name='update-doc'),
    path('view-documents/<str:application_id>',viewDocuments,name='view-doc'),
    path('Eduapplication-flow/<str:application_id>',applicationVerification,name='EduapplicationFlow'),
    path('EduUpdate-verification/<str:application_id>',update_verification,name="EduUpdate-verification"),
    path('EducustomerProfile/<str:application_id>',customerProfile,name="Educustomer-profile"),
    path('edubasicdetail/',edubasicdetails,name='edubasicdetail'),



]

from django.conf.urls.static import static
from django.conf import  settings



urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


