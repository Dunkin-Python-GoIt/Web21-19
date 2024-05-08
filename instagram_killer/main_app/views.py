from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm, CustomUserCreationForm


class PostCreateView(CreateView):
    model = Post
    author = "author"
    fields = ["post_text"]
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("index")
    
    def form_valid(self, form):
        setattr(form.instance, self.author, self.request.user)
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ["post_text"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("index")


class PostDeleteView(DeleteView):
    model = Post
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy("index")
    

# Create your views here.
def index(request):
    last_2_posts = Post.objects.order_by("-publish_at")[:2]
    template = loader.get_template("main_app/index.html")
    context = {
        "posts": last_2_posts
    }
    # response = "<br>".join([p.post_text for p in last_2_posts])
    return HttpResponse(template.render(context=context, request=request))


def register(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            # form.email_clean()
            form.save()  
            return redirect(to="index")
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'registration/register.html', context) 


# def post_details(request, post_id):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = Post.objects.get(pk=post_id)
#             post.post_text = form.cleaned_data.get("post_text")
#             post.save()
#             return redirect(to="index")
        
#     post = Post.objects.get(pk=post_id)
#     template = loader.get_template("main_app/post.html")
#     form = PostForm(instance=post)
#     context = {
#         "post": post,
#         "form": form
#         }
#     return HttpResponse(template.render(context, request))


# def post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to="index")
        
#     form = PostForm()
#     template = loader.get_template("main_app/post.html")
#     context = {
#         "form": form
#     }
#     return HttpResponse(template.render(context, request))
    