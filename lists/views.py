from django.shortcuts import render

# Create your views here.


def home_page(request):
    context = {'new_item_text': request.POST.get('item_next', '')}
    return render(request, 'home.html', context)

