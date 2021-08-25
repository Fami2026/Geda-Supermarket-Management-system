from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import Orderform 
from .forms import CreateUserForm
from .forms import SearchForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group
from django.views.generic import TemplateView



class AboutView(TemplateView):
      template_name ="about.html"
		
class ContactView(TemplateView):
      template_name ="contact.html"

class AdvertiseView(TemplateView):
      template_name ="advertise.html"      

class HomeView(TemplateView):
    template_name = "home1.html"

class Footer(TemplateView):
    template_name = "footer.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = "Dipak Niroula"
       
      
        context['product_list'] = Product1.objects.all()
        return  context



@login_required(login_url='login')
@admin_only
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_customers=customers.count()
	total_orders= orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending= orders.filter(status='Pending').count() 

	context ={'orders':orders, 'customers':customers,'total_orders':total_orders, 'delivered':delivered,'pending':pending }
	return render(request,'geda/dashboard.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test): 
	customer = Customer.objects.get(id=pk_test)
	orders = customer.order_set.all()
	order_count = orders.count()
	context ={'customer':customer,'orders':orders,'order_count':order_count}
	return render(request,'geda/customer.html',context)

@unauthenticated_user
def registerpage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			group=Group.objects.get(name='customer')
			user.groups.add(group)
			Customer.objects.create(user=user,)
			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
	context = {'form':form}
	return render(request,'geda/register.html',context)
@unauthenticated_user
def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')


	context ={}
	return render(request,'geda/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])	
def userPage(request):

	orders=request.user.customer.order_set.all()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	print('ORDERS:', orders)
	context = {'orders':orders, 'total_orders':total_orders,
	'delivered':delivered,'pending':pending}
	return render(request, 'geda/user.html', context)	

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def product(request):
	form =SearchForm(request.POST or None)
	product = Product.objects.all()
	context ={'product':product}

	if request.method == 'POST':
		product = Product.objects.filter(category =form['category'].value(),
			                              name=form['name'].value())
		context ={'form':form, 'product':product}
    

	return render(request,'geda/product.html',context)	

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('Product', 'status'), extra=5 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	# form= Orderform(initial={'customer':customer})
	if request.method == 'POST':
		# form = Orderform(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():

			formset.save()
			return redirect('/')

	context={'form':formset}
	return render (request,'geda/order_form.html',context) 	

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):


	order = Order.objects.get(id=pk)
	form = Orderform(instance=order)

	if request.method == 'POST':
		form = Orderform(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'geda/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'order':order}
	return render(request, 'geda/delete.html', context)	  