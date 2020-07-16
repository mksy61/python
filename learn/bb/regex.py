import re

try:
    file = open("s.txt", "r")
except Exception as identifier:
    print("Dosya açılamadı:", identifier)
    quit()

strFile = file.read()
strFile = strFile.replace(".", " ")
strFile = strFile.replace(",", " ")
strFile = strFile.lower()

words = strFile.split()

wordCount = dict()

for word in words:
    wordCount[word] = wordCount.get(word, 0) + 1

mostusednumber = 0
mostusedword = ""
for k, v in wordCount.items():
    if re.search("^s.....$", k):
        print(k, " ", v)
