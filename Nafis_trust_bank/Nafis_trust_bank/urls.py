from django.contrib import admin
from django.urls import path, include
from core.views import HomeView
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('transaction/',include('transtactions.urls'))
]

