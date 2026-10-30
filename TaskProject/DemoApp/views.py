from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name = "dispatch")
class FactorialView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        num1 = form_data.get("num1")
        fact = 1
        for i in range(1,num1+1):
            fact *= i
        data = {
            "Factorial" : fact
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class SimpleintrestView(View):
    def post(self,request):
        request_body = request.body
        data = loads(request_body)
        p = data.get("p")
        t = data.get("t")
        r = data.get("r")
        intrest = (p*t*r)/100
        data = {
            "Principal" : p,
            "rate" : r,
            "time" : t,
            "Simple-Intrest" : intrest
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class DscountCalculatorView(View):
    def post(self,request):
        body = request.body
        form_data = loads(body)
        price = form_data.get("price")
        discount_perecent = form_data.get("discount_percent")
        discount_price = (discount_perecent/100)*price
        final_price = price - discount_price
        data = {
            "price" : price,
            "Discount_percentage" : discount_perecent,
            "Discount_price" : discount_price,
            "Final_price" : final_price
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class ProfitCalculatorView(View):
    def post(self,request):
        body = request.body
        form_data = loads(body)
        cost = form_data.get("cost")
        sell = form_data.get("selling")
        profit = sell - cost
        data = {
            "Cost_Price" : cost,
            "Selling_Price" : sell,
            "Profit" : profit
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class NetsalaryView(View):
    def post(self,request):
        body = request.body
        form_data = loads(body)
        salary = form_data.get("salary")
        bonus = form_data.get("bonus")
        deduction = form_data.get("deduction")
        Net_salary = (salary+bonus)-deduction
        data = {
            "Basic_salary" : salary,
            "Bonus" : bonus,
            "Deduction" : deduction,
            "Net_salary" : Net_salary
        }
        return JsonResponse(data)