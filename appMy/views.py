from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import authenticate, login , logout  #*giriş yap çıkış yap ve girişli mi diye kontrol et
from django.contrib.auth.models import User #* burdaki yaptığımız işlem ise otomatik olarak biz projeyiş oluşturduğumuzda database te oluşan user sayfasını dahil etmemizi yazıyor normalde biz kendi model imizi yazıyoruz ama bu hazır olduğu için böyle çekmemiz lazım
from django.contrib import messages #* mesaj uyarılarını kullanmak için burda çekiyoruz
from django.contrib.auth.decorators import login_required #* burda djangonun login yapılımı değilmi yapan yapısını çekiyoruz kontrol etmek için




# Create your views here.

        # "profile":Profile.objects.get(user = request.user),
        #* profil resmini göstediğim sayfada kullanıcıdan çıkış yaptığım zaman hata veriyor site 

def index(request ):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        cards = Card.objects.filter(user=request.user)
    else:
        cards = Card.objects.all()
   

    category = Category.objects.all()


    context = {
        "cards":cards,
        "category":category,
        "profile":profile,

    }

    return render (request , 'index.html' , context)

def categoryPage(request , ptitle , group=4):
    
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    

    category = Category.objects.all()
    
    if ptitle == "all" and request.user.is_authenticated:
        cards = Card.objects.filter(user=request.user)
    else:
        cards = Card.objects.filter(category__title=ptitle , user=request.user)

    context = {
        "cards":cards,
        "category":category,
        "profile":profile,
        "category_active":ptitle,
        "group":group,
    }

    return render (request , 'category.html' , context)


def detailPage(request , pid):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)


    card_get = Card.objects.get(id=pid)

    context = {
    "profile":profile,
    "card_get":card_get,

    }

    return render (request , 'detail.html' , context)

@login_required(login_url="/login/")
def cardAddPage(request):
    profile = None
    
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    # *  burda modelleri çekiyoruz
    categorys = Category.objects.all()
    dramatype = Dramatype.objects.all()
    gametype = Gametype.objects.all()
    types = Type.objects.all()
    context = {
    "profile":profile,
    "categorys":categorys,
    "gametype":gametype,
    "dramatype":dramatype,
    "types":types,
    }
    
    # * burda gelen bilgiler post mu diye kontrol sağlayıp bilgileri çekiyoruz
    
    if request.method == "POST":
        title = request.POST.get("title")
        category_name = request.POST.get("category")
        type = request.POST.get("type")
        image = request.FILES.get("image")
        text = request.POST.get("text")
        
        
        #* burda boş bırakmayı engelliyoruz 
        if not (title.strip(" ")=="" or text.strip(" ") =="" or category_name.strip(" ") =="" or type.strip(" ") =="" ):
            if image is not None:
                
                category = Category.objects.get(title=category_name)

                type_obj = Type.objects.get(title=type)
                # *  burda kayıt işlemini sağlıyopruz databasse e atıyoruz
                card = Card(user = request.user , title = title , category = category , type = type_obj , image = image , text = text , author = request.user)
                # * ve save ediyoruz

                card.save()
                return redirect("card-add")
            else:
                messages.warning(request,"Boş bırakılan yerler var doldurunuz!!")
                
        else:
            messages.warning(request,"Boş bırakılan yerler var doldurunuz!!")

    
    
    

    return render (request , 'card-add.html' , context)
@login_required(login_url="/login/")
def cardDeletePage(request, id): # * silme yapma fonksiyonu 


    
    # if request.method == "POST":  #* burda gelen bilgiler post ilemi geliyor diye kontrol yapıyoruz
        
    #     submit = request.POST.get("submit")
    #     print("======================================")

    #     if submit == "cardDelete":
    #         print("-------------------------------")

    # if submit == "cardDelete":
    #     print("-------------------------------")
        
    card = Card.objects.get(id = id) #* burda id si eşit olanı ürünü direk siliyoruz bitti gitti
    card.delete()

    return redirect("index")


#! User Start

