from django.shortcuts import render
from .models import Item

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_next']
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''

    context = {'new_item_text': new_item_text}
    return render(request, 'home.html', context)

