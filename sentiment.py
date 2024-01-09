# here the first step is to read text,convert it to lowr case ,and then remove punctuations

import string
from collections import Counter
import matplotlib.pyplot as plt
# encoding is used to read data which is encoded form present in some blogs of internet
file_to_read = open('read.txt', "r", encoding='utf-8')
text = file_to_read.read()

lowertext = text.lower()


# so here translate is used to remove punctuations in data read
# str.maketrans is a function inside translate that take three parameters ,3 rd parameter is for punctuation
cleantext = lowertext.translate(str.maketrans('', '', string.punctuation))


# 2nd step
# tokenization means splliting sting into seperate words into a list because npl is word by word analysis
tokenize_words = cleantext.split()


# thse are some stop words that doesnt add meaning to the sentence
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
              "Yours", "yourself", "yourselves", "he", "nie", "his", "himself", "she",
              "ee", "bers", "herself", "it", "its", "itself", "they", "then", "their", "theirs",
              "themselves", "what", "which", "who", "whoe", "this", "that", "these", "those",
              "a", "i", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
              "do", "does", "did", "doing", "a", "an", "the", "and", "out", "if", "on", "because", "as",
              "until", "while", "Tof", "at", "by", "for", "with", "about", "against", "between", "into",
              "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in",
              "out", "on", "off", "over", "under", "again", "further", "then", "unce", "bere", "there",
              "when", "here", "y", "how", "all", "any", "both", "each", "Few", "more", "most", "other",
              "some", "such", "no", "nor", "hot", "only", "own", "sane", "so", "than", "too", "very", "s",
              "t", "can", "will", "just", "don", "should", "now"]

for word in stop_words:
    if word in tokenize_words:
        tokenize_words.remove(word)



#3rd step to check the final tokenized words matches which emotion

#read emotion list from emotion.txt into a file variable ,then do some modifications and print words and corresponding emotions

emotions_list=[]
with open('emotions.txt',"r") as file:
    for line in file:
        clearline=line.replace('/n','').replace("'",'').replace(',','').strip()
        word,emotion =clearline.split(':')
        # so here the word before colon is stored into word variable and the word after colon is stored in emotion variable
        if word in tokenize_words:
         emotions_list.append(emotion)

print(emotions_list)

#now we have to count number of emotions using counter from importiong collection
w=Counter(emotions_list)
print(w)

#matplotlib is used to plot the graph,of fiven keys and values
#there is also a other way
#fig,ax1=plt.subplots()
#ax1.bar(w.keys(),w.values())
#fig.autofmt_xdate()
plt.bar(w.keys(),w.values())
plt.savefig('graph.png')
plt.show()


