import cohere

# Configura la API Key
API_KEY = "QR1kux6RQUCRRol2rngWNIOV8fchdaXjrMt00D0K"
co = cohere.Client(API_KEY)

# Mensaje de entrada
prompt = "En el siguiente texto encuentra los titulos de libros: $$$ Nos despedimos de Platón con una gran ración de recomendaciones para leer y comentarios valiosos de los oyentes. Ahora sí, el gran Aristóteles aparece en Filosofía de Bolsillo y lo hace para quedarse. 📥 ¡Sin diálogo no hay pensamiento! Escríbeme mensajes en forma de dudas, sugerencias, propuestas para próximas ediciones, o simplemente lo que se te pase por la cabeza a correofilosofiadebolsillo@gmail.com así como a través de esta y otras RRSS como Twitter o Instagram. ➡️ Puedes seguir FILOSOFÍA DE BOLSILLO en las principales plataformas como Spotify, iVoox, Apple Podcasts, Google Podcasts o Youtube.$$$ El formato de salida debe ser el siguiente: Autor - Titulo del libro, solamente debe ser ese formato de salida, no quiero ninguna otra cosa en la respuesta, si no hay me lo dejas saber, Por ejemplo 1. Immanuel Kant - Crítica a la razón pura"

# Genera una respuesta con el modelo de Cohere
response = co.generate(
    model='command-xlarge-nightly',  # Modelo gratuito (puede variar según el plan)
    prompt=prompt,
    max_tokens=50,  # Limita la longitud de la respuesta
    temperature=0.7,  # Controla la creatividad de la respuesta
)

# Muestra la respuesta generada
print("Respuesta de la IA:", response.generations[0].text.strip())
