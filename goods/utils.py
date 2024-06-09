from django.db.models import Q
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [keyword for keyword in query.split() if len(keyword) > 2]
    
    q_objects = Q()
    
    for keyword in keywords:
        q_objects |=  Q(name__icontains=keyword)
        q_objects |= Q(description__icontains=keyword)

    return Products.objects.filter(q_objects)
