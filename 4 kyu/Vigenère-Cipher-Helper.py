class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.n = len(key)
        self.N = len(alphabet)
        self.dic1 = dict(zip(alphabet, list(range(self.N))))
        self.dic2 = dict(zip(list(range(self.N)), alphabet))
    
    def encode(self, text):
        if self.N == 0 or self.n == 0:
            return text
        else:
            res = ''
            text = text
            for i in range(len(text)):
                if text[i] in self.dic1:
                    shift = self.dic1[self.key[i%self.n]]
                    res += self.dic2[(self.dic1[text[i]] + shift) % self.N]
                else:
                    res += text[i]
            return res
    
    def decode(self, text):
        if self.N == 0 or self.n == 0:
            return text
        else:
            res = ''
            text = text
            for i in range(len(text)):
                if text[i] in self.dic1:
                    shift = self.dic1[self.key[i%self.n]]
                    res += self.dic2[(self.dic1[text[i]] - shift + self.N) % self.N]
                else:
                    res += text[i]
            return res
