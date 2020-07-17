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
    if v > mostusednumber:
        mostusednumber = v
        mostusedword = k
    print(k, v)

print()
print(mostusedword, mostusednumber)

s = sorted(wordCount.items())
print(s)

file.close()
