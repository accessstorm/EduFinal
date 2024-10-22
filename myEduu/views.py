#own
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Profile, Comment


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

def loginT(request):
    return render(request, 'loginT.html', {})

def error(request):
    return render(request, 'error.html', {})

def forum(request):
    return render(request, 'forum.html', {})

def link(request):
    return render(request, 'link.html', {})

def ytlink(request):
    return render(request, 'ytlink.html', {})

def stlink(request):
    return render(request, 'stlink.html', {})



def postT(request):
    return render(request, 'postT.html', {})



def Cato(request):
    cat_menu_list = Category.objects.all().order_by('name')
    return render(request, 'all_categories.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})




def LikeView(request, pk):
    # Retrieve a single post object
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    # Redirect to the view2 page
    return HttpResponseRedirect(reverse('view2', args=[str(pk)]))






#class based views

class PostView(ListView):
    model = Post
    template_name = 'view1.html'
    ordering = ['-post_date']
    #ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ShowView(DetailView):
    model = Post
    template_name = 'view2.html'
    
    def get_context_data(self, *args, **kwargs):
        
        cat_menu = Category.objects.all()
        context = super(ShowView, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
from django.contrib.auth.mixins import LoginRequiredMixin
from ckeditor_uploader.views import upload

class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'postT.html'

    def post(self, request, *args, **kwargs):
        # Custom logic to allow image uploads for non-admin users
        if 'upload' in request.path:
            return upload(request)  # Delegate to CKEditor's upload view
        return super().post(request, *args, **kwargs)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    #fields = ('title' , 'body')
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('view1')
    
    
class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title' , 'body')
    
class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body'] this will not allow styling in template
    
class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('view1')
    
    

import math

def calculator(request):
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            # Safely evaluate the mathematical expression
            result = eval(expression, {"__builtins__": None}, math.__dict__)
        except Exception as e:
            result = "Error"
        return render(request, 'calculator.html', {'result': result})
    
    return render(request, 'calculator.html')
