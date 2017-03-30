from django.shortcuts import render

from hut.forms import AddHutForm
from hut.models import Huts


# Create your views here.
def huts_by_mountain(request):
    if request.method == 'GET':
        # TODO: handel for query
        pass


def all_huts(request):
    if request.method == 'GET':
        huts = Huts.objects.all()
        return render(request, 'show_all_huts.html', locals())


def hut_by_name(request):
    if request.method == 'GET':
        pass


def add_hut(request):
    if request.method == 'POST':
        form = AddHutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'test.html', locals())
    if request.method == 'GET':
        form = AddHutForm()
    return render(request, 'add_hut.html', locals())


def update_hut(request):
    if request.method == 'UPDATE':
        pass
    if request.method == 'DELETE':
        pass


def page_of_huts(request):
    if request.method == 'GET':
        pass
