from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Product
from .models import CustomerOrder
from .models import GenerateTransaction



def home(request):
    context = {
        'posts': Product.objects.all()
    }
    return render(request, 'home.html', context)

class SalesListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering ='product_id'

class SalesDetailView(DetailView):
    model = Product
    fields = ['product_name','product_des','quantity','price']
    template_name = 'detail.html'  

class SalesCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['product_name','product_des','quantity','price']
    template_name = 'product_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
            
class SalesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['product_name','product_des','quantity','price']
    template_name = 'product_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return True

class SalesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'
    template_name = 'confirm_delete.html'

    def test_func(self):
        return True

#===========================================================ITO ADDED
class CustomerSalesCreateView(CreateView,ListView):
    model = Product
    fields = ['product_name','quantity','price']
    template_name = 'TESTER.html'
    context_object_name = 'posts'
    ordering ='id'

    def post(self, request, *args, **kwargs):
        #============================ ILALAGAY LAHAT NG NASELECT NG POSTAB.HTML SA items[] 
        order_items = {
            'items':[]
        }
        #=========================== items[] gagawin dictionary ng order_items
        amt = request.POST.get('quantity')
        items = request.POST.getlist('items[]')
        #=========================== lahat ng value ng items[] kukunin, note mga IDs lng yan
        for item in items:

            product = Product.objects.get(pk__contains=int(item))
            product_data = {
                'id': product.product_id,
                'name':product.product_name,
                'price':product.price,
                'quantity': product.quantity

            }
        #=========================== lahat ng ID ng nasaloob ng items, kukunin data gaya ng price nayan
        #=========================== lahat ng nacollect na data, idadagdag sa order_items base sa id nila
            order_items['items'].append(product_data)
            price = 0
            item_ids = []
        
        #=========================== lahat ng nacollect na data, at since may full data na, kukunin lng
        #=========================== price at pagaadd
        for item in order_items['items']:
            price += item['price'] 
            item_ids.append(item['id'])

        order = CustomerOrder.objects.create(price=price)
        order.items.add(*item_ids)

        #=========================== lalagay sa context para mabasa ng HTML
        context = {
            'items':order_items['items'],
            'price':price
        }

    


        return render(request, 'customerconfirm.html',context)

class CustomerOrders(ListView):
    model = CustomerOrder
    template_name = 'salesinput.html'  
    context_object_name = 'posts'
    
def Salesinput(request):
    return render(request, 'salesinput.html', {'title': 'About'})

class POSGenerateTransaction(CreateView,ListView):
    model = Product
    fields = ['product_name','quantity','price']
    template_name = 'POSTAB.html'
    context_object_name = 'posts'
    ordering ='id'


    def post(self, request, *args, **kwargs):
        #============================ ILALAGAY LAHAT NG NASELECT NG POSTAB.HTML SA items[] 
        order_items = {
            'items':[]
        }
        #=========================== items[] gagawin dictionary ng order_items
        amt = request.POST.get('quantity')
        items = request.POST.getlist('items[]')
        #=========================== lahat ng value ng items[] kukunin, note mga IDs lng yan
        for item in items:

            product = Product.objects.get(pk__contains=int(item))
            product_data = {
                'id': product.product_id,
                'name':product.product_name,
                'price':product.price,
                'quantity': product.quantity

            }
        #=========================== lahat ng ID ng nasaloob ng items, kukunin data gaya ng price nayan
        #=========================== lahat ng nacollect na data, idadagdag sa order_items base sa id nila
            order_items['items'].append(product_data)
            price = 0
            item_ids = []
        
        #=========================== lahat ng nacollect na data, at since may full data na, kukunin lng
        #=========================== price at pagaadd
        for item in order_items['items']:
            price += item['price'] 
            item_ids.append(item['id'])

        order = CustomerOrder.objects.create(price=price)
        order.items.add(*item_ids)

        #=========================== lalagay sa context para mabasa ng HTML
        context = {
            'items':order_items['items'],
            'price':price
        }

        return render(request, 'TESTER2.html',context)

class POSListView(ListView):
    model = GenerateTransaction
    template_name = 'POSTAB.html'
    context_object_name = 'posts'
    ordering ='id'

#===========================================================ITO ADDED

def Trans(request):
    return render(request, 'trans.html', {'title': 'About'})

def Salesinput(request):
    return render(request, 'salesinput.html', {'title': 'About'})

def about(request):
    return render(request, 'about.html', {'title': 'About'})

