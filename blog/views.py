from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

from .models import Post, Category
from .forms import CommentForm
from django.db.models import Count
from registration.models import Profile

class StaffRequieredMixin(object):

    #Este Mixin requerirar que el usuario se amiembro del staff
    #Evitando que usuarios no identificados, modifiquen la pagina desde las urls

    #El siguiente metodos(decorador) nos servira para pedir una autentificacion
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
            #Verificando si es usuario es staff, y reedireccionandolo al panel de control, esto no es necesario si tenemos un decorador
            #if not request.user.is_staff:
                #return redirect(reverse_lazy('admin:login'))
            return super(StaffRequieredMixin, self).dispatch(request, *args, **kwargs)


class PostListView(ListView):
    model = Post
    ordering = ['-created']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all() 
        
        return context
    

# class PostDetailView(DetailView):
#     model = Post
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = Category.objects.all() 
        
#         return context
def PostDetailView(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    all_post = Post.objects.all()
    categories = Category.objects.all()
    profiles = Profile.objects.all()
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                            'post_list': all_post,
                                            'comments': comments,
                                            'categories': categories,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form,
                                            "profiles": profiles})

class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories_list'
    template_name = "blog/category.html"

    def get_queryset(self):
        return Category.objects.filter(id=self.kwargs.get('category_id')).all()
    


def blog(request):
    posts = Post.objects.all()
    return render(request,'blog/blog.html', {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id) #forzando un error por si no se encuentra el id
    return render(request,'blog/category.html', {'category':category})
