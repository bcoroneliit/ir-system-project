import pickle
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def process_query():
    data = request.get_json()
    
    # req: error-checking
    if 'query' not in data:
        return jsonify({'error': 'Query is missing'}), 400

    query = data.get('query')

    if not isinstance(query, str):
        return jsonify({'error': 'Query must be a string'}), 400

    if not query.strip():
        return jsonify({'error': 'Query cannot be empty'}), 400

    with open('inverted_index_titles.pkl', 'rb') as file:
        inverted_index = pickle.load(file)

    results = search(query, inverted_index)

    #req: top-k (5) results
    k = 5
    top_results = results[:k]

    return jsonify({'results': top_results})

def search(query, inverted_index):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(inverted_index.keys())
    query_vector = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)
    results = [(title, cosine_similarities[0, i]) for i, title in enumerate(inverted_index.keys())]
    return sorted(results, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    app.run(debug=True)
