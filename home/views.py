# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports


def home(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "home/home.html", data)
