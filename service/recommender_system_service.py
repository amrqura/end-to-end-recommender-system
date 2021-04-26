from flask import Flask
from content_based_recommender import ContentBasedRecommender

app = Flask(__name__)

@app.route('/recommend/<string:userId>',methods=['get'])
def recommend_item(userId):
    stored_model = ContentBasedRecommender()
    result = stored_model.recommend_items(int(userId))
    return result.to_json(orient='records', lines=True)


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5000)