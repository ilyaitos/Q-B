
from django.urls import path
from app.views import index, loging, logout_do, sss_ys, register, now_1, now_2, now_3, knop, now_4, now_5, now_6



urlpatterns = [
    path('main_page', index),
    path("ap", loging),
    path("zzz", logout_do),
    path("sss", sss_ys),
    path('reg', register),
    path("", now_1),
    path("nach", now_2),
    path("o_nass", now_3),
    path("aj",  knop),
    path("voto",  now_4),
    path("yclyg",  now_5),
    path("contact",  now_6),

]

