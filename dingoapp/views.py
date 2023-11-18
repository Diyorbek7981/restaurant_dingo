from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from blogapp.models import Coments
from .models import *
from .forms import *


# Create your views here.

# Function Basic
def index(request):
    chefs = Chefs.objects.filter(level__ch_level='Chef Master')
    exfoods = FoodModel.objects.filter(exsclusive=True)[:3]

    category = Category.objects.all()
    cat = request.GET.get('cat')
    if cat is None:
        cat = 'Special'
    foods = FoodModel.objects.filter(category__category_name=cat)[:6]

    best = Coments.objects.filter(best_comment=True)[:3]
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/#xTab')

    contex = {'home_menu': 'home_menu',
              'chefs': chefs,
              'foods': foods,
              'foods3': foods[:3],
              'foods6': foods[3:6],
              'categories': category,
              'cat': cat,
              'form': form,
              'best':best,
              'exfoods': exfoods}
    return render(request, 'index.html', contex)


# Basic class
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        my_context = super().get_context_data(**kwargs)
        my_context['level'] = ChefLevel.objects.all()
        cat = self.request.GET.get('cat')
        if cat is None:
            cat = 'Chef Master'
        my_context['chefs'] = Chefs.objects.filter(level__ch_level=cat)
        my_context['best'] = Coments.objects.filter(best_comment=True)[:3]

        return my_context


class MenuView(TemplateView):
    template_name = 'food_menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        cat = self.request.GET.get('cat')
        if cat is None:
            cat = 'Special'
        foods = FoodModel.objects.filter(category__category_name=cat)[:6]
        context['foods3'] = foods[:3]
        context['foods6'] = foods[3:6]

        return context


class ChefsView(TemplateView):
    template_name = 'chefs.html'

    def get_context_data(self, **kwargs):
        i_context = super().get_context_data(**kwargs)
        i_context['level'] = ChefLevel.objects.all()
        cat = self.request.GET.get('cat')
        if cat is None:
            cat = 'Chef Master'
        i_context['chefs'] = Chefs.objects.filter(level__ch_level=cat)

        return i_context


class ElementsView(TemplateView):
    template_name = 'elements.html'


class ContactView(CreateView):
    template_name = 'contact.html'

    model = Contact
    form_class = ContactForm
