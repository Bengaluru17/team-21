from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from kshamata_users.models import Women, Volunteer, Activity
# Create your views here.

check = "false"
y = Women.objects.all()
k = Volunteer.objects.all()
a = Activity.objects.all()


@login_required(login_url="login/")
def home(request):
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

