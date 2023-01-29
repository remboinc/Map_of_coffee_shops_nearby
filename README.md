# Map generator with coffee shop addresses
User enters their current address, and the application shows the five nearest coffee shops on the map.
    
```
Введите свой адрес: Красная площадь
Ваши координаты:  ['37.621202', '55.753544']
   * Serving Flask app 'map'
   * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:5000
   * Running on http://192.168.1.8:5000
Press CTRL+C to quit
```
![image](https://user-images.githubusercontent.com/58534082/215354720-205a8a73-7d14-42df-897d-b08239b1dd94.png)

## How to start
Clone the project:
```
git clone https://github.com/remboinc/Map_of_coffee_shops_nearby
```
Create a virtual environment on directory project:
```
python3.10 -m venv env
```
Start virtual environment:
```
.env/bin/activate
```
Before start to deploy install requirements:
```
pip install -r requirements.txt
```
You need to create an `.env` file, get your API token on the [Yandex website](https://developer.tech.yandex.ru/services/) and insert it into the APIKEY variable in the `.env` file.

To run the script, enter the command:
```
python map.py
```
