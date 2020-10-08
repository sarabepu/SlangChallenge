
from typing import List
from collections import deque #this has O(1) complexity for popleft()

"""
This function calculates all the Ngrams in a text. 
parameters:
    text: str. text to be analyzed
    n: int. length of the ngrams
return: list of strings with the ngrams or an empty list if n=0 or the text in not long enough

time complexity: O(len(text))

"""
def calculateNGrams(text:str,n:int)-> List[str]:
    # Edge cases
    if not n or len(text)<n:
        return []
    else:
        currentNgram= deque()
        for i in range(n):
            currentNgram.append(text[i])
        currentIndex=n-1
        ans=[]
        
        ans.append(''.join(currentNgram)) # first ngram,  .join has complexity O(n)
        while currentIndex<len(text)-1:
            currentNgram.popleft()
            currentIndex+=1
            currentNgram.append(text[currentIndex])
            ans.append(''.join(currentNgram)) 
        return ans
"""
This function returns the most frecuent Ngram in a text for a given n. Ngrams are case insensitive
parameters:
    text: str. text to be analyzed
    n: int. length of the ngrams
return: most frecuent ngram in a text. If more than 1 ngram have the same frecuency returns the first in the text

time complexity: O(len(text)) 
"""
def mostFrequentNGram(text:str, n:int)-> str:
    # I'm going to use first step function because of mantenibility but if performance is more important, 
    # it would be more efficent to construct a hashtable in the first step instead of constructing it from the list
    ngrams=calculateNGrams(text,n) #O(len(text))
    
    #The complexity below is O(k) being k the number of ngrams
    hash_ngrams={}
    for ngram in ngrams:
        ngram=ngram.lower()
        hash_ngrams[ngram]= hash_ngrams.get(ngram,0)+1
    print(hash_ngrams)
    ans=''
    freq=0
    for key in hash_ngrams:
        if hash_ngrams[key]>freq:
            ans,freq=key,hash_ngrams[key]
    return ans



# First step 
print('First step',calculateNGrams("Slang",2))
# Second step 
print('Second step',mostFrequentNGram("To be or not to be",2))

"""
FIRST STEP VALIDATION 

text: Slang, n:3
len(text)=5

currentNgram=[]->[S,l,a]
currentIndex=2
ans=[] -> [Sla]

curentNgam=[l,a]
currentIndex=3
curentNgam=[l,a,n]
ans=[Sla,lan]

curentNgam=[a,n]
currentIndex=4
curentNgam=[a,n,g]
ans=[Sla,lan,ang] #check


SECOND STEP VALIDATION 

text: Slang, n:3
len(text)=5

ngrams=['To', 'o ', ' b', 'be', 'e ', ' o', 'or', 'r ', ' n', 'no', 'ot', 't ', ' t', 'to', 'o ', ' b', 'be']
hash_ngrams={'to': 2, 'o ': 2, ' b': 2, 'be': 2, 'e ': 1, ' o': 1, 'or': 1, 'r ': 1, ' n': 1, 'no': 1, 'ot': 1, 't ': 1, ' t': 1}
ans=to
freq=2


"""




