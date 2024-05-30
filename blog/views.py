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
        'author':  'joy',
        'title': 'blog 4 Odoo',
        'content': 'odoo project',
        'date_posted': 'April 23, 2024'
    },
    {
        'author':  'annita',
        'title': 'blog 5 Machine learning',
        'content': ' project',
        'date_posted': 'May 21, 2024'
    },
    {
        'author':  'myles',
        'title': 'blog 6 Machine learning',
        'content': ' project',
        'date_posted': 'May 22, 2024'
    },
    {
        'author':  'qoey',
        'title': 'blog 7 Machine learning',
        'content': ' project',
        'date_posted': 'May 23, 2024'
    },
    
   

    
    
   
    
        


]




def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', {'title': "About"})

