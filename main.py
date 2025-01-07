import cohere
import sqlite3

def peticion_busqueda_libros(prompt):
    # Configura la API Key
    API_KEY = "QR1kux6RQUCRRol2rngWNIOV8fchdaXjrMt00D0K"
    co = cohere.Client(API_KEY)

    # Mensaje de entrada
    prompt = f"En el siguiente texto encuentra los titulos de libros: $$${prompt}$$$ El formato de salida debe ser el siguiente: Autor - Titulo del libro, solamente debe ser ese formato de salida, no quiero ninguna otra cosa en la respuesta, si no hay me lo dejas saber, Por ejemplo 1. Immanuel Kant - Crítica a la razón pura"

    # Genera una respuesta con el modelo de Cohere
    return co.generate(
        model='command-xlarge-nightly',  # Modelo gratuito (puede variar según el plan)
        prompt=prompt,
        max_tokens=50,  # Limita la longitud de la respuesta
        temperature=0.7,  # Controla la creatividad de la respuesta
    )

def conexion_db(nombre_archivo):
    # Aquí conectamos a la base de datos y extraemos los libros
    conn = sqlite3.connect(nombre_archivo)
    return conn

def obtener_descripciones_db(conn):
    """
    Extrae las descripciones de los episodios desde la base de datos.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT description FROM episodio")  # Selecciona solo la columna 'description'
    descripciones = cursor.fetchall()
    return descripciones  # Devuelve una lista con las descripciones


def main():
    conexion = conexion_db('Db_filosofia_de_bolsillo_libros_spotify.db')
    episodios = obtener_descripciones_db(conexion)
    
    # Itera sobre las descripciones y ejecuta la función
    for i, episodio in enumerate(episodios, start=1):
        try:
            # Llama a la API y guarda el resultado
            resultado = peticion_busqueda_libros(episodio)
            
            # Extrae los textos de cada generación
            texts = [generation.text for generation in resultado.generations]
            
            # Imprime los resultados
            for text in texts:
                print(text)
            print("\n")  # Salto de línea entre episodios
        except Exception as e:
            print(f"Error procesando el episodio {i}: {e}\n")



if __name__ == "__main__":
    main()