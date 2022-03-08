def split(a):
    array=[]
    for i in range(0,len(a)):
        array.append(a[i])
    return sorted(array)

def anagrams(word, words):
    array=[]
    for i in range(0,len(words)):
        if split(word) == split(words[i]):
            array.append(words[i])
    return array
