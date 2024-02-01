from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/deTextByEar/', include('deTextByEar.urls')),
    path('api/deGuessGame/', include('deGuessGame.urls')),
    path('api/deStorys/', include('deAudioStorys.urls')),
    path('api/deSpells/', include('deGrammar.urls')),
    path('api/enAudioStorys/', include('enAudioStorys.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

