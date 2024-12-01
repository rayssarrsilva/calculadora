from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
    result = ''
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operator = request.POST.get('operator')

        if num1 and num2 and operator:
            try:
                num1 = float(num1)
                num2 = float(num2)

                if operator == 'add':
                    result = num1 + num2
                elif operator == 'subtract':
                    result = num1 - num2
                elif operator == 'multiply':
                    result = num1 * num2
                elif operator == 'divide':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = 'Erro: Divisão por zero'
            except ValueError:
                result = 'Erro: Entrada inválida'

    return render(request, 'calculadora/calculadora.html', {'result': result})
