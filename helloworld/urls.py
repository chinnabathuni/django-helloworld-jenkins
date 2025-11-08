from webapp.views import index
urlpatterns = [
    path('', index, name='home'),
]
