import re

def diffCharCount(message):
    alpha_c = 0
    digit_c = 0
    symbols_c = 0
    white_c = 0

    alpha = "nm"
    digit = "1234567890"
    symbols = "~!@#$%^&*()_+`{}|[]\\:\';\",./<>?"
    whites = " \r \n \t"


    for char in message:
        if char in alpha:
            alpha_c += 1
        if char in digit:
            digit_c += 1
        if char in symbols:
            symbols_c += 1
        if char in whites:
            white_c += 1
        
    return alpha_c, digit_c, symbols_c, white_c

def wordsFeature(words):
    sum = 0
    swords = []
    for word in words:
        sum += len(word)
        if len(word) <= 2:
            swords.append(word)
    if len(words) > 0:
            
        avg = sum/len(words)

        w_set = set(words)
        unique = len(w_set)

        u_r = unique/len(words)

        return len(swords), avg, u_r
    
    return 0, 0, 0

def getKeywords(msg, spm):
    c = 0
    msg = msg.lower()
    for w in spm:
        if w.lower() in msg:
            c+=1
    return c    

def extractFeatures(message, spam):
    features = []
    c = len(message)
    
    ac, dc, sc, wc = diffCharCount(message)

    ar = ac/c
    dr = dc/c
    sr = sc/c
    wr = wc/c
    
    words = (re.findall("[a-zA-Z_]+", message))
    word_c = len(words)

    small_c, avg_w, u_r = wordsFeature(words)

    k_c = getKeywords(message, spam)

    features.append(c)
    features.append(ar)
    features.append(dr)
    features.append(sr)
    features.append(wr)
    features.append(wc)
    features.append(small_c)
    features.append(avg_w)
    features.append(u_r)
    features.append(k_c)

    return features

def getXY(data, spam):
    X = [[]]
    messages = []
    Y = []
    final_data = []
    for html in data:
        html = html.encode('utf-8', 'ignore')
        html = html.decode('ascii', 'ignore')

        a = html.split(',', 1)
        if a[0] == 'spam':
            Y.append(1)
        else:
            Y.append(0)

        messages.append(a[1])

    i = 0
    for message in messages:
        features = extractFeatures(message, spam)
        X.append(features)
        i+=1

    return X, Y

def getMessageFeatures(message):
    spam = open('spamWords').read()
    spam = spam.split("\n")
    spam = spam[:-1]
    return extractFeatures(message, spam)


def getFeatures():
    file = open('data/spam.csv')

    data = file.readlines()
    spam = open('spamWords').read()
    spam = spam.split("\n")
    spam = spam[:-1]
    X, Y = getXY(data, spam)

    return X[1:], Y
