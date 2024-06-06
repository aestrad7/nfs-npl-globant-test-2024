# Abstracts Segmentation

1. This repository contains an exercise in segmenting abstracts (summaries) using two different approaches:
   1. TF-IDF (Term Frequency-Inverse Document Frequency) with KMeans
   2. OpenAI embeddings obtained through their API and KMeans

- ## Project Structure

  - `src/`
    - `data/`: Contains scripts for data loading and preprocessing.
    - `features/`: Contains scripts for feature extraction.
    - `models/`: Contains scripts for model construction and evaluation.
    - `utils/`: Contains utility functions used in different parts of the project.
  - `data/`: Directory where input data is stored.
  - `notebooks/`: Contains Jupyter notebooks with exploratory analysis and model testing.
  - `requirements.txt`: File with the project dependencies.
  - `README.md`: This file.

## Requirements

To install the necessary dependencies for this project, use the `requirements.txt` file. You can install them with the following command:

```
bash
Copiar código
pip install -r requirements.txt
```

## Data

The `data/` directory should contain the necessary data files for the project. Ensure that the data is preprocessed and ready to be used in the models.

## Methodology

### Approach 1: TF-IDF with KMeans

1. **Preprocessing**: The texts of the abstracts are tokenized, and stopwords are removed.
2. **Vectorization**: TF-IDF is used to convert the texts into numerical vectors.
3. **Clustering**: KMeans is applied to group the abstracts into different clusters.

### Approach 2: OpenAI Embeddings with KMeans

1. **Obtain Embeddings**: The OpenAI API is used to obtain embeddings of the texts of the abstracts.
2. **Clustering**: KMeans is applied to the obtained embeddings to group the abstracts into different clusters.

## Usage

### Data Preprocessing

```
from importer import Importer

imp = Importer()
archivos_full = imp.abstract_names_function(path)
muestra = imp.abstract_sampler(archivos_full)
```

### Feature Extraction

For TF-IDF:

```
tfidf_vectorizer = TfidfVectorizer(max_df=0.8, min_df=3, max_features=3323, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(df_abstracts['clean_abstract'])
```

For OpenAI Embeddings:

```
titles = df['clean_abstract'].tolist()
embeddings = [embeddings_model.embed_query(title) for title in titles]
```

### Clusters

| Cluster | Title | Description | Most Valuable Words |
| ------- | ----- | ----------- | ------------------- |
|         |       |             |                     |

| Cluster 0 | Environment and Ecosystem Studies | This set of papers focuses on topics related to the environment, climate change, and ecosystems, especially in Arctic and marine regions. The studies address environmental processes, the impact of climate change, and the understanding of ecosystems. | new, study, students, soil, plant |
| --------- | --------------------------------- | ------------------------------------------------------------ | --------------------------------- |
|           |                                   |                                                              |                                   |

| Cluster 1 | Mathematics and Theoretical Models | This set focuses on mathematical models, algebraic applications, and geometric analysis. The studies may involve advanced mathematical theories and their application in science and technology. | matter, models, galaxies, students, mathematics |
| --------- | ---------------------------------- | ------------------------------------------------------------ | ----------------------------------------------- |
|           |                                    |                                                              |                                                 |

| Cluster 2 | Material Physics and Quantum Science | Papers on magnetic properties, quantum entanglement, and the behavior of materials at the quantum level. The studies explore devices and fundamental physical phenomena. | dots, magnetic, science, light, electrons |
| --------- | ------------------------------------ | ------------------------------------------------------------ | ----------------------------------------- |
|           |                                      |                                                              |                                           |

| Cluster 3 | Computer Science and IT | Focused on software development, data analysis, networks, and algorithms. The works cover the design of computational systems and learning methods. | software, science, analysis, develop, computing |
| --------- | ----------------------- | ------------------------------------------------------------ | ----------------------------------------------- |
|           |                         |                                                              |                                                 |

| Cluster 4 | Health and Biomedical Sciences | This set addresses the development of treatments for diseases, studies on viruses, and innovation in medical devices. Topics related to the pandemic and public health are highlighted. | develop, disease, virus, detection, device |
| --------- | ------------------------------ | ------------------------------------------------------------ | ------------------------------------------ |
|           |                                |                                                              |                                            |

| Cluster 5 | Education and Pedagogical Practices | Papers on teaching methods, educational experiences, and professional development in university contexts. The studies include both science teaching and the development of educational programs. | teaching, practices, experiences, undergraduate, university |
| --------- | ----------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
|           |                                     |                                                              |                                                             |

| Cluster 6 | Material Science and Chemistry | Focused on the design and understanding of molecular structures, proteins, and chemical materials. The studies include research on energy, chemical materials, and cells. | design, manufacturing, protein, fundamental, structures |
| --------- | ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------- |
|           |                                |                                                              |                                                         |