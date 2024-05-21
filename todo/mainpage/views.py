
from django.shortcuts import render
def index(request):
    return render(
        request,                    # Запрос
      'mainpage/index.html',      # путь к шаблону
        #context                    # подстановки
    )
# Create your views here.
