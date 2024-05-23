import site
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from app.models import JobPost

# Create your views here.

# job_title = [
#     "First Job",
#     "Second Job",
#     "Third Job",
#     "Fourth Job"
# ]

# job_description = [
#     "First job description",
#     "Second job description",
#     "Third job description",
#     "Fourth job description"
# ]

# my_list = ['Ken', 'King']
# is_authenticated = False



def jobs(request):
    jobs = JobPost.objects.all()

    context = {"jobs":jobs,}
    return render(request, "app/index.html", context)

def job_detail(request, id):
    # pass
    try:
        #  get the data according to the id
        job = JobPost.objects.get(id = id)
        context = {"job":job}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound('Page Not Found')
    


# def hello(request):
#     return render(request, 'app/hello.html', context)

# def hello(request):
#     # return HttpResponse('<h1>Hello world</h1>')
#     # site = "https://getbootstrap.com/"
#     # return HttpResponse(f'Visit <a href = "{site}">Bootstrap.com</a>')

#     list_of_jobs = '<ul>'

#     for j in job_title:
#         list_of_jobs += f'<i>{j}</i>'

#     list_of_jobs += '</ul>'
#     return HttpResponse(list_of_jobs)

# def job_detail(request, id):
#     if id == 0:
#         return redirect("/")
    
    

    
    # return_html = f'<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>'
    # return HttpResponse(return_html)
    # return HttpResponse(list_of_jobs)