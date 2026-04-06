from django.shortcuts import render

books = [
    {'id': 1, 'title': 'Кобзар'},
    {'id': 2, 'title': 'Лісова пісня'},
    {'id': 3, 'title': 'Тигролови'},
]

def home(request):
    return render(request, 'index.html', {'books': books})

def book_detail(request, id):
    book = next((b for b in books if b['id'] == id), None)
    return render(request, 'detail.html', {'book': book})