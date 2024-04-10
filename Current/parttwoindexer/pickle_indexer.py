from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

input_file_path = 'raw_titles.txt'  
output_file_path = 'clean_titles.txt' 

# load docs from cleaned_titles
with open(input_file_path, 'r', encoding='utf-8') as file:
    titles = file.readlines()

# tf-idf vector
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(titles)

# creating inverted index
terms = vectorizer.get_feature_names_out()
inverted_index = {}
for i, term in enumerate(terms):
    inverted_index[term] = [(j, tfidf_matrix[j, i]) for j in range(tfidf_matrix.shape[0]) if tfidf_matrix[j, i] > 0]

# inverted index saved to pickle file
with open('inverted_index_titles.pkl', 'wb') as file:  
    pickle.dump(inverted_index, file)

# cosine similairty bw query and doc
def search(query):
    query_vector = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)
    results = [(titles[i], cosine_similarities[0, i]) for i in range(cosine_similarities.shape[1])]
    return sorted(results, key=lambda x: x[1], reverse=True)

# testing example
query = "University"
results = search(query)
for result, similarity in results:
    print(f"Similarity: {similarity}\n{result}")
