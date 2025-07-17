from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties()
    data = [
        {
            'title': prop.title,
            'description': prop.description,
            'price': str(prop.price),
            'location': prop.location,
            'created_at': prop.created_at.isoformat()
        }
        for prop in properties
    ]
    return JsonResponse({'properties': data})