from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import itemForm 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.views import View
# Create your views here.
def index(request):
    Item_list = Item.objects.all()
    template = loader.get_template("food/index.html")
    params={
        'item': Item_list,
    }
    # return HttpResponse(template.render(params, request))
    return render(request, "food/index.html",params )

# class based views 
class IndexClassView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = 'item'

def detail(request, id):
    item_id = Item.objects.get(pk=id) # pk - primary key
    params={
        'item':item_id,
    }

    # return HttpResponse("This is the food item numbered-> %s" % id)
    return render(request, "food/detail.html", params)

class ItemDetailView(DetailView):
    model=Item
    template_name = 'food/detail.html'

# def addItem(request):
#     # return HttpResponse("Adding Item here")
#     params={}
#     form = itemForm(request.POST or None, request.FILES or None)
#     if(form.is_valid()):
#         form.save()
#         return redirect("food:index")
#     params['form'] = form
    
#     return render(request, 'food/form_succ.html',params)

class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'desc', 'price', 'image']
    template_name = "food/form_succ.html"

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)
    



# def updateItem(request, id):
#     item = Item.objects.get(pk=id)
#     form  = itemForm(request.POST or None, instance=item)
#     if(form.is_valid()):
#         form.save()
#         return redirect("food:index")
#     params={}
#     params["form"] = form
#     params["item"] = item

#     return render(request, "food/form_succ.html", params)

class updateItem(UpdateView):
    model = Item
    fields="__all__"
    success_url="food:index"


def deleteItem(request, id):
    item = Item.objects.get(pk=id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request, 'food/confirm_delete.html',{'item':item})






def contact(request):
    return HttpResponse("contact page")