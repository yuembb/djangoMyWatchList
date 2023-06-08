from django.shortcuts import get_object_or_404
from appMy.models import *
from django.contrib.auth.decorators import login_required #* burda djangonun login yapılımı değilmi yapan yapısını çekiyoruz kontrol etmek için


#* ve bu kısımda yazılan def leri bütün yapımızda kullana biliyoruz yani burda ortak kullanılması gerekilen yapıları yazabiliriz 



def infoPage(request):
    if request.user.is_authenticated:
        context = {
            "userinfo": get_object_or_404(Profile, user =request.user),
        }
        return context
    else:
        return ""
            
        