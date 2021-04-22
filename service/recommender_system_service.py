from flask import Flask
from ContentBasedRecommender import ContentBasedRecommender

app = Flask(__name__)

@app.route('/recommend/<string:userId>',methods=['get'])
def recommend_item(userId):
    stored_model = ContentBasedRecommender()
    x= stored_model.recommend_items(int(userId))
    return x.to_json(orient='records', lines=True)


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=5000)