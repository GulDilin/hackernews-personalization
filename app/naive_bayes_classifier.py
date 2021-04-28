from collections import defaultdict, Counter
import math
from textblob import TextBlob
from nltk.corpus import stopwords
import string


def clean(s):
    translator = str.maketrans("", "", string.punctuation)
    return s.translate(translator)


class NaiveBayesClassifier:

    def __init__(self, alpha):
        self.categories = defaultdict(Counter)
        self.words = defaultdict(Counter)
        self.words_probs = defaultdict(Counter)
        self.N = 1
        self.alpha = alpha
        self.stop_words = stopwords.words('english')

    def _define_probabilities(self):
        for category in self.categories:
            self.categories[category]['prob'] = self.categories[category]['amount'] / self.N

        for word in self.words:
            for category in self.categories:
                n = self.words[word][category]
                nc = self.categories[category]['amount']
                d = len(self.words)
                self.words_probs[word][category] = (n + self.alpha) / (nc + self.alpha * d)

    def _tokenize(self, x):
        text_blob = TextBlob(x.lower())
        words = text_blob.words.lemmatize().stem()
        words = [it for it in words if it not in self.stop_words]
        return words

    def fit(self, X, y):
        """ Fit Naive Bayes classifier according to X, y. """
        if len(X) != len(y):
            raise ValueError('X and y need to have same len')

        self.N = len(X)
        for i in range(len(X)):
            category = y[i]
            self.categories[category]['amount'] += 1
            words = self._tokenize(X[i])
            for word in words:
                self.words[word][category] += 1
        self._define_probabilities()

    def classify(self, x):
        words = self._tokenize(x)
        counter = Counter()
        for category in self.categories:
            counter[category] = math.log(self.categories[category]['prob']) + \
                                sum([self.words_probs[word][category] for word in words])
        return counter.most_common(1)[0][0]

    def predict(self, X):
        """ Perform classification on an array of test vectors X. """
        return [self.classify(entry) for entry in X]

    def score(self, X_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        if len(X_test) != len(y_test):
            raise ValueError('X_test and y_test need to have same len')
        y = self.predict(X_test)
        total_true = len([i for i in range(len(y_test)) if y[i] == y_test[i]])
        return total_true / len(y_test)
