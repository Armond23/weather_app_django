from django.shortcuts import render
from django.views import View
import urllib.request
import json

class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    
    def post(self, request):
            city = request.POST['city']
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=090c5108a91c925432a7bbe9c8c4d990').read()
            
            list_of_data = json.loads(source)
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', '
                + str(list_of_data['coord']['lat']),

                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }
            print(data)
            return render(request, "home/index.html", data)
