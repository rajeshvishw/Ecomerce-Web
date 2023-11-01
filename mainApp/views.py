from django.shortcuts import render,HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



from .models import *
def home(Request):
    data = Product.objects.all()
    data = data[::-1]
    data = data[0:10]
    brand = Brand.objects.all()
    subcategory = Subcategory.objects.all()
    return render(Request,"index.html",{'data':data,'brand':brand,'subcategory':subcategory})

def checkout(Request):
    return render(Request,"checkout.html")

def contact(Request):
    return render(Request,"contact.html")

def shop(Request,mc,sc,br):
    if(mc=="All" and sc=="All" and br=="All"):
        data = Product.objects.all()
    elif(mc!="All" and sc=="All" and br=="All"):
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc))
    elif(mc=="All" and sc!="All" and br=="All"):
        data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc))
    elif(mc=="All" and sc=="All" and br!="All"):
        data = Product.objects.filter(brand=Brand.objects.get(name=br))
    elif(mc!="All" and sc!="All" and br=="All"):
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc))
    elif(mc!="All" and sc=="All" and br!="All"):
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br))
    elif(mc=="All" and sc!="All" and br!="All"):
        data = Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc))
    else:
        data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc))
    count = len(data)
    data = data[::-1]
    maincategory = Maincategory.objects.all()
    subcategory = Subcategory.objects.all()
    brand = Brand.objects.all()
    return render(Request,"shop.html",{'data':data,'maincategory':maincategory,'subcategory':subcategory,'brand':brand,'mc':mc,'sc':sc,'br':br,'count':count})

def priceFilter(Request,mc,sc,br):
    if(Request.method=="POST"):
        min = Request.POST.get("min")
        max = Request.POST.get("max")
        if(mc=="All" and sc=="All" and br=="All"):
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max)
        elif(mc!="All" and sc=="All" and br=="All"):
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,maincategory=Maincategory.objects.get(name=mc))
        elif(mc=="All" and sc!="All" and br=="All"):
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,subcategory=Subcategory.objects.get(name=sc))
        elif(mc=="All" and sc=="All" and br!="All"):
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,brand=Brand.objects.get(name=br))
        elif(mc!="All" and sc!="All" and br=="All"):
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc))
        elif(mc!="All" and sc=="All" and br!="All"):
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br))
        elif(mc=="All" and sc!="All" and br!="All"):
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc))
        else:
            data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max,maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc))
        # data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max)
        count = len(data)
        data = data[::-1]
        maincategory = Maincategory.objects.all()
        subcategory = Subcategory.objects.all()
        brand = Brand.objects.all()
        return render(Request,"shop.html",{'data':data,'maincategory':maincategory,'subcategory':subcategory,'brand':brand,'mc':mc,'sc':sc,'br':br,'count':count})
    else:
        return HttpResponseRedirect("/shop/All/All/All")

