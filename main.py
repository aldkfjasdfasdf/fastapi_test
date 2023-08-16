import json
import os
import httpx
from fastapi import FastAPI
from schemas import DynamicList
from utils import SortTime

app = FastAPI()


@app.get("/get-moscow-weather")
async def get_moscow_weather():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://wttr.in/Moscow?format=3")

        if response.status_code == 200:
            weather_data = response.text.split(" ")[-1].replace("\n", "")
            return {"Moscow-weather": weather_data}
        else:
            return {"error": "data retrieval failed"}
    except httpx.HTTPError:
        return {"error": "HTTP error"}


@app.post("/sort-time")
def sort_time(data: DynamicList):
    # print("{:.6f}".format(SortTime.bubble_sort(arr=arr.arr)[-1])) in milliseconds
    buble_sort_time = SortTime.bubble_sort(arr=data.arr.copy())[-1]
    quick_sort_time = SortTime.quick_sort(arr=data.arr.copy())[-1]
    book_sort_time = SortTime.book_sort(arr=data.arr.copy())[-1]
    alphabet_sort_time = SortTime.alphabet_sort(arr=data.arr.copy())[-1]
    result = {
        "buble-sort-time": buble_sort_time,
        "quick-sort-time": quick_sort_time,
        "book-sort-time": book_sort_time,
        "alphabet-sort-time": alphabet_sort_time,
    }
    return result


@app.post("/max-integer")
def max_integer(value: int):
    file_path = "data.json"

    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump({"value": value}, file)
        return {"max-value": value}

    with open(file_path, "r") as file:
        data = json.load(file)

    current_value = data["value"]
    if value > current_value:
        data["value"] = value
        with open(file_path, "w") as file:
            json.dump(data, file)
        return {"max-value": value}
    else:
        return {"max-value": current_value}
