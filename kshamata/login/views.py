from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from kshamata_users.models import Women, Volunteer, Activity
# Create your views here.


from django.http import HttpResponse
from django.template import loader
import json
import requests
from django.views.decorators.csrf import csrf_exempt


check = "false"
y = Women.objects.all()
k = Volunteer.objects.all()
a = Activity.objects.all()
m = []
l =[]
o = []


@login_required(login_url="login/")
def home(request):
    if request.user.username=='admin':
        return render(request,"admin_home.html")

    #name = request.user.username
    #z = Volunteer.objects.filter(name=request.user.username).values('name')
    #return render(request, "home.html", {'vol': z, 'name': name})
    return render(request, "home.html")


@login_required(login_url="login/")
def survey(request):
    return render(request, "make.html")


def make(request):
    if request.method == "POST":
        women = Women()
        women.name = request.POST['name']
        women.dob = request.POST['dob']
        women.aadhar_id = request.POST['aadhar']
        women.contact = request.POST['detail']
        women.background = request.POST['background']
        women.time_of_stay = request.POST['duration']
        women.skills = request.POST['skill']
        women.trainings = request.POST['training']
        women.level_of_skill = request.POST['skill_rating']
        women.cur_salary = request.POST['salary']
        women.cur_location = request.POST['location']
        women.future_plans = request.POST['plans']
        women.remarks = request.POST['remarks']
        women.date_of_survey = request.POST['date_survey']
        women.save()
        check = "true"
        return render(request, "make.html", {'check': check})


def show(request):
    name = request.user.username
    z = Volunteer.objects.filter(name=name).values('name')
    #x = [Volunteer.encode("utf-8") for volunteer in Volunteer.objects.filter(name=name).values('name')
    #definitions_list = [d
#   definition.encode("utf8") for definition in definitions.objects.values_list('title', flat=True)]

    #m.append([str(s) for s in Volunteer.objects.filter(name=name).values('name')])

    return render(request, "show.html", {'vol':k})

def search(request):
    return render(request, "search.html" , {'wom' : y})

@csrf_exempt
def location(request):
    p = Women.objects.all().values_list('cur_location')
    for x in p:
    # if post request came
        name = ""
        a = "https://maps.googleapis.com/maps/api/geocode/json?address="
        d = name.replace(" ", "+")
        link1 = a + d
        link1 = link1 + "&key="
        key = "AIzaSyDYmXM1x027foY3T8RUf4874x3bf3OvU5g"
        final = link1 + key
        response = requests.get(final)
        json_data = json.loads(response.text)
        b = json_data['results'][0]

        c = b['geometry']['location']
        l.append(c['lat'])
        o.append((c['lng']))
    # adding the values in a context variable
    context = {
        'mylat': c['lat'],
        'mylong': c['lng'],
              }

    # getting our showdata template
    template = loader.get_template("location.html")
    # returing the template
    return HttpResponse(template.render(context, request), {'l':l,'o':o})