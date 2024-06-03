import os
import re
import random
import pandas as pd
import xml.etree.ElementTree as ET

class Importer():
    """_summary_
    """
    def __init__(self) -> None:
        pass

    def abstract_names_function(self, path):
        """
        Lista todos los nombres de los archivos en el directorio especificado.

        Args:
        path (str): La ruta al directorio del que se quieren listar los archivos.

        Returns:
        list: Una lista con los nombres de todos los archivos en el directorio.
        """
        # Verificar si el directorio existe
        if not os.path.exists(path):
            return "El directorio no existe."
        
        # Obtener todos los archivos y subdirectorios en el directorio especificado
        nombres_de_archivos = [archivo for archivo in os.listdir(path) if os.path.isfile(os.path.join(path, archivo))]

        return nombres_de_archivos
    
    def abstract_sampler(self, full_list, prop=0.8):
        """
        Selecciona una muestra aleatoria de n elementos de una lista de strings.

        Args:
        full_list (list): La lista original de strings de la cual seleccionar la muestra.
        n (int): El número de elementos a seleccionar.

        Returns:
        list: Una lista con n elementos seleccionados aleatoriamente de la lista original.
        """
        # Definir proporcion
        self.n = int(len(full_list)*prop)

        # Verificar si n es mayor que la longitud de la lista
        if self.n > len(full_list):
            return "Error: n es mayor que el número de elementos en la lista."
        
        # Seleccionar n elementos aleatorios de la lista
        muestra_seleccionada = random.sample(full_list, self.n)
        
        return muestra_seleccionada
    
    def extract_data(self, file_path):
        """Función para extraer los datos relevantes de un archivo XML

        Args:
            file_path (arr): array con los nombres de los archivos en string

        Returns:
            _dict_: devuelve un diccionario con el titulo y el resumen del archivo
        """
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extraer información básica
        title = root.find('.//AwardTitle').text if root.find('.//AwardTitle') is not None else "No Title"
        abstract = root.find('.//AbstractNarration').text if root.find('.//AbstractNarration') is not None else "No Abstract"
        
        return {
            "title": title,
            "abstract": abstract
        }
    
    def clean_text(self, text): 
        """Función para limpiar el texto de los resúmenes

        Args:
            text (str): String con el texto a transformar

        Returns:
            str: Texto transformado
        """
        if pd.isna(text):
            return ""  # Retorna un string vacío si el texto es NaN

        # Eliminar etiquetas HTML
        text = re.sub(r'<[^>]+>', '', text)
        # Eliminar caracteres especiales y números
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convertir a minúsculas
        text = text.lower()
        # Eliminar espacios adicionales
        text = re.sub(r'\s+', ' ', text).strip()

        return text