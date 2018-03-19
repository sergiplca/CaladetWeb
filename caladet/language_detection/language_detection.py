import pickle


def load_trained_set():
    filehandler = open('caladet/language_detection/trained_sets/naive_bayes.pickle', 'rb')
    trained_set = pickle.load(filehandler, encoding='latin1')
    filehandler.close()
    return trained_set


def word_feats(words):
    return dict([(word, True) for word in words.split()])


def classify(tweet):
    classifier = load_trained_set()
    return classifier.classify(word_feats(tweet))