# import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.calibration import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import csv
import pickle
import re
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')


def preprocess(text):
    text = re.sub(r'\d+', '', text)  # Eliminar números
    text = re.sub(r'[,.\\-]', '', text)
    tokens = get_words(text)
    stop_words = get_lis_stopwords()
    filtered_tokens = get_words_without_stopwords(tokens, stop_words)
    lemmatized_tokens = get_words_lemanized(filtered_tokens)
    stemmed_tokens = get_words_stemmed(lemmatized_tokens)
    return ' '.join(stemmed_tokens)


def get_lis_stopwords():
    stop_words_spanish = set(stopwords.words('spanish'))
    stop_words_english = set(stopwords.words('english'))
    stop_words = stop_words_spanish.union(stop_words_english)
    return stop_words


def get_words(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    return tokens


def get_words_without_stopwords(text, stop_words):
    tokens = [word for word in text if word not in stop_words]
    return tokens


def get_words_lemanized(filtered_tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return lemmatized_tokens


def get_words_stemmed(filtered_tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    return stemmed_tokens


def get_training_data():
    training_data = []
    with open('training_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            text, category = row
            training_data.append((text, category))
    return training_data


def generate_model():
    training_data = []
    training_data = get_training_data()

    preprocessed_training_data = [(preprocess(text), category) for text, category in training_data]
    vectorizer = TfidfVectorizer(strip_accents="ascii")

    X_train = [text for text, _ in preprocessed_training_data]
    y_train = [category for _, category in preprocessed_training_data]

    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)
    X_train_vectorized = vectorizer.fit_transform(X_train)

    classifier = RandomForestClassifier()
    classifier.fit(X_train_vectorized, y_train_encoded)

    return classifier, vectorizer, label_encoder


def save_object(obj, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(obj, file)


def load_object(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)


def save_model(classifier, vectorizer, label_encoder, path):
    model_pkl_file = path + 'classifier_model.pkl'
    vectorizer_pkl_file = path + 'vectorizer.pkl'
    label_encoder_pkl_file = path + 'label_encoder.pkl'

    save_object(classifier, model_pkl_file)
    save_object(vectorizer, vectorizer_pkl_file)
    save_object(label_encoder, label_encoder_pkl_file)


def load_model(path):
    model_pkl_file = path + r'/classifier_model.pkl'
    vectorizer_pkl_file = path + r'/vectorizer.pkl'
    label_encoder_pkl_file = path + r'/label_encoder.pkl'

    classifier = load_object(model_pkl_file)
    vectorizer = load_object(vectorizer_pkl_file)
    label_encoder = load_object(label_encoder_pkl_file)

    return classifier, vectorizer, label_encoder


def use_classifier(text, pathFiletoLoad):
    classifier, vectorizer, label_encoder = load_model(pathFiletoLoad)
    new_text = text
    preprocessed_text = preprocess(new_text)

    X_new = vectorizer.transform([preprocessed_text])
    predicted_category_encode = classifier.predict(X_new)
    predicted_category = label_encoder.inverse_transform(predicted_category_encode)
    return predicted_category[0]


# classifier, vectorizer, label_encoder = generate_model()
# save_model(classifier, vectorizer, label_encoder, "./")
# use_classifier("I love my dog")
