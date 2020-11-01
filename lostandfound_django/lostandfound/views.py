from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Item
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import ItemForm

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Item
    context_object_name = 'items'
def FoundView(request):
    item = get_object_or_404(Item, pk=request.POST['item'])
    item.found = True
    item.save()
    return redirect('index')
class CreateItemView(CreateView):
    model = Item
    template_name = 'item_form.html'
    form_class = ItemForm
class ItemDetailView(DetailView):
    model = Item
    template_name = 'item.html'
class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item_form.html'
    form_class = ItemForm
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_delete.html'
    success_url = reverse_lazy('index')