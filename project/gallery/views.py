from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from custom_auth.models import User
# from django.contrib.auth.mixins import LoginRequiredMixin

from gallery.models import Post
from gallery.forms import ArtCreateForm


def index(request):
    return render(request, 'gallery/index.html')


def about_us_view(request):
    return render(request, 'gallery/about_us.html')


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    posts = Post.objects.all().filter(user_id=user.id).order_by('-created_at')
    context = {'user': user, 'posts': posts}
    return render(request, "gallery/profile.html", context)


class ArtCreate(CreateView):
    model = Post
    form_class = ArtCreateForm
    template_name = "gallery/art_create.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArtListView(ListView):
    model = Post
    paginate_by = 25
    template_name = "gallery/art_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]


class ArtDetailView(DetailView):
    model = Post
    template_name = "gallery/art_detail.html"
    context_object_name = "post"
