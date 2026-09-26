import pickle
from pathlib import Path

import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors


APP_DIR = Path(__file__).resolve().parent


def main():
    medicines = pd.read_csv(APP_DIR / 'medicine.csv')
    medicines = medicines.dropna(subset=['Drug_Name', 'Description', 'Reason']).reset_index(drop=True)

    tags = (
        medicines['Description'].astype(str).str.split()
        + medicines['Reason'].astype(str).str.split()
    ).map(lambda words: ' '.join(words).lower())

    stemmer = PorterStemmer()
    tags = tags.map(lambda text: ' '.join(stemmer.stem(word) for word in text.split()))
    vectors = CountVectorizer(stop_words='english', max_features=5000).fit_transform(tags)

    neighbor_model = NearestNeighbors(metric='cosine', algorithm='brute', n_jobs=1)
    neighbor_model.fit(vectors)
    _, neighbor_indices = neighbor_model.kneighbors(vectors, n_neighbors=min(6, len(medicines)))
    recommendations = [
        [int(index) for index in row if index != medicine_index][:5]
        for medicine_index, row in enumerate(neighbor_indices)
    ]

    with (APP_DIR / 'medicine_records.pkl').open('wb') as medicine_file:
        pickle.dump(medicines[['Drug_Name']].to_dict(), medicine_file)
    with (APP_DIR / 'medicine_neighbors.pkl').open('wb') as neighbors_file:
        pickle.dump(recommendations, neighbors_file)


if __name__ == '__main__':
    main()