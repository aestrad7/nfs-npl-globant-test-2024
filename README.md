# Segmentación de Abstracts

Este repositorio contiene un ejercicio de segmentación de abstracts (resúmenes) utilizando dos enfoques diferentes:

1. TF-IDF (Term Frequency-Inverse Document Frequency) con KMeans.
2. Embeddings de OpenAI obtenidos a través de su API y KMeans.

## Estructura del Proyecto

- `src/`
  - `data/`: Contiene los scripts para la carga y preprocesamiento de los datos.
  - `features/`: Contiene los scripts para la extracción de características.
  - `models/`: Contiene los scripts para la construcción y evaluación de los modelos.
  - `utils/`: Contiene funciones de utilidad que se utilizan en diferentes partes del proyecto.
- `data/`: Directorio donde se almacenan los datos de entrada.
- `notebooks/`: Contiene los notebooks Jupyter con análisis exploratorio y pruebas de los modelos.
- `requirements.txt`: Archivo con las dependencias del proyecto.
- `README.md`: Este archivo.

## Requisitos

Para instalar las dependencias necesarias para este proyecto, utiliza el archivo `requirements.txt`. Puedes instalarlas con el siguiente comando:

```
bash
Copiar código
pip install -r requirements.txt
```

## Datos

El directorio `data/` debe contener los archivos de datos necesarios para el proyecto. Asegúrate de que los datos estén preprocesados y listos para ser utilizados en los modelos.

## Metodología

### Enfoque 1: TF-IDF con KMeans

1. **Preprocesamiento**: Los textos de los abstracts se tokenizan y se eliminan las palabras vacías (stopwords).
2. **Vectorización**: Se utiliza TF-IDF para convertir los textos en vectores numéricos.
3. **Clustering**: Se aplica KMeans para agrupar los abstracts en diferentes clusters.

### Enfoque 2: Embeddings de OpenAI con KMeans

1. **Obtener Embeddings**: Se utiliza la API de OpenAI para obtener embeddings de los textos de los abstracts.
2. **Clustering**: Se aplica KMeans a los embeddings obtenidos para agrupar los abstracts en diferentes clusters.

## Uso

### Preprocesamiento de Datos

```
from importer import Importer

imp = Importer()
archivos_full = imp.abstract_names_function(path)
muestra = imp.abstract_sampler(archivos_full)
```

### Extracción de Características

Para TF-IDF:

```
tfidf_vectorizer = TfidfVectorizer(max_df=0.8, min_df=3, max_features=3323, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(df_abstracts['clean_abstract'])
```

Para Embeddings de OpenAI:

```
titles = df['clean_abstract'].tolist()
embeddings = [embeddings_model.embed_query(title) for title in titles]
```

### Clusters

| Cluster   | Título                                   | Descripción                                                  | Palabras más valiosas                                       |
| --------- | ---------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| Cluster 0 | Medio Ambiente y Estudios de Ecosistemas | Este conjunto de papers se centra en temas relacionados con el medio ambiente, el cambio climático y los ecosistemas, especialmente en regiones árticas y marinas. Los estudios abordan procesos ambientales, el impacto del cambio climático y la comprensión de los ecosistemas. | new, study, students, soil, plant                           |
| Cluster 1 | Matemáticas y Modelos Teóricos           | Este conjunto se enfoca en modelos matemáticos, aplicaciones algebraicas y análisis geométricos. Los estudios pueden involucrar teorías matemáticas avanzadas y su aplicación en la ciencia y la tecnología. | matter, models, galaxies, students, mathematics             |
| Cluster 2 | Física de Materiales y Ciencia Cuántica  | Papers sobre propiedades magnéticas, entanglement cuántico y el comportamiento de materiales a nivel cuántico. Los estudios exploran dispositivos y fenómenos físicos fundamentales. | dots, magnetic, science, light, electrons                   |
| Cluster 3 | Ciencia de la Computación y TI           | Enfocado en el desarrollo de software, análisis de datos, redes y algoritmos. Los trabajos tratan sobre el diseño de sistemas computacionales y métodos de aprendizaje. | software, science, analysis, develop, computing             |
| Cluster 4 | Salud y Ciencias Biomédicas              | Este conjunto aborda el desarrollo de tratamientos para enfermedades, estudios sobre virus y la innovación en dispositivos médicos. Se destacan temas relacionados con la pandemia y la salud pública. | develop, disease, virus, detection, device                  |
| Cluster 5 | Educación y Prácticas Pedagógicas        | Papers sobre métodos de enseñanza, experiencias educativas y desarrollo profesional en contextos universitarios. Los estudios incluyen tanto la enseñanza de ciencias como el desarrollo de programas educativos. | teaching, practices, experiences, undergraduate, university |
| Cluster 6 | Ciencia de Materiales y Química          | Concentrado en el diseño y la comprensión de estructuras moleculares, proteínas y materiales químicos. Los estudios incluyen investigaciones sobre energía, materiales químicos y células. | design, manufacturing, protein, fundamental, structures     |