from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse

from custom_auth.models import User
# from django.contrib.auth.mixins import LoginRequiredMixin

from gallery.models import Post
from gallery.forms import ArtCreateForm, ArtCommentForm


def index(request):
    return render(request, 'gallery/index.html')


def about_us_view(request):
    return render(request, 'gallery/about_us.html')


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    posts = Post.objects.all().filter(user_id=user.id).order_by('-created_at')
    context = {'user': user, 'posts': posts}
    return render(request, "gallery/profile.html", context)


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('art-detail', pk=pk)


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

    form = ArtCommentForm()

    def post(self, request, *args, **kwargs):
        form = ArtCommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse('art-detail', kwargs={
                'pk': post.id
            }))

    def get_context_data(self, **kwargs):
        context = super(ArtDetailView, self).get_context_data(**kwargs)
        likes = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = likes.total_likes()
        context['total_likes'] = total_likes
        context['form'] = self.form
        return context
