from django.shortcuts import render
from .models import Communities
#def communities_list(req):
    #return render(req, 'communities/communities_list.html')


def communities_list(request):
    commun = Communities.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'commun': Communities})
