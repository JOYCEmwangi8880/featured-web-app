from django.shortcuts import render

posts=[
    {
        'author':  'Joyce',
        'title': 'blog 1 software',
        'content': 'coding',
        'date_posted': 'March 26, 2024'
    },
     {
        'author':  'Mwangi',
        'title': 'blog 2 Django',
        'content': 'django project',
        'date_posted': 'March 27, 2024'
    },
    {
        'author':  'Maggy',
        'title': 'blog 3 Odoo',
        'content': 'odoo project',
        'date_posted': 'April 22, 2024'
    },
    {
        'author':  'Joy',
        'title': 'blog 4 Odoo',
        'content': 'odoo project',
        'date_posted': 'April 23, 2024'
    },
        {
        'author':  'Sarah',
        'title': 'blog 5 Kotlin',
        'content': 'Kotlin Basics',
        'date_posted': 'April 24, 2024'
    }
]




def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', {'title': "About"})

