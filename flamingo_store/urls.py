from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import flamingo_store.views as views

urlpatterns = [
    path('', views.wellcome, name='wellcome'),
    path('tickets/', views.TicketsListViews.as_view(), name='home'),
    path('t/', views.index, name='test')
]

urlpatterns += staticfiles_urlpatterns()
