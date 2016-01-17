
things=raw_input("please input some word:")

word=things.split(' ')

morestuff=["day","night","song","corn","banana","girl"]
if "dog" in word:
   print "dog in word"
else:
    print "dog is not in word"
while len(word)!=8:
      hello=morestuff.pop()
      word.append(hello)
      print "word:%s"%word

print "let's do some thing with word:"

print "the length of the word:%s"%len(word)

print "word[1]:%s"%word[1]
print "word[-1]:%s"%word[-1]
sen=word.pop(-1)
print "word.pop(-1):%s"%sen
print "word:%s"%word

word.append(sen)
print "word:%s"%word

print ' '.join(word)
print '#'.join(word)
