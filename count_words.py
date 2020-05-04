#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter
import re, string
"""Count words."""

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    print(text)
    # TODO: Convert to lowercase
    lowerText = text.lower()
  
    # TODO: Split text into tokens (words), leaving out punctuation
    text = text.replace('.','').replace(',','').replace('!','').replace('-','')
    textlist = text.split(' ')
    # (Hint: Use regex to split on non-alphanumeric characters)
    
    # TODO: Aggregate word counts using a dictionary
    counts = Counter(textlist)
    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()

