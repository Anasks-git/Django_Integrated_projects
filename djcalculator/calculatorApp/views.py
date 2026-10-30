from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
# Create your views here.
@method_decorator(csrf_exempt,name = "dispatch")
class AdditionView(View):
    def post(self,request):
        request_body = request.body

        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 + n2
        print(request_body)
        data = {
            "Sum" : result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class SubstractionView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 - n2
        print(request_body)
        data = {
            "Diffrence" : result 
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class MultiplicationView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 * n2
        print(request_body)
        data = {
            "Multiplication" : result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class DivisionView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 // n2
        print(request_body)
        data = {
            "Operation" : "Division",
            "Division" : result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class ModulusView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 % n2
        print(request_body)
        data = {
            "Operation" : "Modulus",
            "Modulus" : result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class BmiView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        height = form_data.get("height")
        height_in_meter = height/100
        weight = form_data.get("weight")
        bmi = weight/(height_in_meter**2)
        print(request_body)
        data = {
            "Height" : height_in_meter,
            "Weight" : weight,
            "BMI" : bmi
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class AgeView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        DOB_year = form_data.get("Birth_year")
        Year = form_data.get("Current_year")
        Age = Year - DOB_year
        print(request_body)
        data = {
            "Age" : Age
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = "dispatch")
class PercentageView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        mark = form_data.get("mark")
        Total_mark = form_data.get("total_mark")
        percentage =(mark/Total_mark)*100
        print(request_body)
        data = {
            "Percentage" : percentage
        }
        return JsonResponse(data)