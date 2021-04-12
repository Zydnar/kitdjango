from django.conf.urls import patterns

urlpatterns = patterns('lck.django.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
