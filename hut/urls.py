from django.conf.urls import url

from hut import views

urlpatterns = [
    url(r'huts', views.all_huts),
    url(r'add_hut', views.add_hut),
    url(r'hut/(?P<hutname>[A-Za-z0-9]+)', views.show_hut),
    url(r'update_hut/(?P<hutname>[A-Za-z0-9]+)', views.update_hut),
    url(r'huts/(?P<mountain>[A-Za-z]+)', views.huts_by_mountain),
    url(r'huts/(?P<mountain>[A-Za-z0-9]+)/(?P<hutname>[A-Za-z0-9]+)',
        views.hut_by_name),
    url(r'huts/(?P<mountain>[A-Za-z0-9]+)/?page=n&size=l', views.page_of_huts),
    # url(r'/hut/(?P<mountain>[A-Za-z0-9]+)?query', views.huts_by_parameters),
    url(r'^$', views.home),
]
