import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        # store postives/negatives in seperate lists
        self.positives = []
        self.negatives = []

        # open files, ignore non-words, grab words, strip em, add em
        with open(positives) as lines:
            for line in lines:
                if not line.startswith(';') and len(line) > 0:
                    self.positives.append(line.strip())
        with open(negatives) as lines:
            for line in lines:
                if not line.startswith(';') and len(line) > 0:
                    self.negatives.append(line.strip())

    def analyze(self, text):

        # tokenize text
        words = nltk.word_tokenize(text)

        # find score of tweet
        score = 0.0
        for word in words:
            if word in self.positives:
                score += 1.0
            elif word in self.negatives:
                score -= 1.0
        return score