#! Register start
def registerUser(request):
    context = {

    }
    

    if request.method == "POST":  #* burda gelen bilgiler post ilemi geliyor diye kontrol yapıyoruz
        # * bu kısımda html den gelen verileri çekiyoruz
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        # * bu kısımda html den gelen verileri çekiyoruz/


        # * bu kısımda kontrol yapmak için check yapıyoruz
        email_check = True
        username_check = True
        upp = False
        num = False
        passwordlen = False
       # * bu kısımda kontrol yapmak için check yapıyoruz/

        for i in password1:
            if i.isdecimal():
                num = True
            if i == i.upper() and not i.isdecimal():
                upp = True
            if len(password1) >=6:
                passwordlen = True


        # * bu kısımda boş bırakılmasını engelliyoruz strip(" ") != "" dersek fname boş değilse analamına geliyor burda onun kontrolunu yapıyoruz
        if fname.strip(" ") !="" and lname.strip(" ") !="" and username.strip(" ") !="" and email.strip(" ") !="" and password1.strip(" ") !="" and password2.strip(" ") !="":
            # * burda ise şifreleri eşitliyoruz ve yukarıda kontrolun yaptığımız koşulların doğruluğunu kontrol ediyoruz
            if password1==password2 and upp and num and passwordlen:
                # * burda ise User model'i içerisinde username adında bir başkası varmı diye kontrol sağlıyoruz eğer varsa bu kullanıcı adı alınmıştır diye hata veriyoruz yani burda username alınabilirmi diye kontrol sağlıyoruz
                if not User.objects.filter(username=username).exists():
                    # * burda ise User model'i içerisinde mail adında bir başkası varmı diye kontrol sağlıyoruz eğer varsa bu mail adı alınmıştır diye hata veriyoruz yani burda mail alınabilirmi diye kontrol sağlıyoruz
                    if not User.objects.filter(email=email).exists():
                        
                        # * burda ise User Model inin içerisinde kullanıcı oluşturuyoruz ve ordaki gelen yerlere first_name(data base ten geliyor ona fname atıyoruz html den aldığımız) bu şekilde verileri eşitleyip kayıt yapıyoruz ardından login sayfasına yönlendiriyoruz
                        user = User.objects.create_user(first_name = fname , last_name = lname , username = username , email = email , password = password1)
                        user.save()
                        
                        profile = Profile(user=user , password= password1)
                        profile.save()
                        
                        return redirect("loginUser")
                    
                    
                    
                    else: # * burda mail adresi başka bir kullanıcıya ait diye hata basıyoruz
                        messages.warning(request, 'bu email adresi başka bir kullanıcıya ait')
                        email_check = False
                else:  # * burda username adresi başka bir kullanıcıya ait diye hata basıyoruz
                    messages.warning(request, 'bu username başka bir kullanıcıya ait')
                    username_check = False
            # *  bu kısımda şifrede uymayan hataların mesajını basıyor
            if num == False:
                messages.warning(request, 'şifrede en az 1 harf olmalı')
            if upp == False:
                messages.warning(request, 'şifrede en az 1 büyük olmalı')
            if passwordlen == False:
                messages.warning(request, 'şifrede en az 6 karakter olmalı')
            if password1 != password2:
                messages.warning(request, 'şifreler birbiriyle eşleşmiyor yeniden deneyin')
        else: # *  burda sayfada boş bırakılan yerler olduğunu belirtiyoruz
            messages.warning(request,"boş bırakılan yerler var")
        if username_check == False:    # *  burda ise hata mesajı adlığında doldurduğu yerleri geli getiriyoruz çünkü her seferinde yazmak can sıkıcı
            context.update({
            "fname": fname,
            "lname": lname,
            "email": email,
        })
        elif email_check == False: # *  burda ise hata mesajı adlığında doldurduğu yerleri geli getiriyoruz çünkü her seferinde yazmak can sıkıcı
            context.update({
            "fname": fname,
            "lname": lname,
            "username": username,
        })
        else: # *  burda ise hata mesajı adlığında doldurduğu yerleri geli getiriyoruz çünkü her seferinde yazmak can sıkıcı
            context.update({
                "fname": fname,
                "lname": lname,
                "email": email,
                "username": username,
            })    



    return render (request , 'user/register.html' , context)
#! Register End

#! Login
def loginUser(request):

     #* burda gelen bilgiler post ilemi geliyor diye kontrol yapıyoruz
    if request.method == "POST":
        # * bu kısımda html den gelen verileri çekiyoruz
        username = request.POST.get("username")
        password = request.POST.get("password")
        # * bu kısımda html den gelen verileri çekiyoruz

        user = authenticate(username=username , password=password) #* burda database de böyle bir kullanıcı varmı diye kontrol ediyor
        useractive = User.objects.filter(username=username) #* burda username i username olanla filtreledikten sonra useracteive atıyoruz
        
        if not (username.strip(" ")=="" or password.strip(" ")==""):  #* burda boş bırakmayı engelliyoruz 
        
            if useractive.exists(): #* böyle bir kullanıcı varmı diye kontrol ediyor ardından
                if useractive.get().is_active ==True: #* burda kullanıcının aktif durumunun kontrol ediyoruz get ile çekiyoruz çünkü filter ile çekerssek burda hata veriyor get ile direk çekersekte var olmayan bir kullanıcı girerse hata alırız o yüzden varlığını sorguluyoruz 
                    if user is not None: #* burida ise gelen user verisinin içerisi dolu mu boşmu diye kontrol sağlanıyor eğer şifre ve username eşleşmişse bir değer dönüyor ve bu değer doğrultusunda login yaptırıyoruz
                        login(request , user)
                        return redirect('index')
                    else:
                        messages.warning(request, "kullanıcı adı veya şifreniz yanlış")
                        return redirect("loginUser")

                else:
                    messages.warning(request , "email i aktif et")
                    return redirect("loginUser")
            else:
                messages.warning(request, "kullanıcı adı veya şifreniz yanlış")
                return redirect("loginUser")
        else:
            messages.warning(request , "Boş Bırakılan Yerler Var !")
            return redirect("loginUser")
    
    context = {


    }

    return render (request , 'user/login.html' , context)
