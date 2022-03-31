from ast import operator
from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
import random

# Create your views here.
def calculator(request):
    # return HttpResponse("계산기 기능 구현 시작입니다. 이거 맞아?")
    # print(f'request = {request}')
    # print(f'request type = {type(request)}')
    # print(f'request.__dict__ = {request.__dict__}')
    
    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operator')
    
    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
    
    # 3. 응답
    return render(request, 'calculator.html', {'result':result})

def lotto(request):
    lotto_number = list()
    if request.method == "POST":
        while len(lotto_number) < 7:
            number = random.randint(1, 45)
            if not number in lotto_number:
                lotto_number.append(number)
            else:
                continue
        
        return render(request, 'lotto.html', {'lotto_number':lotto_number})
    return render(request, 'lotto.html')


def lotto_index(request):
    return render(request, 'lotto_index.html')

def lotto_result(request):
    count = request.GET.get('count')
    print(type(count))
    pull_number = list()
    for i in range(int(count)):
        lotto_number = list()
        while len(lotto_number) < 7:
            number = random.randint(1, 45)
            if not number in lotto_number:
                lotto_number.append(number)
            else:
                continue
        pull_number.append(lotto_number)
    return render(request, 'lotto_result.html', {'pull_number':pull_number, 'count':count})