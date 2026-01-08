from fastapi import FastAPI
from fastapi import Query, HTTPException
from pydantic import BaseModel
import httpx, os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

class FavoriteLocation(BaseModel):
    city: str
    country:str
    nickname: str| None =None

@app.get("/weather/{city}")
async def get_weather(city:str, unit:str = "celsius", days:int = Query(default=3, le=14)): #le stands for less than

     #  
    api_key = os.getenv("OPENWEATHER_API_KEY", "YOUR_API_KEY_PLACEHOLDER")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    async with httpx.AsyncClient() as client:
       response = await client.get(url)
       
       #handles error from the external API
       if response.status_code != 200:
           raise HTTPException(status_code = response.status_code, detail="city not found or API error")

       data = response.json() #turn the response into a python dictonary
       
       if unit == "celsius":
           temp_kelvin = data.get("main", {}).get("temp") #ensures main exists
           
           if temp_kelvin:
               data["main"]["temp_celsius"] = round(temp_kelvin - 273.15, 2)
    return data

@app.post("/favorite")
def save_location(location: FavoriteLocation):
    return{"message": "saved", "data":location}

@app.get("/heatalert")
def get_temp_advice(temp: int):
    if temp > 35:
        return {"advice":"Stay hydrated"}
    elif temp < 0:
        return {"advice":"watch out for ice"}
    else:
        return{"advice": "enjoy"}


