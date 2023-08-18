from django.shortcuts import render


def home(request):

    context = {
        'text': 'HOME',
        'title': 'Home',
    }

    return render(
        request,
        'home/index.html',
        context
    )
