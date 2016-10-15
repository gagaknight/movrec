from os import path
import graphlab as gl

# Path to the dataset directory
data_dir = './data'

# Table of movies we are recommending: movieId, title, genres
items = gl.SFrame.read_csv(path.join(data_dir, 'movies.csv'))

# Table of interactions between users and items: userId, movieId, rating, timestamp
actions = gl.SFrame.read_csv(path.join(data_dir, 'ratings.csv'))

### Prepare Data ###

# Prepare the data by removing items that are rare
rare_items = actions.groupby('movieid', gl.aggregate.COUNT).sort('Count')
rare_items = rare_items[rare_items['Count'] <= 5]
items = items.filter_by(rare_items['movieid'], 'movieid', exclude=True)
actions = actions[actions['rating'] >=4 ]
actions = actions.filter_by(rare_items['movieid'], 'movieid', exclude=True)

training_data, validation_data = gl.recommender.util.random_split_by_user(actions, 'userid', 'movieid')

model = gl.recommender.create(training_data, 'userid', 'movieid',target="rating")

model.save("pretrained_model")

results = model.recommend(gl.SArray(data=[3]))

print results
