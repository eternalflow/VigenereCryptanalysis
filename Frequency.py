from utils import textfromfile
from math import log
from collections import Counter
import pprint


class FrequencyAnalyzer:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.bigrams = {}
        self.frequencies = dict.fromkeys(self.alphabet, 0)
        self.percentage = dict.fromkeys(self.alphabet, 0)
        self.text = ""
        self.len = 0
        self.letter_entropy = 0

    def feed(self, filename):
        self.text = textfromfile(filename)
        self.len = len(self.text)
        # for s in self.text:
        #     self.frequencies[s] += 1
        self.frequencies = Counter(self.text)
        for letter in self.alphabet:
            self.percentage[letter] = self.frequencies[letter] / float(self.len)

        self.__count_bigrams()
        self.__count_entropy()

    def get_freq(self):
        return sorted(self.frequencies.items(), key=lambda s: s[1], reverse=True)

    def get_percentage(self):
        return sorted(self.percentage.items(), key=lambda s: s[1], reverse=True)

    def get_len(self):
        return self.len

    # def print_attrs(self):
    #     for letter in self.alphabet:
    #         print letter, self.frequencies[letter], round(100 * self.percentage[letter], 3)
    #     print "entropy", self.letter_entropy
    #     print self.bigrams

    def __count_entropy(self):
        for letter in self.alphabet:
            self.letter_entropy -= self.percentage[letter] * log(self.percentage[letter], 2)

    def __count_bigrams(self):
        bigrams = []
        for j in range(len(self.text)):
            bigrams.append(self.text[j:j+2])
        self.bigrams = Counter(bigrams)

analyzer = FrequencyAnalyzer()
analyzer.feed("bigclean")
pprint.pprint(analyzer.get_freq())
pprint.pprint(analyzer.get_percentage())
pprint.pprint("Entropy %f" % analyzer.letter_entropy)
print "20 most common bigrams:"
pprint.pprint(analyzer.bigrams.most_common(20))
