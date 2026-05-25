from django.contrib import admin
from django.urls import path, include
from tracker import views as tracker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', tracker_views.dashboard, name='dashboard'),
    path('cycle/', tracker_views.cycle, name='cycle'),
    path('medicine/', tracker_views.medicine, name='medicine'),
    path('appointments/', tracker_views.appointments, name='appointments'),
    path('diet/', tracker_views.diet, name='diet'),
    path('lifestyle/', tracker_views.lifestyle, name='lifestyle'),
    path('insights/', tracker_views.insights, name='insights'),
    path('chatbot/', include('chatbot.urls')),
    path('', tracker_views.dashboard, name='home'),
]
