from django.shortcuts import render, redirect
from accounts.models import *
from .forms import OrderForm, UserRegister
from django.forms import inlineformset_factory
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout


def register(request):
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()

            messages.success(request,'Account was created for ' + user )

            return redirect('login')

    context = {
        'form' : form,

    }
    
    return render(request,'accounts/register.html',context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.info(request,'username or password is incorrenct')


    context = {

    }

    return render(request,'accounts/login.html',context)


def logoutuser(request):
    pass


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'customers' : customers,
        'orders' : orders,
        'total_customers' : total_customers,
        'total_orders' : total_orders,
        'delivered' : delivered,
        'pending' : pending,
    }
    return render(request,'accounts/dashboard.html',context)


def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request,'accounts/products.html',context)


def customers(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    #filtering_order
    order_Filter = OrderFilter(request.GET,queryset=orders)
    orders = order_Filter.qs

    context = {
        'customer' : customer,
        'orders' : orders,
        'order_count' : order_count,
        'orderFilter' : order_Filter,
    }

    return render(request,'accounts/customers.html',context)


def createorder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form' : form,
    }
    return render(request,'accounts/order_form.html',context)



def createorderinlineset(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'),extra=5)
    customer = Customer.objects.get(id=pk)

    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    
    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {
        'formset' : formset,
    }

    return render(request,'accounts/order_form_inline.html',context)


def updateorder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance = order)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form,
    }

    return render(request, 'accounts/update_order.html',context)


def deleteorder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item' : order,
    }
    return render(request,'accounts/delete_order.html',context)