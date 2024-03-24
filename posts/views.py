from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .forms import PostForm  # Import the PostForm
from categories.models import Category  # Import the Category model
from .models import Post  # Import the Category model
from django.contrib.auth.models import User  # Import the User model (assuming you're using Django's built-in authentication)

# Create your views here.

class PostListView(View):
    template_name = 'posts/index.html'

    def get(self, request):
        posts = Post.objects.select_related('category', 'user').all()
        return render(request, self.template_name, {'posts': posts})
    
class PostCreateView(View):
    template_name = 'posts/create.html'  # Update the template name if needed

    def get(self, request):
        form = PostForm()
        categories = Category.objects.all()
        users = User.objects.all()
        return render(request, self.template_name, {'form': form, 'users': users, 'categories': categories})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Optionally, you can set the category and user based on your requirements
            # For example, you can get the first category and user from the database
            category = Category.objects.first()  # Get the first category from the database
            user = User.objects.first()  # Get the first user from the database
            
            # Assign the category and user to the post before saving
            post = form.save(commit=False)
            post.category = category
            post.user = user
            post.save()
            
            return redirect('post_list')  # Assuming 'post_list' is the name of the URL for post list view
        else:
            return render(request, self.template_name, {'form': form,})
        

class PostUpdateView(View):
    template_name = 'posts/update.html'  # Update the template name if needed

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        categories = Category.objects.all()
        users = User.objects.all()
        return render(request, self.template_name, {'form': form, 'users': users, 'categories': categories})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Assuming 'post_list' is the name of the URL for post list view
        else:
            return render(request, self.template_name, {'form': form})

class PostDeleteView(View):
    template_name = 'posts/delete.html'  # Update the template name if needed

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post_list')  # Assuming 'post_list' is the name of the URL for post list view