from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from ecart_app.models import product
from ecart_app.models import register
from ecart_app.forms import registerForm
from ecart_app.models import category
from ecart_app.models import subcategory
from ecart_app.models import cart
from django.contrib import messages
from ecart_app.models import order
from django.contrib.auth import logout
from datetime import datetime,date,timedelta


# Create your views here.

def home(request):
    form=product.objects.all()
    return render(request,'home.html',{'form':form})

def Signin(request):
    print('hii')
    if request.method=="POST":
        a=request.POST.get('Name')
        b=request.POST.get('Password')
        user1=register.objects.get(Name=a)
        if user1.Name==a and user1.Password==b:
            request.session['Name']=user1.Name
            request.session['Email']=user1.Email
            return redirect('/home')
        else:
            return redirect('/register')
    else:
        form=registerForm()
        return render(request,"signin.html",{'form':form})
def Register(request):
    if request.method=="POST":
        print('a')
        form=registerForm(request.POST)
        if form.is_valid():
            print("b")
            form.save()
            return redirect('/signin')        
    else:
        form=registerForm()    
    return render(request,"register.html",{'form':form})

def Category(request):
    form=category.objects.all()
    return render(request,'category.html',{'form':form})

def Subcategory(request,id):
    form=subcategory.objects.filter(category_id=id)
    return render(request,'subcategory.html',{'form':form})

def Product(request,id):
    form=product.objects.filter(subcategory_id=id)
    return render(request,'product.html',{'form':form})

def Viewproduct(request,id):
    pform=product.objects.get(id=id)
    return render(request,'viewproduct.html',{'pform':pform})

def Order(request,id):
    if request.session.get('Name'):
        name=request.session['Name']
        user1=register.objects.get(Name=name)
        buy=order.objects.filter(register=user1)
        print(buy)
        Cart=cart.objects.filter(register=user1)
        # print(cart)
        today=date.today()
        time=today+timedelta(days=7)
        if request.method=='POST':
            val=request.POST.get('buyvalue')
            val=int(val)
            print(val)
            form=product.objects.get(id=id)
            a=order.objects.filter(name=form.name)
            b=1
            for i in (a):
                if i.register.Name==user1.Name and i.conformation==0:
                    b=2
                    break
                else:
                    b=1
            if (a.exists()) and b==2:
                messages.warning(request,'This product already in your cart')
                return redirect('viewproduct',form.id)
            else:
                name1=request.session['Name']
                user1=register.objects.get(Name=name1)
                overallpr=val*form.price
                if val > form.quantity:
                    messages.warning(request,'Your order count is not available in stock')
                    return redirect('/viewproduct',form.id)
                else:
                    for i in Cart:
                        if i.product.name==form.name:
                            i.delete()
                    order.objects.create(product=form,register=user1,name=form.name,image=form.image,quantity=val,price=form.price,totalprice=overallpr,detail=form.detail).save()
    else:
        return redirect('/signin')
    return render(request,'order.html',{'buy':buy})

def Orders(request,id):
    name1=request.session['Name']
    user1=register.objects.get(Name=name1)
    buy=order.objects.filter(register=user1)
    buy1=order.objects.get(id=id)
    today=buy1.updated
    time=today+timedelta(days=7)
    time=time.strftime('%b-%d')
    if request.method=='POST':     
        val=request.POST.get('but')
        if val=='conformation':
            if (order.objects.filter(name=buy1.name).exists()) and buy1.conformation==1:
                pass
            else:
                if buy1.product.quantity >= buy1.quantity:
                    buy1.conformation=True
                    buy1.delivery=time
                    buy1.product.quantity=buy1.product.quantity-buy1.quantity
                    buy1.save()
                    buy1.product.save()
                    messages.error(request,'Your order successfully placed')
                else:
                    print("Your order count is not available in stock")
    return render(request,'order.html',{'buy':buy})

def Buy(request):
    name1=request.session['Name']
    user1=register.objects.get(Name=name1)
    buy=order.objects.filter(register=user1)
    # today=buy.updated
    # time=today+timedelta(days=7)
    return render(request,'order.html',{'buy':buy})

def Cancelorder(request,id):
    Buyprod=(order.objects.get(id=id))
    Buyprod.product.quantity=Buyprod.quantity+Buyprod.product.quantity
    Buyprod.product.save()
    Buyprod.delete()
    return redirect('/buy')

def Remove(request,id):
    Buyprod=(order.objects.get(id=id))
    Buyprod.product.save()
    Buyprod.delete()
    return redirect('/buy')


def Carts(request):
    name=request.session['Name']
    user1=register.objects.get(Name=name)
    form=cart.objects.filter(register=user1)
    print(form)
    return render(request,'carts.html',{'form':form})

def Cart(request,id):
    if request.session.get('Name'):
        name=request.session['Name']
        print(name)
        user1=register.objects.get(Name=name)
        print(user1)
        carts=cart.objects.filter(register=user1)
        print(carts)
        if request.method =='POST':
            print("posted")
            value=int(request.POST.get('cartvalue'))
            print(value)
            form=product.objects.get(id=id)
            print(form)
            x=cart.objects.filter(name=form.name)
            y=1
            for i in (x):
                if i.register.Name==user1.Name:
                    y=2
                    break
                else:
                    y=1
            if (x.exists()) and y==2:
                messages.warning(request,'This product is already available in your cart')
                return redirect('viewproduct',form.id)
            
            name1=request.session['Name']
            user2=register.objects.get(Name=name1)
            tot=value*form.price
            cart.objects.create(product=form,register=user2,name=form.name,image=form.image,quantity=value,price=form.price,totalprice=tot,detail=form.detail).save()
            # cart.save()
    else:
        return redirect('/signin')
    return render(request,'cart.html',{'carts':carts})

def removecart(request,id):
    form=(cart.objects.get(id=id))
    form.delete()
    return redirect('/carts')
    

def Signout(request):
    logout(request)
    return render(request,'home.html')



