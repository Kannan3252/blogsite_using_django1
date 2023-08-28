from django.shortcuts import render,redirect
from django.views import generic 
from .models import Post
from .forms import BlogPostForm

# Create your views here.
class PostList(generic.ListView):
    queryset=Post.objects.all().order_by('-created_on')
    template_name='index.html'

class PostDetail(generic.DetailView):
    model=Post
    template_name='Post_detail.html'

class create_blog_post1(generic.ListView):
    def create_blog_post(request):
        if request.method == 'POST':
            form = BlogPostForm(request.POST)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user  # Assuming you're using Django's built-in User model
                blog_post.save()
                return redirect('app/templates/index.html')  # Redirect to the appropriate page
        else:
            form = BlogPostForm()
        return render(request, 'app/templates/create_blog_post.html', {'form': form})