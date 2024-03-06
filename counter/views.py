from django.shortcuts import render
import requests , json
#Ub54IEjQVcN8XiJIMW3mCg==n1FIhf5hieOGsRf0
# Create your views here.
def home(request):
    if request.method == "POST":
        query = request.POST["query"]
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-key': 'Ub54IEjQVcN8XiJIMW3mCg==n1FIhf5hieOGsRf0'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "Error..."
            print(e)
        return render(request, "home.html",{'api': api})
    else:
        return render(request, "home.html",{'query:': "Enter a valid food item"})