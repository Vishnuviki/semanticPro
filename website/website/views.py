from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from .models import SPARQL_Model

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def search(request):
    bindings = ""

    print('SUCCESS')
    if request.method == 'POST':
        attractions = request.POST['attractions']
        transport = request.POST['transport']
        fare = request.POST['fare']
        entertainment = request.POST['entertainment']
        room = request.POST['room']

        # query_res = SPARQL_Model().getAttraction();
        # results = query_res['results']
        # bindings = results['bindings']
        if (attractions != "none" and transport == "none" and
                fare == "none" and entertainment == "none" and room == "none"):
            bindings = search_by_attraction(attractions)
        if (attractions != "none" and transport == "none" and
                fare != "none" and entertainment == "none" and room == "none"):
            bindings = search_by_attr_fare(attractions, fare)
        if (attractions != "none" and transport != "none" and
                fare == "none" and entertainment == "none" and room == "none"):
            bindings = search_by_att_and_transport(attractions, transport)
        if (attractions != "none" and transport != "none" and
                fare != "none" and entertainment == "none" and room == "none"):
            bindings = search_by_att_trans_fare(attractions, transport, fare)
        if (attractions != "none" and transport != "none" and
                fare != "none" and entertainment != "none" and room == "none"):
            bindings = search_by_att_trans_fare_enter(attractions, transport, fare, entertainment)
        if (attractions != "none" and transport != "none" and
                fare != "none" and entertainment != "none" and room != "none"):
            bindings = search_by_att_trans_fare_enter_room(attractions, transport, fare, entertainment, room)
        if (attractions != "none" and transport != "none" and
                fare != "none" and entertainment == "none" and room != "none"):
            bindings = search_by_att_trans_fare_room(attractions, transport, fare, room)
    return HttpResponse(json.dumps(bindings))


def search_by_attraction(attractions):
    query_res = SPARQL_Model().get_by_attraction(attractions)
    results = query_res['results']
    bindings = results['bindings']
    return bindings;

def search_by_att_and_transport(attraction, transport):
    query_res = SPARQL_Model().get_by_att_and_transport(attraction, transport)
    results = query_res['results']
    bindings = results['bindings']
    return bindings;

def search_by_att_trans_fare(attraction, transport, fare):
    query_res = SPARQL_Model().get_by_att_tran_fare(attraction, transport, fare)
    results = query_res['results']
    bindings = results['bindings']
    return bindings;

def search_by_att_trans_fare_enter(attraction, transport, fare, entertains):
    query_res = SPARQL_Model().get_by_att_tran_fare_enter(attraction, transport, fare, entertains)
    results = query_res['results']
    bindings = results['bindings']
    return bindings;

def search_by_att_trans_fare_enter_room(attraction, transport, fare, entertains, room):
    query_res = SPARQL_Model().get_by_att_tran_fare_enter_room(attraction, transport, fare, entertains, room)
    results = query_res['results']
    bindings = results['bindings']
    return bindings;

def search_by_att_trans_fare_room(attraction, transport, fare, room):
    query_res = SPARQL_Model().get_by_att_tran_fare_room(attraction, transport, fare, room)
    results = query_res['results']
    bindings = results['bindings']
    return bindings;

def search_by_attr_fare(attraction, fare):
    query_res = SPARQL_Model().get_by_att_fare(attraction, fare)
    results = query_res['results']
    bindings = results['bindings']
    return bindings;



