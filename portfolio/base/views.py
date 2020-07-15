from django.shortcuts import render
from django.http import JsonResponse
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests,json,ast
from .variables import ghub_username,l_username,Name,image


def error_500_view(request):
    return render(request,'500.html')

def error_404_view(request,exception):
    return render(request,'404.html')

def home(request):
    base = dict.fromkeys(['name','html_url','description'])
    base_list = []
    realdict = dict.fromkeys(['name','html_url','description'])

    custom_url = 'https://api.github.com/users/'+ghub_username+'/repos'
    response = requests.get(custom_url)#'https://api.github.com/users/gadeRaghav/repos')
    totalcontent = response.json()
    for content in totalcontent:
        base.update({'name' : content['name']})
        base.update({'html_url' : content['html_url']})
        base.update({'description': content['description']})
        realdict = ast.literal_eval(json.dumps(base))
        copy = realdict.copy()
        base_list.append(copy)


    return render(request ,'base/home.html',{
        'ghublist' : base_list,
        'l_username':l_username,
        'ghub_username':ghub_username,
        'Name':Name,
        'image':image
    })




