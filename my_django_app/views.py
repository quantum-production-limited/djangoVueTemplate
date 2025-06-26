from django.shortcuts import render


def example_vue_app(request):
    context = {
        "example_vue_app_props": {
            "fromDjango": "A string passed in as a prop from Django"
        }
    }
    return render(request, "my_django_app/example_vue_app.html", context=context)
