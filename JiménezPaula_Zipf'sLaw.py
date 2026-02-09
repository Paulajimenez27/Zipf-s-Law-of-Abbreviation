#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 12:49:51 2026

@author: pauli
"""
#IMPORTS#
import en_core_web_sm  #FOR ENGLISH BASED TOKENIZATION
import es_core_news_sm #FOR SPANISH BASED TOKENIZATION
from collections import Counter #COUNTING   
import spacy #LIBRARY TO TOKENIZE AND NORMALIZE TEXT
import matplotlib.pyplot as plt #TO PLOT VISUALIZATION


#--1 English text--#

#load document (name of document, function read, encoding ignores special symbols)
with open('Relatocorto_ENG.txt', 'r', errors='ignore') as archivo:
    textoENG = archivo.read()
    
#load english model for spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp(textoENG)

#normalization and tokenization (all lowecase, no punctuation, no spaces)
wordsENG = [t.text.lower() for t in doc if not t.is_punct and not t.is_space]

#calculates 10 most common words
top10_ENG = Counter(wordsENG).most_common(10)
#printing 10 most common words
print("English Top 10 most common words:", top10_ENG)

#calculate average length (number of letters) for most common words
suma_top = 0
for word, freq in top10_ENG:
    suma_top = suma_top + len(word)
promedio_topENG = suma_top / 10

#calculate average length of all words in text
suma_total = 0
for w in wordsENG:
    suma_total = suma_total + len(w)

average_generalENG = suma_total / len(wordsENG)

#print results
print("Average total text ENGLISH:",average_generalENG)
print("Average top 10 most frequent words ENGLISH:",promedio_topENG)

#--2 Spanish text--#

#load document (name, function read, encoding ignores special symbols)
with open('Relatocorto_Esp.txt', 'r', errors='ignore') as archivo:
    textoESP = archivo.read()

#load spanish model for spacy
nlp = spacy.load("es_core_news_sm")

doc = nlp(textoESP)

#normalization and tokenization (all lowecase, no punctuation, no spaces)
wordsESP = [t.text.lower() for t in doc if not t.is_punct and not t.is_space]

#calculates 10 most common words
top10_ESP = Counter(wordsESP).most_common(10)
#printing 10 most common words
print("Spanish Top 10 most common words:", top10_ESP)

#calculate average length (number of letters) for most common words
suma_top = 0
for word, freq in top10_ESP:
    suma_top = suma_top + len(word)
average_topESP = suma_top / 10

#calculate average length of all words in text
suma_total = 0
for w in wordsESP:
    suma_total = suma_total + len(w)

average_generalESP = suma_total / len(wordsESP)

#print results
print("Average total text SPANISH:",average_generalESP)
print("Average top 10 most frequent words SPANISH:",average_topESP)


# Scatter plot to visualize results

def get_plot_data(word_list):
    counts = Counter(word_list)
    # x = length of each unique word, y = its frequency
    x = [len(word) for word in counts.keys()]
    y = list(counts.values())
    return x, y

x_eng, y_eng = get_plot_data(wordsENG)
x_esp, y_esp = get_plot_data(wordsESP)

plt.figure(figsize=(10, 6))

# Plot English Data (Blue)
plt.scatter(x_eng, y_eng, alpha=0.5, color='royalblue', label='English words', s=40)

# Plot Spanish Data (Orange)
plt.scatter(x_esp, y_esp, alpha=0.5, color='darkorange', label='Spanish words', s=40)

# Formatting the Chart
plt.yscale('log') # This is important to see the distribution clearly
plt.title("Word Frequency vs. Word Length", fontsize=14)
plt.xlabel("Word Length (Number of Characters)", fontsize=12)
plt.ylabel("Frequency of Use (Log Scale)", fontsize=12)
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.3)

plt.show()




    









