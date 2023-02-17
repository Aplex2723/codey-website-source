from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HTMLModel, Testimonials

from .forms import TestimonialsFrom

# Create your views here.
# class AboutView(TemplateView):
#     template_name = 'about/about-us.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["info"] = HTMLModel.objects.first()
#         return context

def AboutView(request):
    template_name = 'about/about-us.html'
    info = HTMLModel.objects.first()
    testimonials = Testimonials.objects.all()[:10]
    new_testimonial = None

    if request.method == "POST":
        testimonial_form = TestimonialsFrom(data=request.POST)
        if testimonial_form.is_valid():
            new_testimonial = testimonial_form.save()
    else:
        testimonial_form = TestimonialsFrom()


    return render(request, template_name, {
        "info": info,
        "testimonials": testimonials,
        "testimonial_form": testimonial_form
    }) 
    