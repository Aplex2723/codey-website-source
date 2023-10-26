from django.shortcuts import render
from .models import ConctactModel
from .forms import ContactForm

# Create your views here

#TODO:  Enviar la peticion de contactos a travez de correo electronico
def ContactView(request):
    template_name = "contact/contact.html"
    new_contact = None

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            new_contact = contact_form.save(commit=False)
            new_contact.save()
            contact_form = ContactForm()
    else:
        contact_form = ContactForm()

    return render(request, template_name, {'contact_form': contact_form,
                                            'new_contact': new_contact})
