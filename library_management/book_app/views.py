from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
class GoodMorningView(View):
    def get(self,request):
        data = {
            'Message': "Good Morning..!"
        }
        return JsonResponse(data)

class LibraryView(View):
    def get(self,request):
        data = {
            "Library" : "Central Library",
            "Location" : "Perumbavoor",
            "Status" : "Open",
            "Timing" : "10am - 5pm",
        }
        return JsonResponse(data)

class BookView(View):
    def get(self,request):
        data = {
            "Book_Name" : "Wing of fire",
            "Author" : "APJ Abdul Kalam",
            "Price" : 650,
            "Year" : "1960"
        }
        return JsonResponse(data)

class StudentView(View):
    def get(self,request):
        data = {
            "Name" : "Gokul",
            "Course" : "Python-Django",
            "Batch" : "June 2026",
            "Institute" : "LuminarTechnoLab",
            "Hobby" : "Coding"
        }
        return JsonResponse(data)

class BooksView(View):
    def get(self,request):
        data = {
            "Books" : [
                "django",
                "wings of fire",
                "python",
                "React",
                "Java",
                "Maths",
                "Web application"
            ]
        }
        return JsonResponse(data)

class EmployeeView(View):
    def get(self,request):
        data = {
            "id"            : 101,
            "Name"          : "Adith",
            "place"         : "Cochin",
            "Designation"   : "Full stack developer",
            "Contact"       : "9867102993",
            "Experiance"    : "5-Years",
            "Qualification" : "Diploma in AI"
        }
        return JsonResponse(data)