# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('testdb/', views.testdb),
# ]
from django.urls import  path

from . import views

urlpatterns = [
    # path('testdb', views.testdb),

    path('entityAdd/',views.entityAdd),
    path('entityDel/', views.entityDel),
    path('entityMod/', views.entityMod),
    path('entityFind/', views.entityFind),
    path('patientlogin/', views.patientlogin),
    path('patientregister/', views.patientregister),
    path('doctorregister/', views.doctorregister),
    path('doctorlogin/', views.doctorlogin),
    path('chat/', views.chat),

    path('relAdd/', views.relAdd),
    path('relDel/', views.relDel),
    path('relMod/', views.relMod),

    path('showKG/', views.showKG),
    path('test/', views.test),

    path('entitySearch/', views.entitySearch),
    path('relSearch/', views.relSearch),

    # path('login/', views.login),
    # path('register/', views.register),

    path('showUser/', views.showUser),
    path('addUser/', views.addUser),
    path('delUser/', views.delUser),
    path('modUser/', views.modUser),

    path('showModel/', views.showModel),
    path('delModel/', views.delModel),
    path('addModel/', views.addModel),

    path('entityReasoning/',views.entityReasoning),
    path('resoningMod/',views.resoningMod),
    path('reasoningDel/',views.reasoningDel),



]