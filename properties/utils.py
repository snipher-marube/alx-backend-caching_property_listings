from django.core.cache import cache
from django_redis import get_redis_connection
import logging
from .models import Property

logger = logging.getLogger(__name__)

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

def get_redis_cache_metrics():
    """
    Retrieves and analyzes Redis cache hit/miss metrics.
    Returns a dictionary with hits, misses, and hit ratio.
    """
    try:
        # Get Redis connection
        redis_conn = get_redis_connection("default")
        
        # Get Redis INFO command output
        redis_info = redis_conn.info()
        
        # Extract cache stats
        hits = redis_info.get('keyspace_hits', 0)
        misses = redis_info.get('keyspace_misses', 0)
        
        # Calculate hit ratio (handle division by zero)
        total = hits + misses
        hit_ratio = hits / total if total > 0 else 0
        
        metrics = {
            'hits': hits,
            'misses': misses,
            'hit_ratio': round(hit_ratio, 4),
            'total_operations': total
        }
        
        # Log the metrics
        logger.info(
            f"Redis cache metrics - Hits: {hits}, Misses: {misses}, "
            f"Hit Ratio: {hit_ratio:.2%}, Total: {total}"
        )
        
        return metrics
    
    except Exception as e:
        logger.error(f"Error getting Redis cache metrics: {str(e)}")
        return {
            'hits': 0,
            'misses': 0,
            'hit_ratio': 0,
            'total_operations': 0,
            'error': str(e)
        }