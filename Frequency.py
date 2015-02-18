from utils import textfromfile

class FrequencyAnalyzer:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.frequencies = dict.fromkeys(self.alphabet, 0)
        self.text = ""
        self.len = 0

    def feed(self, filename):
        self.frequencies = dict.fromkeys(self.alphabet, 0)
        self.text = textfromfile(filename)
        self.len = len(self.text)
        for s in self.text:
            self.frequencies[s] += 1

    def get_freq(self):
        return sorted(self.frequencies.items(), key=lambda s: s[1], reverse=True)

    def get_len(self):
        return self.len

analyzer = FrequencyAnalyzer()
analyzer.feed("bigclean")