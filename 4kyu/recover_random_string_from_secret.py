
'''There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.
A triplet here is defined as a sequence of three letters such that each letter occurs somewhere 
before the next in the given string. "whi" is a triplet for the string "whatisup".
As a simplification, you may assume that no letter occurs more than once in the secret string.
You can assume nothing about the triplets given to you other than that they are valid 
triplets and that they contain sufficient information to deduce the original string. 
In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.'''


secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],    # w h a()
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]


from collections import defaultdict

def recoverSecret(subsequences):
    # build up dictioanry
    preceding_chars = defaultdict(set)
    for subseq in subsequences:
        for i in range(len(subseq)):
            preceding_chars[subseq[i]].update(subseq[i - 1] if i else '')

    solution = []
    while preceding_chars:
        
        empty = iter([k for k, v in preceding_chars.items() if not v])
        charac = next(empty)
        
        del preceding_chars[charac]
        for prec in preceding_chars.values():
            if charac in prec:
                print(charac)
                prec.remove(charac)
        solution.append(charac)
    
    return ''.join(secret)

print(recoverSecret(triplets))



