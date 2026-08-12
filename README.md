# Zipf-s-Law-of-Abbreviation
This code is part of an assignment for the subject Natural Language Processing from the Universitat Pompeu Fabra (UPF). The aim of it is to serve as a tool to analyze if the Zipf's law stands for different genres and languages.

In this case two texts were used as dataset, these can be found in this repository under the names "Relatocorto_ENG" for the English text and "Relatocorto_ESP" for the Spanish text. 

# The code

(1) normalizes and tokenizes the texts through a spacy model for the desired languages. In this case "en_core_web_sm" for English and "es_core_news_sm" for Spanish. These models can be changed by others if the languages analyzed are not English or Spansih, for a better tokenization. 

(2) Then it calculates the 10 most frequent words for each language. 

(3) An average length is calculated for the 10 most common words and for all the words in the text.

(4) Qualitative analysis: scatter plot is done so as to visualize the results.

The code results in a list of the 10 most frequent words for each language shown as tupples (word, frequency) together with the number for the average length (letters) of the 10 most frequent words and then an average length of all words in the corpus for each language.
Then the scatter plot serves as aid to observe whether the curve looks in fact like Zipf's law curve. 
