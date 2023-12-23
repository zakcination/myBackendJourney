from collections import Counter
import re

words = re.findall(r'\w+', open('week3/third_word_of_Abay.txt').read().lower())
c = Counter(words)


print(c.most_common(3))



list(c)
