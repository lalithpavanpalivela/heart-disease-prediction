from django.contrib import admin
from django.urls import path
from prediction import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page where user inputs features
    path('predict/', views.predict, name='predict'),  # Prediction result page
]
