import string 

count = {}
count2= {}

with open('lab21text.txt', 'r') as file:
    #words = file.read().split('\n').lower()
    book = file.read()
    print(book)
    book = book.lower()
    #.split('\n')
    # maketrans takes in 3 paramaters and returns the utf-8 code number
    translator = str.maketrans('', '', string.punctuation)
   
    # this translates the translator to readable things
    book = book.translate(translator) # I am a string with punctuation
    
    #words = str.maketrans('', '', digits)
    #words = [i.translate(words) for i in words]

    # this splits the string to a list of strings
    book = book.split()#.split('\n')
    #print (book)


    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# checking to see if the word is in the book and checking aginst stop words
    for word in book:
        if word in stopwords:
            pass
        elif word not in count:
            count[word] = 1
        elif word in count:
            count[word] += 1
    # print(count)
    words = list(count.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    # print("this is",words)
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

    for word in book:
        if word in stopwords:
            pass
        elif word not in count2:
            count2[word] = word
        elif word in count2:
            count2[word] += word

    print(count2)
    words2 = list(count2.items())
    print(words2)

    pair = {}
    pairs = {}


    for i in range(len(words)):
        word = words[i]
        if word not in stopwords:
            pair[word] = pair.get(word, 0) +1
        if i< len(words) -1:
            if (words[i] not in stopwords) and (words[i+1] not in stopwords):
                things = (words[i], words[i+1])
                pairs[things] = pairs.get(things, 0) + 1
    print(pair, "this is pair")
    print(pairs, "this is pairs")





