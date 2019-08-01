from django.contrib import admin
from django.urls import path, include
import add_words

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', include('add_words.urls')),
    path('', include('search.urls'))
]
