from django.http import HttpResponse
from django.template import loader

from .models import Post

# Create your views here.
def index(request):
    last_2_posts = Post.objects.order_by("-publish_at")[:2]
    template = loader.get_template("main_app/index.html")
    context = {
        "posts": last_2_posts,
        "user": "Skiff"
    }
    # response = "<br>".join([p.post_text for p in last_2_posts])
    return HttpResponse(template.render(context=context, request=request))


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    template = loader.get_template("main_app/post.html")
    context = {"post": post}
    return HttpResponse(template.render(context, request))