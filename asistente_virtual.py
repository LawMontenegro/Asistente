import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
# import yfinance as yf
import wikipedia

# Escucha el microfono y devuelve el texto del audio



# Declara id de voces
    
id_1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'

id_2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    
    

# Declaracion de lista de dias de la semana
semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']    
    
    

def transformar_audio_texto():
    # almacena reconocedor
    
    reconocedor = sr.Recognizer()
    
    # Comfiguracion el microfono
    
    with sr.Microphone() as origen:
        
        # Tiempo de espera
        reconocedor.pause_thereshold = 0.8
        
        # Aviso de comienzo de grabacion
        print('ya puedes hablar')
        
        # Guarda audio
        
        audio = reconocedor.listen(origen)
        
        try:
            # Buscar en GO
            solicitud = reconocedor.recognize_google(audio, language="es-co")
            
            
            # Prueba de ingreso
            print("has dicho:  " + solicitud)
            
            # Devolver 
            return solicitud
        
        except sr.UnknownValueError:
            # Prueba de que no comprendio
            print('Ups, no entendí')
            
            # Devolver Error
            
            return "Sigo Esperando"
        
        except sr.RequestError as e:
            # Error: No se puede obtener respuesta del servicio
            print("No se puede obtener respuesta del servicio; {0}".format(e))
            return None
        
        # Error inesperado
        
        except:
            # Prueba 
            print("Ups, algo salio mal")
            
            # Devolver error
            
            return "sigo esperando"
        
        
def hablar_asistente(mensaje):
    # Encender el motor de pyttsx3
    
    engine = pyttsx3.init()
    
    
    # Fijar voces de Asistente
    
    engine.setProperty('voice', id_1)
    
    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()
    
    
def solicitar_dia():
    
    # crear varible de datos de hoy
    
    dia = datetime.date.today()
    
    # crear una variable dia de la semana
    dia_semana = dia.weekday()
    
    
    
    
    # Declaracion nombre de la semana
    semana = {0:'Lunes',
              1:'Martes' , 
              2:'Miércoles', 
              3:'Jueves',
              4:'Viernes',
              5:'Sábado',
              6:'Domingo'}
    
    # Frase del dia de la semana
    hablar_asistente(f'Hoy es {semana[dia_semana]}')


def solicitar_hora():
     
     # variable de hora

    hora = datetime.datetime.now().time()
    hora_formateada = hora.strftime("%H:%M:%S")
    hablar_asistente(f'En este momento son las  {hora_formateada}')
        
        
def saludo_inicial():
    
    # declara dato de hora
    
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour >= 20 :
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 12 :
        momento = 'Buenos dias'
    else:
        momento = 'Buenas tardes'
    
    
    
    # saludar
    hablar_asistente(f'{momento}. Hola soy luz!. tu asistente personal, por favor dime en que te puedo ayudar')


def solicitudes():
    # Activar sonido
    saludo_inicial()
    
    # Variable de corte
    comenzar = True
    while  comenzar:
        
        # Activar el micro y guarda la solicitus en str
        solicitud = transformar_audio_texto().lower()
        
        
        if 'abrir youtube' in solicitud:
            hablar_asistente('Con gusto, estoy ariendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir google' in solicitud:
            hablar_asistente('Con gusto, estoy en eso, google no?')
            webbrowser.open('https://www.google.com')
            continue
        elif 'gracias' in solicitud:
            hablar_asistente('aaw ~ no me digas gracias desgraciado')
            continue
        elif 'qué hora es' in solicitud:
            solicitar_hora()
            continue
        elif 'tienes agua' in solicitud:
            hablar_asistente('No baja y sirve un poc de agua, y no olvides la sal')
            continue
        elif 'qué día es hoy' in solicitud:
            solicitar_dia()
            continue
        elif 'ver anime' in solicitud:
            hablar_asistente('con gusto, yo me encargo')
            webbrowser.open('https://ww3.animeonline.ninja')
            continue
        elif 'busca en wikipedia' in solicitud:
            hablar_asistente('con gusto, buscando en wikipedia')
            solicitud = solicitud.replace('busca en wipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(solicitud, sentences=1)
            hablar_asistente('Wikipedia dice lo siguiente:')
            hablar_asistente(resultado)
            continue               
        elif 'busca en internet' in solicitud:
            hablar_asistente('ya mismo estoy en eso')
            solicitud = solicitud.replace('buscar en internet', '')
            pywhatkit.search(solicitud)
            hablar_asistente('Esto es lo que he encotrado')
            continue
        elif 'reproducir' in solicitud:
            hablar_asistente(' exelente idea, ahora mismo voy a reproducir')
            pywhatkit.playonyt(solicitud)
            continue
        elif 'broma' in solicitud:
            hablar_asistente(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in solicitud:
            accion = solicitud.split('de')[-1].strip()
            cartera = {'apple' : 'APPL',
                       'amazon': 'AMZN',
                       'google' : 'GOOGL'}
            
            try:
                accion_buscada = cartera[accion]
                accion_buscada  = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarkertPrice']
                hablar_asistente(f'La encontre. el precio de la accion {accion} es {precio_actual}')    
                continue
            except:
                hablar_asistente(f'Lo siento no logre encontra el precia de la accion. {solicitud}')    
                continue    

        elif 'adiós' in solicitud:
            hablar_asistente('Me voy a descansar, cualquier cosa me avisas')
            break

# transformar_audio_texto()
# hablar_asistent
# saludo_inicial()
# e('Hola marcela. Espero que tengas un gran dia')
# solicitar_dia()
solicitudes()
