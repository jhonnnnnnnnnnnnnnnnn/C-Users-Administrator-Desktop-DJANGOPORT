from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render (request,"home.html")

def about(request):
    return render (request,"about.html")

def projects (request):
    projects_show=[

        {
            "title":"Mental health check-in",
        "path":"images/image.jpg"
        },

        {
            "title":"Online Portfolio",
        "path":"images/portonline.jpeg"
        }

    ]
    return render (request,"projects.html",{"projects_show":projects_show})

def eda(request):

    eda=[
        {
            "school":"YPLC",
            "grade":" kindergarten"
        },

        {
            "school":"Cornelia M De Jesus",
            "grade":"Grade 1-6"
        },

        {
            "school":"Pulong Buhangin National Highschool",
            "grade":"Grade 7-10"
        },

        {
            "school":"Mystical Rose School of Bulacan",
            "grade":"Grade 11-12"
        }

    ]

    return render (request,"eda.html",{"eda":eda})

def testimonials(request):
    return render (request, "testimonials.html")

def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)