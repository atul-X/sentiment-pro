import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from text_utils import text_process

# Load train and test data from archive
train_df = pd.read_csv('archive/drugsComTrain_raw.csv')
test_df = pd.read_csv('archive/drugsComTest_raw.csv')

# Combine for more data
all_df = pd.concat([train_df, test_df], ignore_index=True)

# Drop rows with missing reviews or ratings
all_df = all_df.dropna(subset=['review', 'rating'])

# Label sentiment based on rating
# >=8: positive, <=4: negative, else neutral
def label_sentiment(rating):
    if rating >= 8:
        return 'positive'
    elif rating <= 4:
        return 'negative'
    else:
        return 'neutral'

all_df['sentiment'] = all_df['rating'].apply(label_sentiment)

# Vectorization
cv = CountVectorizer(analyzer=text_process, max_features=5000)
x = cv.fit_transform(all_df['review'])
y = all_df['sentiment']

# Train model
model = MultinomialNB()
model.fit(x, y)

# Save model and vectorizer
with open('Model.pickle', 'wb') as f:
    pickle.dump(model, f)
with open('cv1', 'wb') as f:
    pickle.dump(cv, f)

print('Model and vectorizer retrained and saved.')
