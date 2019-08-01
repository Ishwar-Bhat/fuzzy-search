from django.contrib import admin
from django.urls import path, include
import add_words

urlpatterns = [
    path('', include('search.urls')),
    path('admin/', admin.site.urls),
    path('add/', include('add_words.urls')),
    path('search', include('api.urls'))
]
