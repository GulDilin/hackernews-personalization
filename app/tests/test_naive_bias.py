import csv
import pytest
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from app.naive_bayes_classifier import NaiveBayesClassifier, clean


def test_naive_bayes_classifier():
    with open('./smsspamcollection/SMSSpamCollection', 'r', encoding='utf-8') as f:
        data = list(csv.reader(f, delimiter='\t'))

    def print_n_first(X_1, y_1, n_first):
        for row in zip(y_1[:n_first], X_1[:n_first]):
            print(row)

    X, y = [], []
    for target, msg in data:
        X.append(msg)
        y.append(target)
    X = [clean(x).lower() for x in X]

    cut = 3900
    X_train, y_train, X_test, y_test = X[:cut], y[:cut], X[cut:], y[cut:]
    print(f'\nLength of X: {len(X)} len_train: {len(X_train)} len_test: {len(X_test)}')

    model = NaiveBayesClassifier(alpha=0.05)
    model.fit(X_train, y_train)
    y = model.predict(X_test)
    print()
    print_n_first(X_test, y, 5)
    score_1 = model.score(X_test, y_test)
    print(score_1)

    model = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('classifier', MultinomialNB(alpha=0.05)),
    ])

    model.fit(X_train, y_train)
    y_2 = model.predict(X_test)
    print()
    print_n_first(X_test, y_2, 5)
    score_2 = model.score(X_test, y_test)
    print(score_2)
    assert abs(score_2 - score_1) < 0.2
