from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse 



# Create your views here.
class AboutView(View):
    def get(self,request):
        data = {
            "id" : 101,
            "Full Name" : "Anandhu Ashokan",
            "Professional title" : "Full-stack developer",
            "Bio" : "well knwoledge in python",
            "Dob" : "2005-12-02",
            "Email" : "Anandhu@gmail.com",
            "Contact NUmber" : 9403202038,
            "Location" : "Aluva",
            "GithubURL" : "githuB",
            "LinkedinURL" : "linkedin"
        }
        return JsonResponse(data)

class EducationView(View):
    def get(self,request):
        data = {
            "id" : 101,
            "Institution" : "Luminar",
            "Degree/Course" : "Ai",
            "University" : "MGU",
            "Location" : "Kochi",
            "start_year" : "2023",
            "End_year" : "2026",
            "Grade of CGPA" : 7,
            "Description" : "Loyal"
        }
        return JsonResponse(data)

class StudentView(View):
    def get(self,request):
        data = {
            "id" : 1,
            "Name" : "BasilPaul",
            "Place" : "Kochi",
            "Course" : "Python-fullstack",
            "DOB" : "2005-12-12",
            "Institute" : "Luminar"                                
        }
        return JsonResponse(data)

class ProjectsView(View):
    def get(self,request):
        data =  [
                {
                    "id" : 101,
                    "Title" : "First-Aid",
                    "Short_Description" : "First-Aid Description",
                    "Tech_Used" : ["python","Django","Google Gen AI"],
                    "Live URL" : "URL",
                    "Github URL" : "URL",
                    "Image URL" : "URL",
                    "Featured" : True                    
                },
                {
                    "id" : 102,
                    "Title" : "FootBox",
                    "Short_Description" : "FootBox Description",
                    "Tech_Used" : ["python","Django","Google Gen AI"],
                    "Live URL" : "URL",
                    "Github URL" : "URL",
                    "Image URL" : "URL",
                    "Featured" : True                    
                },
                {
                    "id" : 103,
                    "Title" : "Movie pox",
                    "Short_Description" : "MoviePox Description",
                    "Tech_Used" : ["python","Django","Google Gen AI"],
                    "Live URL" : "URL",
                    "Github URL" : "URL",
                    "Image URL" : "URL",
                    "Featured" : True                    
                }                               
            ]
        return JsonResponse(data,safe=False)

class SkillsView(View):
    def get(self,request):
        skills = [
            {
                "id" : 101,
                "Skil_name" : "Python",
                "Category" : "Programming Lnguage",
                "Proficiency" : "Advanced",
                "Year_od_Experiance" : "4-years"
            },
            {
                "id" : 102,
                "Skil_name" : "Django",
                "Category" :"Backend",
                "Proficiency" : "Advanced",
                "Year_od_Experiance" : "3-years"               
            },
            {
                "id" : 103,
                "Skil_name" : "React",
                "Category" : "Frontend",
                "Proficiency" : "Intermediate",
                "Year_od_Experiance" : "1-years"
            },
            {
                "id" : 104,
                "Skil_name" : "Java",
                "Category" : "programming Language",
                "Proficiency" : "Beginner",
                "Year_od_Experiance" : "6-Months"
            }
        ]
        return   JsonResponse(skills,safe = False)

class ExperianceView(View):
    def get(self,request):
        data = [
            {
                "ID" : 101,
                "Job_title" : "Software Developer",
                "Company Name" : "Infosys",
                "Location" : "Cochin",
                "Employement Type" : "Permanant",
                "Start Date" : "2022-12-10",
                "End Date" : "2023-12-10",
                "Currently Working" : "No",
                "Description" : "Well"
            },
            {
                "ID" : 102,
                "Job_title" : "Backend Developer",
                "Company Name" : "IBM",
                "Location" : "Kakkanad",
                "Employement Type" : "Remote",
                "Start Date" : "2023-12-10",
                "End Date" : "2024-12-10",
                "Currently Working" : "No",
                "Description" : "Well"
            },
            {
                "ID" : 103,
                "Job_title" : "Full-stack Developer",
                "Company Name" : "Luminar",
                "Location" : "Kakkanad",
                "Employement Type" : "Permanant",
                "Start Date" : "2023-12-10",
                "End Date" : "2026-12-10",
                "Currently Working" : "yes",
                "Description" : "Well"
            }

        ]
        return JsonResponse(data,safe=False)

class CertificateView(View):
    def get(self,request):
        data = [
            {
                "ID" : 101,
                "Certification Name" : "Front-End Developer",
                "Issuing Organization" : "ASSI",
                "Issued Date" : "2022-10-10",
            },
            {
                "ID" : 102,
                "Certification Name" : "Back-End Developer",
                "Issuing Organization" : "CCCAI",
                "Issuing Date" : "2025-19-17"
            },
            {
                "ID" : 103,
                "Certification Name" : "Full-stack Developer",
                "Issuing Organization" : "ASSIS",
                "Issuing Date" : "2026-12-10"
            }

        ]
        return JsonResponse(data,safe=False)

class ServicesView(View):
    def get(self,request):
        data = [
            {
                "ID" : 101,
                "Service Name" : "Web Apllication",
                "Description" : "Web developer since 2005",
                "Technologies" : ["Python","Django" , "React" ,"js"]
            },
            {
                "ID" : 102,
                "Service Name" : "DataBase Management",
                "Description " : "Database management since 2006",
                "Technologies":["Mysql","sqlite3","DBMS","Postegrelsql"]
            }
        ]
        return JsonResponse(data,safe = False)


