from django.shortcuts import render

def about(req):
    return render(req, "about.html")

def homepage(req):
    return render(req, "homepage.html")