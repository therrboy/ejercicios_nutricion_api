import os
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 130
HEIGHT = 183
AGE = 29


APP_ID = os.environ["OWM_APP_ID"]   # Variable de entorno por datos sensibles, se declaran en la configuracion de PYCHARM
APP_KEY = os.environ["OWM_APP_KEY"]  # Variable de entorno por datos sensibles, se declaran en la configuracion de PYCHARM

# Podemos declarar mas facilmente en esta web: https://replit.com/@DobleR1/AttractiveUltimatePriorities#main.py

FINAL_WEB = "https://trackapi.nutritionix.com/v2/natural/exercise"  # Pagina principal mas pagina de ejercicios
WEB_PROJECT_POST_AND_GET = "https://api.sheety.co/4042edcc990d0e0ce71d8420255ff63e/trabajo38/workouts"  # Con mis datos

exercise_input = str(input("Que ejercicio hiciste hoy? "))  # Datos sobre el ejercicio que vamos a hacer

header = {  # Datos de cabecera con ID y LLAVE
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

bearer_header = {
    "Authorization": "Bearer jadlasjjksajkd1203123120"    # Variable de entorno por datos sensibles

}

parametros = {  # Parametros que paso al programa para que haga calculos
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE
}

respuesta = requests.post(url=FINAL_WEB, json=parametros, headers=header)
respuesta.raise_for_status()
data_ejercicio = respuesta.json()["exercises"][0]

dia_hoy = datetime.now().strftime("%d/%m/%Y")
hora_actual = datetime.now().strftime("%X")

tabla_datos = {
    "workout": {
          "date": dia_hoy,
          "time": hora_actual,
          "exercise": data_ejercicio["name"].title(),
          "duration": data_ejercicio["duration_min"],
          "calories": data_ejercicio["nf_calories"]
        }
    }



ingresar_datos = requests.post(url=WEB_PROJECT_POST_AND_GET, json=tabla_datos, headers=bearer_header)
ingresar_datos.raise_for_status()