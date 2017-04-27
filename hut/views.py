from django.shortcuts import render, redirect

from hut.forms import AddHutForm
from hut.models import Huts


# Create your views here.
def home(request):
    return render(request, 'navbar.html', locals())


def all_huts(request):
    if request.method == 'GET':
        huts = Huts.objects.all()
        return render(request, 'show_all_huts.html', locals())


def add_hut(request):
    if request.method == 'POST':
        form = AddHutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/huts')
    if request.method == 'GET':
        form = AddHutForm()
    return render(request, 'add_hut.html', locals())


def show_hut(request, hutname):
    if request.method == 'GET':
        huts = Huts.objects.filter(hutname__icontains=hutname)
        return render(request, 'show_all_huts.html', locals())


def update_hut(request, hutname):
    print('-----------', request.method)
    if request.method == 'POST':
        form = AddHutForm(request.POST, request.FILES)
        if form.is_valid():
            hut = Huts.objects\
                      .filter(hutname__icontains=form.cleaned_data['hutname'])\
                      .first()
            hut.image = form.cleaned_data['image']
            hut.altitude = form.cleaned_data['altitude']
            hut.mountain = form.cleaned_data['mountain']
            hut.people_capacity = form.cleaned_data['people_capacity']
            hut.email = form.cleaned_data['email']
            hut.image = form.cleaned_data['image']
            hut.phone = form.cleaned_data['phone']
            hut.save()
            return redirect('/huts')
    if request.method == 'DELETE':
        pass
    if request.method == 'GET':
        hut = Huts.objects.filter(hutname__icontains=hutname).first()
        form = AddHutForm(initial={'hutname': hut.hutname,
                                   'image': hut.image,
                                   'altitude': hut.altitude,
                                   'mountain': hut.mountain,
                                   'people_capacity': hut.people_capacity,
                                   'email': hut.email,
                                   'phone': hut.phone})
    return render(request, 'update_hut.html', locals())


def huts_by_mountain(request):
    if request.method == 'GET':
        # TODO: handel for query
        pass


def hut_by_name(request):
    if request.method == 'GET':
        pass


def page_of_huts(request):
    if request.method == 'GET':
        pass
