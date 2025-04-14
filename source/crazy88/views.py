from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from .models import MissionList, MissionExecution, Team
from .forms import MissionUploadForm

from random import choice

HOME_SCREEN_RANDOM_MISSIONEXE_ENTRIES = 10

# Create your views here.
@login_required
def crazy88_view_home(request):
    active_mission_lists = MissionList.objects.filter(is_active = True)
    
    if len(active_mission_lists) == 1:
        return redirect("crazy88_view-list", mission_list = active_mission_lists.first().list_name)
    
    mission_exe_pks = MissionExecution.objects.values_list('pk', flat=True)
    random_objs = []

    # TODO fix getting duplicate mission obj on homescreen
    while len(random_objs) < HOME_SCREEN_RANDOM_MISSIONEXE_ENTRIES and mission_exe_pks != len(random_objs):
        random_pk = choice(mission_exe_pks)
        random_objs.append(MissionExecution.objects.get(pk=random_pk))
 


    return render(request, "crazy88_overview.html", context={
        "mission_lists": active_mission_lists,
        "random_mission_exe": random_objs,
    })

@login_required
def crazy88_view_list(request, mission_list):
    mission_list_obj = get_object_or_404(MissionList, list_name = mission_list)
    missions = []

    # Make an array with mission objects
    for index, mission in enumerate(mission_list_obj.missions.rsplit("\n")):
        missions.append({
            "index": index + 1,
            "mission": mission,
            "teams_who_did": []
        })

    # add teams who did a mission
    mission_executions_list = MissionExecution.objects.filter(mission_list = mission_list_obj)
    for mission_exe in mission_executions_list:
        missions[mission_exe.mission_number - 1]["teams_who_did"].append(mission_exe.team)


    return render(request, "crazy88.html", context={
        "mission_list": mission_list_obj.list_name,
        "missions": missions
    })

@login_required
def view_detailed_task(request, mission_list, mission_number):

    if request.method == "POST":
        form = MissionUploadForm(request.POST, request.FILES)
        if form.is_valid():
            miss_ex = form.save(commit=False)
            miss_ex.mission_list = MissionList.objects.get(list_name = mission_list)
            miss_ex.mission_number = mission_number
            miss_ex.team = Team.objects.filter(team_members__in=[request.user]).first()

            miss_ex.save()

            return HttpResponseRedirect('')

    mission_list_obj = get_object_or_404(MissionList, list_name = mission_list)
    mission_exe = MissionExecution.objects.filter(mission_list = mission_list_obj.pk, mission_number = mission_number).order_by("upload_date").reverse()

    can_upload = (len(request.user.participating_in_team.all()) !=0) and mission_list_obj.is_active

    return render(request, "crazy88_detailed.html", context={
        "mission_list": mission_list_obj,
        "mission": get_task(mission_list_obj.missions, mission_number - 1),
        "missione_xecutions": list(mission_exe),
        "show_upload": can_upload,
        "upload_form": MissionUploadForm,
    })




#--------------------------------------------------------------
#   Helper functions
#--------------------------------------------------------------

def create_task_list(input: str):
    task_list = []
    for line in input.rsplit("\n"):
        task_list.append(line.lstrip())

    return task_list

def get_task(task_list, index):
    return create_task_list(task_list)[index]