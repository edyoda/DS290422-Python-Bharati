str2 = ""
str1="six two five four"
map_dict={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
words=str1.split(' ')
digit=0
for word in words:
    word=word.lower()
    digit=digit*10+(map_dict[word])

print(digit)



