from collections import Counter

word_list = []
keywords = []

with open('input_file.txt','rb') as f:
    [word_list.append(word) for line in f for word in line.lower().split()]
    
with open('keywords.txt','rb') as f:
    [keywords.append(word) for line in f for word in line.lower().split()]

word_list_count = Counter(word_list)
#print(word_list_count)
keyword_count = Counter(keywords)

#print(keyword_count) 


f = open('out_put_file.txt','w')
print('\n\n')

common = set(word_list_count) & set(keyword_count)
#print(common)

for (key,value) in set(word_list_count.items()):
    if key in common:
      print('%s: %s ' % ((key).decode(),value))
      f.write('%s: %s \n' % (key.decode(),value))

for (key,value) in set(keyword_count.items()):
    if key not in common:
      print('%s: NOT FOUND ' % (key.decode()))
      f.write('%s: NOT FOUND \n' % (key.decode()))


print('\n\n')

f.close()