def sortFilter(Request,mc,sc,br):
    if(Request.method=="POST"):
        sort = Request.POST.get("sort")
        if(sort=="Newest"):
            sort="id"
        elif(sort=="LTOH"):
            sort="-finalprice"
        else:
            sort="finalprice"
        if(mc=="All" and sc=="All" and br=="All"):
            data = Product.objects.all().order_by(sort)
        elif(mc!="All" and sc=="All" and br=="All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by(sort)
        elif(mc=="All" and sc!="All" and br=="All"):
            data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by(sort)
        elif(mc=="All" and sc=="All" and br!="All"):
            data = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by(sort)
        elif(mc!="All" and sc!="All" and br=="All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by(sort)
        elif(mc!="All" and sc=="All" and br!="All"):
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by(sort)
        elif(mc=="All" and sc!="All" and br!="All"):
            data = Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by(sort)
        else:
            data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by(sort)
        # data = Product.objects.filter(finalprice__gte=min,finalprice__lte=max)
        count = len(data)
        data = data[::-1]
        maincategory = Maincategory.objects.all()
        subcategory = Subcategory.objects.all()
        brand = Brand.objects.all()
        return render(Request,"shop.html",{'data':data,'maincategory':maincategory,'subcategory':subcategory,'brand':brand,'mc':mc,'sc':sc,'br':br,'count':count})
    else:
        return HttpResponseRedirect("/shop/All/All/All")

def searchPage(Request):
    if(Request.method=="POST"):
        search = Request.POST.get("search")
        data = Product.objects.filter(Q(name__icontains=search)|Q(color__icontains=search)|Q(size__icontains=search)|Q(description__icontains=search))
        maincategory = Maincategory.objects.all()
        subcategory = Subcategory.objects.all()
        brand = Brand.objects.all()
        count = len(data)
        return render(Request,"shop.html",{'data':data,'maincategory':maincategory,'subcategory':subcategory,'brand':brand,'mc':'All','sc':'All','br':'All','count':count})
    else:
        return HttpResponseRedirect("/shop/All/All/All")

def singleProduct(Request,num):
    data = Product.objects.get(id=num)
    return render(Request,"single-product.html",{'data':data})


def loginPage(Request):
    if(Request.method=='POST'):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(Request,user)
            if(user.is_superuser):
                return HttpResponseRedirect("/admin")
            else:
                return HttpResponseRedirect("/profile")
        else:
            messages.error(Request,"Invalid Username or Password!!!!")
    return render(Request,"login.html")

def signupPage(Request):
    if(Request.method=="POST"):
        name = Request.POST.get("name")
        username = Request.POST.get("username")
        email = Request.POST.get("email")
        phone = Request.POST.get("phone")
        password = Request.POST.get("password")
        cpassword = Request.POST.get("cpassword")
        if(password==cpassword):
            try:
                user = User(username=username)
                user.set_password(password)
                user.save()
                buyer = Buyer()
                buyer.name = name
                buyer.username = username
                buyer.email = email
                buyer.phone = phone
                buyer.password = password
                buyer.save()
                return HttpResponseRedirect("/login")
            except:
                messages.error(Request,"User Name Already Exist!!!")                
        else:
            messages.error(Request,"Password and Confirm Password Doesn't Matched!!!")
    return render(Request,"signup.html")

def logoutPage(Request):
    logout(Request)
    return HttpResponseRedirect("/login/")

@login_required(login_url="/login/")
def profilePage(Request):
    user = User.objects.get(username=Request.user.username)
    if(user.is_superuser):
        return HttpResponseRedirect("/admin/")
    else:
        buyer = Buyer.objects.get(username=Request.user.username)
    return render(Request,"profile.html",{'data':buyer})


@login_required(login_url="/login/")
def updateProfilePage(Request):
    user = User.objects.get(username=Request.user.username)
    if(user.is_superuser):
        return HttpResponseRedirect("/admin/")
    else:
        buyer = Buyer.objects.get(username=Request.user.username)
        if(Request.method=="POST"):
            buyer.name = Request.POST.get("name")
            buyer.email = Request.POST.get("email")
            buyer.phone = Request.POST.get("phone")
            buyer.addressline1 = Request.POST.get("addressline1")
            buyer.addressline2 = Request.POST.get("addressline2")
            buyer.addressline3 = Request.POST.get("addressline3")
            buyer.pin = Request.POST.get("pin")
            buyer.city = Request.POST.get("city")
            buyer.state = Request.POST.get("state")
            if(Request.FILES.get("pic")):
                buyer.pic = Request.FILES.get("pic")
            buyer.save()
            return HttpResponseRedirect("/profile/")
    return render(Request,"update-profile.html",{'data':buyer})

def addToCart(Request,num):
    p = Product.objects.get(id=num)
    cart = Request.session.get("cart",None)
    if(cart):
        if(str(p.id) in cart):
            item = cart[str(p.id)]
            item['qty']=item['qty']+1
            item['total']=item['total']+p.finalprice
            cart[str(p.id)]=item
        else:
            cart.setdefault(str(p.id),{'name':p.name,'color':p.color,'size':p.size,'price':p.finalprice,'qty':1,'total':p.finalprice,'pic':p.pic1.url})
    else:
        cart = {str(p.id):{'name':p.name,'color':p.color,'size':p.size,'price':p.finalprice,'qty':1,'total':p.finalprice,'pic':p.pic1.url}}
    Request.session['cart']=cart
    total = 0
    for value in cart.values():
        total = total+value['total']
    if(total<1000 and total>0):
        shipping = 150
    else:
        shipping = 0
    Request.session['total']=total
    Request.session['shipping']=shipping
    Request.session['final']=total+shipping
    return HttpResponseRedirect("/cart/")

def cartPage(Request):
    cart = Request.session.get('cart',None)
    items = []
    for key,value in cart.items():
        value.setdefault('id',key)
        items.append(value)
    total = Request.session.get('total',0)
    shipping = Request.session.get('shipping',0)
    final = Request.session.get('final',0)
    return render(Request,"cart.html",{'cart':items,'total':total,'shipping':shipping,'final':final})

def deleteCartPage(Request,id):
    cart = Request.session.get("cart",None)
    if(cart and id in cart):
        del cart[id]
        Request.session['cart']=cart

        total = 0
        for value in cart.values():
            total = total+value['total']
        if(total<1000 and total>0):
            shipping = 150
        else:
            shipping = 0
        Request.session['total']=total
        Request.session['shipping']=shipping
        Request.session['final']=total+shipping
    return HttpResponseRedirect("/cart/")


def updateCartPage(Request,id,op):
    cart = Request.session.get("cart",None)
    if(cart and id in cart):
        item = cart[id]
        if(op=="dec" and item['qty']==1):
            pass
        elif(op=="dec"):
            item['qty']=item['qty']-1
            item['total']=item['total']-item['price']  
        else:
            item['qty']=item['qty']+1
            item['total']=item['total']+item['price']
        cart[id]=item 
        Request.session['cart']=cart

        total = 0
        for value in cart.values():
            total = total+value['total']
        if(total<1000 and total>0):
            shipping = 150
        else:
            shipping = 0
        Request.session['total']=total
        Request.session['shipping']=shipping
        Request.session['final']=total+shipping
        
    return HttpResponseRedirect("/cart/")