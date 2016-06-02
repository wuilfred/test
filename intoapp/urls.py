from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from .views import *

app_name = 'intoapp'

urlpatterns = [
    url(regex=r'^$', view=IndexView.as_view(), name='index'),
    url(r'^ticketEventSpecific/', TicketEventSpecificAjax.as_view(), name='AjaxTicketSpecific'),
    url(r'^ticketEventProduct/', TicketEventProductAjax.as_view(), name='AjaxTicketProduct'),
    url(r'^ticketSpecificProduct/', TicketEventSpecificProductAjax.as_view(), name=''),
    url(r'^ticketguestlist/', TicketEventGuestAjax.as_view(), name='ticketguestlist'),
    url(r'^ajaxdata/', views.ajaxdata, name='ajaxdata'),
    #url(r'^admin/guest/list$', 'guest.admin_views.list')
]