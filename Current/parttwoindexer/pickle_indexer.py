from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load documents from output_file.txt
with open('paragraphs.txt', 'r', encoding='utf-8') as file:
    documents = file.readlines()

# Calculate TF-IDF scores
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Construct inverted index
terms = vectorizer.get_feature_names_out()
inverted_index = {}
for i, term in enumerate(terms):
    inverted_index[term] = [(j, tfidf_matrix[j, i]) for j in range(tfidf_matrix.shape[0]) if tfidf_matrix[j, i] > 0]

# Save the inverted index to a pickle file
with open('inverted_index.pkl', 'wb') as file:
    pickle.dump(inverted_index, file)

# Calculate cosine similarity between query and documents
def search(query):
    query_vector = vectorizer.transform([query])
    print("Query Vector:")
    print(query_vector)
    
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)
    print("Cosine Similarities Matrix:")
    print(cosine_similarities)
    
    results = [(documents[i], cosine_similarities[0, i]) for i in range(cosine_similarities.shape[1])]
    return sorted(results, key=lambda x: x[1], reverse=True)

# Example usage
query = "University"
results = search(query)
for result, similarity in results:
    print(f"Similarity: {similarity}\n{result}")

# Example usage
query = "University"
results = search(query)
for result, similarity in results:
    print(f"Similarity: {similarity}\n{result}")
