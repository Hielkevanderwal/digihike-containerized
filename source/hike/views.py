from django.shortcuts import render, redirect
from .models import Route, RouteProgress, RouteSection, HintUsed

# Create your views here.
def index_view(request):
    return redirect("/hike/wiltz")

def wiltz_view(request):
    team_of_user = request.user.participating_in_team.first()
    current_route = Route.objects.first()

    route_sections = current_route.route_sections.all().order_by("ordering")
    used_hint_pks = HintUsed.objects.filter(team = team_of_user).values_list('route_section', flat=True)

    route_progress, existed = RouteProgress.objects.get_or_create(
        team = team_of_user,
        route = current_route,
    )

    current_section = route_sections[route_progress.progress-1]

    fout_text = ""

    if request.method == "POST":
        if test_awnser(request, current_section):
            route_progress.progress = route_progress.progress + 1
            route_progress.save()
        
        else:
            fout_text = "Fout!"


    display_next_question = route_progress.progress < len(route_sections)
    display_hint = current_section.hint != ""
        
    
    return render(request, "rsa-hike/wiltz-1.html", context={
        "wrong_anwer": fout_text,
        "hint_available": display_hint,
        "display_question": display_next_question,
        "question": route_sections[route_progress.progress-1],
        "available_hints": used_hint_pks,
        "route_sections": route_sections[0:route_progress.progress]
    })

def get_hint(request, route_progress_pk):
    if request.method == "POST":
        print()
        HintUsed.objects.create(
            team =request.user.participating_in_team.first(),
            route_section = RouteSection.objects.get(pk = route_progress_pk)
                                )

    return redirect('/hike/wiltz')

def test_awnser(req, section):
    print(req.POST)

    for index, answer in enumerate(section.answer.splitlines()):
        print(req.POST.get(str(index)), answer)
        if req.POST.get(str(index)) != answer:
            break

    else:
        return True      
    return False