import re
text =  input("Enter your text: ")
text = text.lower()
clean_text = re.sub(r"[^\w\s]", " ", text)
tokens = clean_text.split()
print (tokens)

stopwords = {"a", "an", "the", "is", "are", "was", "were", "am", "be", "been",
             "and", "or", "but", "if", "in", "on", "at", "to", "of", "for",
             "with", "as", "by", "this", "that", "it", "from", "not"}
clean_tokens =[]
for i in tokens:
    if i not in stopwords:
        clean_tokens.append(i)

print(clean_tokens," ")
word_freq = {}
for word in clean_tokens:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
       

print(word_freq)
