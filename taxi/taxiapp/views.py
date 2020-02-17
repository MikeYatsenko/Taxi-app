from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderForm
from .models import Order, Car
from  django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,UpdateView, DeleteView)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CreateOrderView(CreateView):
    form_class = OrderForm
    model = Order
    def get_success_url(self):
        return ('finish')

class AboutView(TemplateView):
    template_name = 'taxiapp/about.html'

class FinishView(ListView):
    model = Car
    template_name = 'taxiapp/finish.html'
    context_object_name = 'cars'
    queryset = Car.objects.filter(is_free=True)[0]

class OrderListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Order
    template_name = 'taxiapp/order_list.html'
    context_object_name = 'orders'
    paginate_by = 4
    queryset = Order.objects.order_by('-time')

class OrderDetailedView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Order
    template_name = 'taxiapp/order_list_detail.html'