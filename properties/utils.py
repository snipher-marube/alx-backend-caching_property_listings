from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try to get cached properties
    cached_properties = cache.get('all_properties')
    
    if cached_properties is not None:
        return cached_properties
    
    # If not in cache, fetch from database
    properties = Property.objects.all()
    
    # Cache the queryset for 1 hour (3600 seconds)
    cache.set('all_properties', properties, 3600)
    
    return properties