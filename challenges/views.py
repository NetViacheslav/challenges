from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': "Prepare documents for the visa",
    'february': "Visit department",
    'march': "Work, work",
    'april': "Same work, work",
    'may': "Make weekend and hiring mount",
    'june': "Again work",
    'july': "Make weekend",
    'august': "Again work",
    'september': "Work and study",
    'october': "Travel in Europe",
    'november': "Work",
    'december': "Prepare towards to Christmas"
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html',{
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
