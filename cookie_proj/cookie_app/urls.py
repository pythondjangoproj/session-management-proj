# from django.contrib import admin
from django.urls import path
from . import views
app_name='cookie_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.count_view, name='count_view'),
]
