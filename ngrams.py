
from typing import List
from collections import deque #this has O(1) complexity for popleft()

"""
This function calculates all the Ngrams in a text. 
text: str. text to be analyzed
n: int. length of the ngrams
return: list of strings with the ngrams

time complexity: O(len(text))
"""
def calculateNGrams(text:str,n:int)-> List[str]:
    if len(text)<n:
        return
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

# First step 
print('First step',calculateNGrams("Slang",2))

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

"""




