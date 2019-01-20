from django.conf.urls import url

from commodity.views import CommodityView

urlpatterns = [
    url(r'^index$', CommodityView.as_view(), name='主页')

]
