from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'cleanapp.views.html_message', name='html_message'),
    url(r'^short-message$', 'cleanapp.views.short_message', name='short_message'),
    url(r'^average-message$', 'cleanapp.views.average_message', name='average_message'),
    url(r'^long-message$', 'cleanapp.views.long_message', name='long_message'),
    url(r'^json-message$', 'cleanapp.views.json_message', name='json_message'),
    url(r'^slow-request$', 'cleanapp.views.slow_request', name='slow_request'),
)
