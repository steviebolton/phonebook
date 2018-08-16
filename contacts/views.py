from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {'contacts': contacts})
    
    
def add_contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contact_list)
    else:
        form = ContactForm()
    
    return render(request, "contacts/contact_form.html", {'form': form})
    
    
def edit_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)
    
    if request.method=="POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(contact_list)
    else:
        form = ContactForm(instance=contact)
    
    return render(request, "contacts/contact_form.html", {'form': form})