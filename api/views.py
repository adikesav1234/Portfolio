from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class AboutView(View):
    def get(self,request):
        data={
            "id":1,
            "Full Name":"Adi Kesav M",
            "Professional Title":"Developer",
            "Bio":"A passionate developer",
            "DOB":"21-04-26",
            "Email":"adi1234@gmail.com",
            "Contact Number":"9872354667",
            "Location":"Angamaly",
            "Github Url":"https://github.com/adi-kesav",
            "LinkedIn Url":"https://linkedin.com/in/adi-kesav"
        }
        return JsonResponse(data)

class EducationView(View):
    def get(self,request):
        data={
            "ID":1,
            "Institution":"MGAJ",
            "Degree/Course":"BCA",
            "University":"MGU",
            "Location":"Paravur",
            "Start_Year":"2023",
            "End_Year":"2026",
            "Grade_or_CGPA":"B+",
            "Description":"A passionate developer"
        }
        return JsonResponse(data)

class ProjectView(View):
    def get(self,request):
        data=[
            {
                "id":1,
                "title":"DietLense",
                "short_description":"long_description",
                "technologies_used":["Python","Django","Google GenAI SDK"],
                "live_url":"https://dietlens.example.com",
                "github_url":"https://github.com/yourusername/dietlens",
                "image_url":"https://api.yourdomain.com/media/projects/dietlense",
                "featured":True
            },
            { 
                "id":2,
                "title":"xxx",
                "short_description":"xxx_description",                
                "technologies_used":["x","x","Google GenAI SDK"],
                "live_url":"https://dietlens.example.com",
                "github_url":"https://github.com/yourusername/dietlens",
                "image_url":"https://api.yourdomain.com/media/projects/dietlense",
                "featured":True
            },
            {
                "id": 3,
                "title": "Blood Donor Management",
                "short_description": "A web application to manage blood donor information",
                "technologies_used": ["Python", "Django", "MySQL"],
                "live_url": "https://blooddonor.example.com",
                "github_url": "https://github.com/yourusername/blood-donor-management",
                "image_url": "https://api.yourdomain.com/media/projects/blooddonor",
                "featured": True
            },
            {
                "id": 4,
                "title": "Gym Management System",
                "short_description": "A system for managing gym members, plans and payments",
                "technologies_used": ["Python", "Django", "MySQL"],
                "live_url": "https://gymmanagement.example.com",
                "github_url": "https://github.com/yourusername/gym-management",
                "image_url": "https://api.yourdomain.com/media/projects/gymmanagement",
                "featured": False
            },
            {
                "id": 5,
                "title": "E-Commerce Website",
                "short_description": "An online shopping platform for browsing and purchasing products",
                "technologies_used": ["Python", "Django", "HTML", "CSS", "JavaScript"],
                "live_url": "https://ecommerce.example.com",
                "github_url": "https://github.com/yourusername/ecommerce",
                "image_url": "https://api.yourdomain.com/media/projects/ecommerce",
                "featured": True
            }
        ]
        return JsonResponse(data,safe=False)

class EmployeeView(View):
    def get(self,request):
        data=[
            {
                "ID":1,
                "Skille_name":"Python",
                "Category":"Programming Language",
                "Proficiency":"Advanced",
                "years_of_experience":4
            },
            {
                "ID":2,
                "Skille_name":"Django",
                "Category":"Backend",
                "Proficiency":"Advanced",
                "years_of_experience":5
            },
            {
                "ID":3,
                "Skille_name":"Framework",
                "Category":"Frontend",
                "Proficiency":"Advanced",
                "years_of_experience":2
            }
        ]
        return JsonResponse(data,safe=False)

class ExperienceView(View):
    def get(self, request):
        data = [
            {
                "ID": 1,
                "Job_Title": "Software Developer",
                "Company_name": "Infosys",
                "Location": "Kakkanad",
                "Employment_Type": "Remote",
                "Start_Date": "2025-10-10",
                "End_Date": "2027-10-10",
                "Currently_Working": "Yes",
                "Description": "Currently working as a Software Developer"
            },
            {
                "ID": 2,
                "Job_Title": "Python Programmer",
                "Company_name": "Wipro",
                "Location": "Kochi",
                "Employment_Type": "Remote",
                "Start_Date": "2024-06-10",
                "End_Date": "2025-09-10",
                "Currently_Working": "No",
                "Description": "Worked on Python-based applications and backend development"
            },
            {
                "ID": 3,
                "Job_Title": "Python Intern",
                "Company_name": "Envigo Technologies",
                "Location": "Calicut",
                "Employment_Type": "Internship",
                "Start_Date": "2026-05-01",
                "End_Date": "2026-05-31",
                "Currently_Working": "No",
                "Description": "Worked on AI automation and AI agent related projects"
            }
        ]

        return JsonResponse(data, safe=False)

class CertificateView(View):
    def get(self, request):
        data = [
            {
                "ID": 1,
                "Certificate_name": "Python Full Stack Development",
                "issueing organization": "Luminar Technolab",
                "Issued date": "2026-09-20"
            },
            {
                "ID": 2,
                "Certificate_name": "Python Programming",
                "issueing organization": "Udemy",
                "Issued date": "2026-08-15"
            },
            {
                "ID": 3,
                "Certificate_name": "Web Development Fundamentals",
                "issueing organization": "Coursera",
                "Issued date": "2026-07-10"
                
            }
        ]

        return JsonResponse(data, safe=False)

class ServiceView(View):
    def get(self, request):
        data = [
            {
                "id": 1,
                "service name": "Web Development",
                "description": "Building responsive and user-friendly web applications",
                "technologies": ["Python", "Django", "HTML", "CSS", "JavaScript"]
            },
            {
                "id": 2,
                "service name": "Database Management",
                "description": "Designing and managing databases for web applications",
                "technologies": ["MySQL", "SQL", "Django ORM"]
            },
            {
                "id": 3,
                "service name": "API Development",
                "description": "Creating and integrating APIs for web and mobile applications",
                "technologies": ["Python", "Django", "REST API", "JSON"]
            },
            {
                "id": 4,
                "service name": "Backend Development",
                "description": "Developing secure and scalable server-side applications",
                "technologies": ["Python", "Django", "MySQL"]
            },
            {
                "id": 5,
                "service name": "AI Integration",
                "description": "Integrating AI capabilities into modern applications",
                "technologies": ["Python", "Google GenAI SDK", "Django"]
            }
        ]

        return JsonResponse(data, safe=False)



