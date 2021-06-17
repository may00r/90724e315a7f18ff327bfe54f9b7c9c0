from django.http import HttpResponse
from django.shortcuts import redirect


def go_to_admin(request):
    return redirect('/admin')
