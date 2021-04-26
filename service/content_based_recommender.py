from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle
import os

class ContentBasedRecommender:
    MODEL_NAME = 'Content-Based'
    user_profiles = None
    tfidf_matrix = None
    item_ids = None
    model=None

    def __init__(self, items_df=None):
        # self.item_ids = item_ids
        self.items_df = items_df
        dirname = os.path.dirname(__file__)
        self.user_profiles = pickle.load(open(os.path.join(dirname, 'user_profiles.p'), "rb"))
        self.tfidf_matrix = pickle.load(open(os.path.join(dirname, 'tfidf_matrix.p'), "rb"))
        self.item_ids = pickle.load(open(os.path.join(dirname, 'item_ids.p'), "rb"))
        self.model = pickle.load(open(os.path.join(dirname, 'content_based_recommender_model.p'), "rb"))


    def get_model_name(self):
        return self.MODEL_NAME

    def _get_similar_items_to_user_profile(self, person_id, topn=10):
        # Computes the cosine similarity between the user profile and all item profiles
        cosine_similarities = cosine_similarity(self.user_profiles[person_id], self.tfidf_matrix)
        # Gets the top similar items
        similar_indices = cosine_similarities.argsort().flatten()[-topn:]
        # Sort the similar items by similarity
        similar_items = sorted([(self.item_ids[i], cosine_similarities[0, i]) for i in similar_indices],
                               key=lambda x: -x[1])
        return similar_items

    def recommend_items(self, user_id, items_to_ignore=[], topn=10, verbose=False):
        similar_items = self._get_similar_items_to_user_profile(user_id)
        # Ignores items the user has already interacted
        similar_items_filtered = list(filter(lambda x: x[0] not in items_to_ignore, similar_items))

        recommendations_df = pd.DataFrame(similar_items_filtered, columns=['contentId', 'recStrength']) \
            .head(topn)

        if verbose:
            if self.items_df is None:
                raise Exception('"items_df" is required in verbose mode')

            recommendations_df = recommendations_df.merge(self.items_df, how='left',
                                                          left_on='contentId',
                                                          right_on='contentId')[
                ['recStrength', 'contentId', 'title', 'url', 'lang']]

        return recommendations_df
