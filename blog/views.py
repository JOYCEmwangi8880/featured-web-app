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
        'author':  'Myles',
        'title': 'blog 4 Data Science $ Analytics',
        'content': ' Basics',
        'date_posted': 'june 12, 2024'
    },
    {
        'author':  'LM',
        'title': 'blog 5 odoo',
        'content': ' Basics',
        'date_posted': 'june 15, 2024'
    },
    {
        'author':  'Evans',
        'title': 'blog 6 goolang',
        'content': ' Basics',
        'date_posted': 'june 18, 2024'
    },
    
    
   
    
    
    
    
   

    
    
   
    
        


]




def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', {'title': "About"})

