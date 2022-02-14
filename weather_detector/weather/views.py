from django.shortcuts import render, redirect
import json
import urllib.request


# Create your views here.
def index(request):
    if (request.method == 'POST'):
        city = request.POST['city']
        if (city):

            res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='
                                         + city + '&appid=1a86e99c48cca031cc32be6ce0883370').read()
            json_data = json.loads(res)
            data = {
                'country_code': str(json_data['sys']['country']),
                'coordinate': str(json_data['coord']['lat']) + ' ' +
                              str(json_data['coord']['lon']),
                'temp': str(round(int(json_data['main']['temp']) - 273.15, 0)) + ' C',
                'feels_like': str(round(int(json_data['main']['feels_like']) - 273.15, 0)) + ' C',
                'pressure': str(json_data['main']['pressure']),
                'humidity': str(json_data['main']['humidity']),
                'description': str(json_data['weather'][0]['description']),
            }
        else:
            redirect('http://127.0.0.1:8000/')
            data = {}
    else:
        data = {}
        city = ''
        redirect('http://127.0.0.1:8000/')
    return render(request, 'weather/index.html', {'city': city, 'data': data})
