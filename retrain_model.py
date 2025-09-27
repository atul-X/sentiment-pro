import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from text_utils import text_process
import logging
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load train and test data from archive
logging.info('Loading data...')
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

# Split data for training and validation
logging.info('Splitting data into training and testing sets.')
X = all_df['review']
y = all_df['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorization
logging.info('Vectorizing text data...')
cv = TfidfVectorizer(tokenizer=text_process, max_features=5000, ngram_range=(1, 2))
x_train_vec = cv.fit_transform(X_train)
x_test_vec = cv.transform(X_test)

# Train model
logging.info('Training the model...')
model = LinearSVC(max_iter=1000)
model.fit(x_train_vec, y_train)

# Evaluate model
logging.info('Evaluating the model...')
predictions = model.predict(x_test_vec)
accuracy = accuracy_score(y_test, predictions)
logging.info(f'Model accuracy: {accuracy:.4f}')

# Save model and vectorizer with versioning and as latest
if accuracy > 0.7:  # Threshold set to 70%
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_filename = f'Model_{timestamp}.pickle'
    cv_filename = f'cv_{timestamp}.pickle'

    logging.info(f'Saving versioned model: {model_filename}')
    with open(model_filename, 'wb') as f:
        pickle.dump(model, f)
    with open(cv_filename, 'wb') as f:
        pickle.dump(cv, f)

    logging.info('Saving model as latest for the app.')
    with open('Model.pickle', 'wb') as f:
        pickle.dump(model, f)
    with open('cv1', 'wb') as f:
        pickle.dump(cv, f)

    logging.info('Model and vectorizer retrained and saved successfully.')
else:
    logging.warning(f'New model accuracy ({accuracy:.4f}) is below the threshold of 0.7. Model not saved.')
