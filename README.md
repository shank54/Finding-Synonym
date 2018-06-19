# Finding-Synonym
Python application to find synonym of a word.

This program finds a synonym for given word among four given words using Compting Linguistics without using any english dictionary or thesauruses.
This is achieved by a concept called semantic similarity. It finds the semantic similarity between the question word and the option words.
The word with highest similarity in the given options is returned as answer.

We build a dictionary of dictionaries for each word and check the frequency of occurance of each word among the dictionaries and give a score to each option word. We can use any huge texts like any novels of Shakesphere to build the dictionaries.

## Example Input/Output

###### 1) Input: 	
        wary       sad, vigilant, distorted, tired

###### Output:  	
        vigilant

###### 2) Input: 	
        ecstatic   animanted, bewildered, enraptured, dream
###### Output:	
        enraptured

###### 3) Input: 	
        pious     pure, clean, devout, dirty
######  Output	
        devout

###### 4) Input: 	
        bare      uncovered, tolerance, clear, neat
###### Outout: 	
        uncovered

### Requirements:
Python 2.7

### Instructions to run:
Download meaning.py, txt files and put all in same folder.

python meaning.py
