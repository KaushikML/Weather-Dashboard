import requests
API_KEY="137ce26912231af0f8dd68dbc825f163"

def get_data(place,forecast_days):

    url= f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid=137ce26912231af0f8dd68dbc825f163"
    response=requests.get(url)
    data=response.json()
    filtered=data["list"]
    nr_values=8*forecast_days

    filtered = filtered[:nr_values]


    return filtered

if __name__=="__main__":
    print(get_data(place="Tokyo",forecast_days=3))
