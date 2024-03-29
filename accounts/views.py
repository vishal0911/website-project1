from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import OrderForm, CreateUserForm,CustomerForm
from .models import *
from .filters import OrderFilter
from .decorators import unauthenticated_user,allowed_user,admin_only



@unauthenticated_user
def loginPage(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username OR Password is incorrect')
	context={}
	return render(request,'accounts/login.html',context)


@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			
			messages.success(request, 'Account was created for ' + username)

			return redirect('login')


	context = {'form': form}
	return render(request, 'accounts/register.html', context)

def logoutPage(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def userPage(request):
	orders=request.user.customer.order_set.all()

	total_order = orders.count()
	delivered=orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context={'orders':orders,'number_order':total_order,'delivered':delivered,'pending':pending}
	return render(request,'accounts/user.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def accountSettings(request):
	customer=request.user.customer
	form= CustomerForm(instance=customer)

	if request.method=="POST":
		form = CustomerForm(request.POST,request.FILES,instance=customer)
		if form.is_valid():
			form.save()
	context={'form':form}
	return render(request,'accounts/account_settings.html',context)




@login_required(login_url='login')
#@allowed_user(allowed_roles=['admin'])
@admin_only
def home(request):
	customer=Customer.objects.all()
	order=Order.objects.all()
	total_customers=customer.count()
	total_order=order.count()
	delivered=order.filter(status='Delivered').count()
	pending=order.filter(status='Pending').count()
	context={'customer':customer,'order':order,'number_customer':total_customers,'number_order':total_order,'delivered':delivered,'pending':pending}
	return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def products(request):
	products=Product.objects.all()
	return render(request, 'accounts/products.html',{'products':products})

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request, pk):

	customer=Customer.objects.get(id=pk)
	orders=customer.order_set.all()
	orders_count=orders.count()
	myFilter=OrderFilter(request.GET,queryset=orders)
	orders=myFilter.qs
	context={'customer':customer,'orders':orders,'orders_count':orders_count,'myFilter':myFilter}
	return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def createOrder(request,pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'),extra=10)
	customer=Customer.objects.get(id=pk)
	formset=OrderFormSet(queryset=Order.objects.none(), instance=customer)
	if request.method=="POST":
		formset=OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context={'formset':formset}
	return render(request,'accounts/order_form.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateOrder(request,pk):
	order=Order.objects.get(id=pk)
	form=OrderForm(instance=order)
	if request.method=="POST":
		form=OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request,'accounts/order_form.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteOrder(request,pk):
	order = Order.objects.get(id=pk)
	if request.method=="POST":
		order.delete()
		return redirect('/')
	context={'item':order}
	return render(request,'accounts/delete.html',context)