#! Login End

#!LogOut
def logoutUser(request):

    if request.user.is_authenticated: # * sadece bu yazıyı alıyorsun ve çıkış yap tamamdır girili olan kullanıcıyhı sistemden çıkarıyor
        logout(request)

    return redirect ('index')

# !Profil
@login_required(login_url="/login/") #* girişli olymayan kullanıcı bu sayfaya gitmeye çalışırsa onu login sayfasına yönlendiriyor
def profileUser(request):
   profile = Profile.objects.get(user = request.user) #* user ı girili user olan profili profile değişkenine atıyoruz
   user = User.objects.get(username=request.user) #* username ı girili user olan User'ı  userr değişkenine atıyoruz
   
   
   if request.method == "POST": #* gelen method Post mu diye kontrol ediyoruz
      submit = request.POST.get("submit") #* burda gelen name i submit olan buton u alıyoruz 

      if submit == "passwordChange": #* name i submit olan value su passwordChange olan buton un bilgisini çekiyoruz
         password = request.POST.get("password") #*eski şifre
         password1 = request.POST.get("password1") #*yeni şifre
         password2 = request.POST.get("password2") #*yeni şifre tekrar

         if user.check_password(password): #* eski şifre
            #* PASWORD START
            upp = False
            numm = False
            for i in password1:
               print(i)
               if i == i.upper() and not i.isdecimal():
                  upp = True
               if i.isdecimal():
                  numm = True

            if not upp:
               messages.warning(request, "Şifrede bir büyük harf olmalı!!")
            if not numm:
               messages.warning(request, "Şifrede bir numara olmalı!!")
            if not len(password1) >= 6:
               messages.warning(request, "Şifrede en az 6 karakter olmalı!!")
            #* PASWORD END
            if password1 == password2 and upp and numm and len(password1)>=6: #* yeni şifreler
               user.set_password(password1)
               user.save()
               #* login(request, user)
               return redirect("loginUser")
            else:
               messages.warning(request, "Şifreler aynı değil!!")
         else:
            messages.warning(request, "Şifre Yanlış!!")
               
         
         
      elif submit == "profilChange": #* buton value si profile change olan buton a basıldıysa ordaki bilgileri çekiyoruz
         fullname = request.POST.get("fullname") 
         username = request.POST.get("username")
         job = request.POST.get("job")
         email = request.POST.get("email")
         address = request.POST.get("address")
         tel = request.POST.get("tel")
         image = request.FILES.get("image")

        #* burda profil de açtığımız yerlere çektiğimiz yerlere atıyoruz
         profile.job = job
         profile.address = address
         profile.tel = tel
         if image is not None: #* burda ise image boş değilse 
            profile.image = image # * profil image e seçtiği image i atıyoruz
         profile.save() #* profili save ediyoruz
         
         #* NAME START
         listname = fullname.split(" ") # * burda fullname den gelen veriyi boşluklara göre bölüyoruz
         fname = "" #* boş fname oluşturuyoruz
         lname = "" #* boş lname oluşturuyoruz
         if len(listname) != 1:  #* burda listname 1 e eşit değil ise 
            lname = listname.pop() #* son elemanı çıkarıyoruz ve lname e atıyoruz
         for i in listname: #*burda ise listname in elemanlarını harf harf döyüruz
            if i != "": #* i boşluğa eşit değilse 
               fname += i + " " #* araya boşluk atıyoruz bu forda kısaca
               
         user.first_name = fname # * user model inin firs name ine girdiği fname bilgisini kaydediyoruz
         user.last_name = lname # * user model inin last name ine girdiği lname bilgisini kaydediyoruz
         #* NAME END
         
         if not User.objects.filter(username = username).exists(): # * eğer böyle bir kullanıcı yoksa kaydet 
            user.username = username
            
         if not User.objects.filter(email = email).exists(): #* eğer böyle bir email yoksa kaydet
            user.email = email
         user.save()
      
      return redirect("profileUser")
   
   context = {
       "profile": profile,
   }


   return render(request, "user/profile.html",context)
#!LogOut End



#! User End







