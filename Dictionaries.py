file_name= "textfile.txt"
wordfreq = {}
with open(file_name,"r") as file:
    for line in file:
        words = line.lower().split()
        for word in words:
            word = word.strip(".,?!:()")
            wordfreq[word]= wordfreq.get(word,0) + 1
sorted_words = sorted(wordfreq.items(), key=lambda x: x[1], reverse=True)[:5]
for word, freq in sorted_words:
    print(f"{word}:{freq}")
