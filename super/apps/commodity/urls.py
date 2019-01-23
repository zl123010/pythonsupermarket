from django.conf.urls import url

from commodity.views import IndexView, DetailView, CategoryView

urlpatterns = [
    url(r'^index$', IndexView.as_view(), name='主页'),
    url(r'^detail$', DetailView.as_view(), name='详情'),
    url(r'^category$', CategoryView.as_view(), name='超市'),

]
