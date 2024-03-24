from django.shortcuts import render, redirect, get_list_or_404
from django.views import View
from .models import Category
from .forms import CategoryForm  # Import CategoryForm

class CategoryListView(View):
    template_name = 'categories/index.html'

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})
    
class CategoryCreateView(View):
    template_name = 'categories/create.html'

    def get(self, request):
        form = CategoryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Assuming 'category_list' is the name of the URL for category list view
        else:
            return render(request, self.template_name, {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CategoryForm
from .models import Category

class CategoryUpdateView(View):
    template_name = 'categories/update.html'

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(instance=category)
        return render(request, self.template_name, {'form': form, 'category': category})
    
    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Assuming 'category_list' is the name of the URL for category list view
        else:
            return render(request, self.template_name, {'form': form, 'category': category})


class CategoryDeleteView(View):
    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect('category_list')