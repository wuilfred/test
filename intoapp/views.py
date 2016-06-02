from django.views.generic import View
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
import requests, json
from requests.auth import HTTPBasicAuth
from django.http import JsonResponse, Http404


#@require_http_methods(["GET"])
def ajaxdata(request):
    if request.method == "POST":
        return JsonResponse({'name': 'Hello'})

class IndexView(View):

    def get(self, request, *args, **kwargs):
        url = 'http://www.intoparty.com/rest/events/'
        if request.method == "GET":
            # form = SubmitTicket(request.POST)
            # if form.is_valid():
            # url = form.cleaned_data['url']
            r = requests.get(url, auth=HTTPBasicAuth("wuilfred@gmail.com", "1qaz2wsx"), verify=True)
            json = r.json()
            #serializer = TicketSerializer(data=json)
            # if serializer.is_valid():
            #    ticket = serializer.save()
            #return render(request, 'ticket.html', {'ticket': json})

            return render(request, 'index.html', {'ticket': json})


class TicketEventSpecificAjax(View):

    def dispatch(self, *args, **kwargs):
        # do something
        return super(TicketEventSpecificAjax, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        url = 'http://www.intoparty.com/rest/events/'
        username = 'wuilfred@gmail.com'
        password = '1qaz2wsx'
        if request.method == 'GET':
            JsonData = request.GET['id']
            ticketData = requests.get(url+JsonData+'/', auth=HTTPBasicAuth(username, password), verify=True)
            resultTicket = ticketData.json()
            return JsonResponse({'data': resultTicket})

    def post(self, request, *args, **kwargs):
        #view = TicketEventSpecificAjax.as_view()
        if request.is_ajax:
            try:
                if request.method == 'POST':
                    return JsonResponse({"Hellow": "Word"}, mimetype="application/json")
            except KeyError:
                return HttpResponse('ERROR')
                JsonResponse(json.dumps({'id': '11010101'}), content_type="application/json")
        else:
            raise Http404


class TicketEventProductAjax(View):

    def __init__(self, *args, **kwargs):
        self.event_id = ''

    def get(self, request):

        try:
            self.event_id = request.GET['id']

            url = 'http://www.intoparty.com/rest/events/'+self.event_id+'/products/'
            username = 'wuilfred@gmail.com'
            password = '1qaz2wsx'
            if request.method == 'GET':
                JsonData =request.GET['id']
                ticketData = requests.get(url+JsonData+'/', auth=HTTPBasicAuth(username, password), verify=True)
                resultTicket = ticketData.json()
                return  JsonResponse({'product_data': resultTicket})
        except Exception as err:
                return JsonResponse({'error': err})

class TicketEventSpecificProductAjax(View):

    def __init__(self, *args, **kwargs):
        self.event_id = ''
        self.product_id = ''

    def get(self, request):

        try:
            self.event_id = request.GET['id']
            self.product_id = request.GET['']
            url = 'http://www.intoparty.com/rest/events/<event-id>/products/<product-id>/'+self.event_id+'/products/'
            username = 'wuilfred@gmail.com'
            password = '1qaz2wsx'
            if request.method == 'GET':
                JsonData =request.GET['id']
                ticketData = requests.get(url+JsonData+'/', auth=HTTPBasicAuth(username, password), verify=True)
                resultTicket = ticketData.json()
                return  JsonResponse({'product_data_specific': resultTicket})
        except Exception as err:
                return JsonResponse({'error': err})



class TicketEventGuestAjax(View):

    def __init__(self, *args, **kwargs):
        self.event_id = ''

    def get(self, request):

        try:
            self.event_id = request.GET['id']
            url = 'http://www.intoparty.com/rest/events/'+self.event_id+'/guests/'
            username = 'wuilfred@gmail.com'
            password = '1qaz2wsx'
            if request.method == 'GET':
                ticketData = requests.get(url, auth=HTTPBasicAuth(username, password), verify=True)
                resultTicket = [ticketData.json()[x]['user'] for x in range(len(ticketData.json()))]
                return  JsonResponse({'list_guest': ticketData.json(), 'user': resultTicket})
        except Exception as err:
                return JsonResponse({'error': err})


class TicketEventGuestSpecificAjax(View):

    def __init__(self, *args, **kwargs):
        self.event_id = ''
        self.product_id = ''

    def get(self, request):

        try:
            self.event_id = request.GET['id']
            self.product_id = request.GET['']
            url = 'http://www.intoparty.com/rest/events/<event-id>/guests/<guest-id>/'
            username = 'wuilfred@gmail.com'
            password = '1qaz2wsx'
            if request.method == 'GET':
                JsonData =request.GET['id']
                ticketData = requests.get(url+JsonData+'/', auth=HTTPBasicAuth(username, password), verify=True)
                resultTicket = ticketData.json()
                return  JsonResponse({'product_data_guest': resultTicket})
        except Exception as err:
                return JsonResponse({'error': err})


class TicketEventGuestProductAjax(View):

    def __init__(self, *args, **kwargs):
        self.event_id = ''
        self.guest_id = ''

    def get(self, request):

        try:
            self.event_id = request.GET['id']
            self.guest_id = request.GET['']
            url = 'http://www.intoparty.com/rest/events/'+self.event_id+'/guests/'+self.guest_id+'/products/'
            username = 'wuilfred@gmail.com'
            password = '1qaz2wsx'
            if request.method == 'GET':
                JsonData =request.GET['id']
                ticketData = requests.get(url+JsonData+'/', auth=HTTPBasicAuth(username, password), verify=True)
                resultTicket = ticketData.json()
                return  JsonResponse({'product_data_guest': resultTicket})
        except Exception as err:
                return JsonResponse({'error': err})