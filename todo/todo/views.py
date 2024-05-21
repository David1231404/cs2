from django.shortcuts import render

def index(request):
    context = {
        'tasks':[
            {
                'done':False,
            }
        ]
    }
    return render(
        request,                   # Запрос
      'tasklist/index.html',  # путь к шаблону
              
        context                    # подстановки
    )