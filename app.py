from flask import Flask, render_template, request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', book_name = popular_df['Book-Title'].values, author = popular_df['Book-Author'].values, image = popular_df['Image-URL-M'].values, votes = popular_df['num_ratings'].values, rating = popular_df['avg_ratings'].values)
@app.route('/reccomend')
def recommend_ui():
    return render_template('reccomend.html')
@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    if user_input not in pt.index:
        return render_template('reccomend.html', data = [])
        # fetch index
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]
    data = []
    for i in similar_items:
        item = []
        # Instead of creating a boolean Series, get the actual book title from pt.index
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        # Now temp_df has all the columns from the original books DataFrame
        item.extend(list(temp_df['Book-Title'].drop_duplicates().values))
        item.extend(list(temp_df['Book-Author'].drop_duplicates().values))
        item.extend(list(temp_df['Image-URL-M'].drop_duplicates().values)[:1])

        data.append(item)
    return render_template('reccomend.html', data = data)

if __name__ == '__main__':
    app.run(debug=True)