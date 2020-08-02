from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Pet


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})


def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('PET NOT EXIST')
    # pet = get_object_or_404(klass=Pet, id=id)
    return render(request, 'pet_detail.html', {'pet': pet})

