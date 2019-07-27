from django.shortcuts import render, get_object_or_404 
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Blog, BlogAuthor, BlogComment
from django.urls import reverse

class BlogListView(ListView):
    template_name = "blog/bloglist.html"
    model = Blog


class BlogDetailView(DetailView):
    template_name = "blog/blogdetail.html"
    model = Blog

class BloggersListView(ListView):
    template_name = "blog/bloggerslist.html"
    model = BlogAuthor    

class BloggerBlogList(ListView):
    template_name = "blog/bloggerdetail.html"
    model = Blog
    context_object_name = 'chicks'

    # in get queryset we filter all the blogs by the the selected authors
    def get_queryset(self):
        id = self.kwargs['pk']
        target_author = get_object_or_404(BlogAuthor, pk = id)
        return Blog.objects.filter(blogauthor=target_author)


    # in get context data we are returning the details of the author bio 
    def get_context_data(self, **kwargs):
        context = super(BloggerBlogList, self).get_context_data(**kwargs)
        context['babes']= get_object_or_404(BlogAuthor, pk = self.kwargs['pk'])
        return context
       
class BlogCommentCreate(CreateView):
    model = BlogComment
    fields = ['comment']
    template_name = "blog/newcomment.html"

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blogboi'] = get_object_or_404(Blog, pk = self.kwargs['pk'] ) 
        return context

    def form_valid(self, form):
        form.instance.commentUser = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail',kwargs={'pk':self.kwargs['pk']})    





