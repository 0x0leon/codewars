class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.k = key
        self.al = alphabet
        self.len_alphabet = len(self.al)

    def encode(self, text):
        return ''.join([self.al[(self.al.index(self.k[i % len(self.k)]) + self.al.index(text[i])) % self.len_alphabet ] if text[i] in self.al else text[i] for i in range(len(text))])

    def decode(self, text):           
        return ''.join([self.al[(self.al.index(text[i]) - self.al.index(self.k[i % len(self.k)])) % self.len_alphabet ] if text[i] in self.al else text[i] for i in range(len(text))])


# alphabet = 'abcdefghijklmnopqrstuvwxyz';
# key = 'password';
# v = VigenereCipher(key, alphabet)
# print(f' alphabet {v.al}')
# print(f' key {v.k}')
# print(v.encode("codewars"))
# print(v.decode("rovwsoiv"))

