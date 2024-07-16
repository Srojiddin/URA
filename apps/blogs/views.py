from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from apps.blogs.models import Blog,Departments,About,Gallery,Contact
from apps.blogs.forms import BlogCreateForm, BlogUpdateForm, BlogDeleteForm,GalleryCreateForm,GalleryUpdateForm,GalleryDeleteForm,NewsSearchForm

from django.views.generic import View

class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogCreateForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog')


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog-default.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCreateForm()
        return context


class BlogLargeView(generic.ListView):
    model = Blog
    template_name = 'blog-large.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCreateForm()
        return context


class BlogSingleView(generic.ListView):
    model = Blog
    template_name = 'blog-single.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCreateForm()
        return context


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog-detail.html'
    context_object_name = 'detail'
    pk_url_kwarg = 'pk'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogUpdateForm
    template_name = 'blog/blog_update.html'
    success_url = reverse_lazy('blogs')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    template_name =  'blog/blog_delete.html'
    success_url = reverse_lazy('blogs')


class DepartmentsListView(generic.ListView):
    model = Departments
    template_name = 'departments.html'


class AboutUsView(generic.TemplateView):
    model = About
    template_name = 'about.html'





class GalleryCreateView(generic.CreateView):
    model = Gallery
    form_class = GalleryCreateForm
    template_name = 'gallery/gallery_create.html'
    context_object_name = 'gallery'
    success_url = reverse_lazy('index') 




class GalleryUpdateView(generic.UpdateView):
    model = Gallery
    form_class = GalleryUpdateForm
    template_name = 'gallery/gallery_update.html'
    success_url = reverse_lazy('gallery_list') 




class GalleryDeleteView(generic.DeleteView):
    model = Gallery
    template_name = 'gallery/gallery_delete.html'
    context_object_name = 'gallery'
    success_url = reverse_lazy('index') 
#


class GalleryListView(generic.ListView):
    model = Gallery
    template_name = 'project.html'
    context_object_name = 'gallery'



class GallerySingleView(generic.ListView):
    model = Gallery
    template_name = 'project-single.html'
    context_object_name = 'blogs'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactListView(generic.ListView):
    model = Contact
    template_name = 'contact.html'

class NewssearchView(View):
    def get(self, request):
        form = NewsSearchForm()
        return render(request, 'news_search.html', {'form': form, 'blogs': None})

    def post(self, request):
        form = NewsSearchForm(request.POST)
        if form.is_valid():
            search_name = form.cleaned_data.get('search_name')
            if search_name:
                blogs = Blog.objects.filter(name__icontains=search_name)  # Filtering by name
            else:
                blogs = Blog.objects.all()
            return render(request, 'news_search.html', {'form': form, 'blogs': blogs})
        return render(request, 'news_search.html', {'form': form, 'blogs': None})
