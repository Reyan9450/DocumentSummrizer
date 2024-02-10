import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

def preprocess_text(text):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    # Convert words to lowercase
    words = [word.lower() for word in words]
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    
    return sentences, words

def calculate_sentence_scores(sentences, word_scores):
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_scores.keys():
                if len(sentence.split(' ')) < 30:  # Consider only sentences less than 30 words
                    if sentence not in sentence_scores.keys():
                        sentence_scores[sentence] = word_scores[word]
                    else:
                        sentence_scores[sentence] += word_scores[word]
    
    return sentence_scores

def summarize_text(text, num_sentences=3):
    sentences, words = preprocess_text(text)
    
    # Calculate word frequencies
    word_freq = FreqDist(words)
    
    # Calculate word scores
    word_scores = {}
    for word in word_freq.keys():
        word_scores[word] = word_freq[word] / max(word_freq.values())
    
    # Calculate sentence scores
    sentence_scores = calculate_sentence_scores(sentences, word_scores)
    
    # Sort sentences by score in descending order
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Select the top 'num_sentences' sentences for summary
    summary_sentences = [sentence for sentence, score in sorted_sentences[:num_sentences]]
    
    # Join the selected sentences to form the summary
    summary = ' '.join(summary_sentences)
    
    return summary

# Example usage
text = """
Text summarization is the process of distilling the most important information from a source (or sources) to produce an abridged version for a particular user (or users) and task (or tasks). There are two main types of text summarization: extractive and abstractive. Extractive summarization involves selecting and extracting important sentences or passages from the source text, while abstractive summarization involves generating new sentences to capture the core meaning of the source text.

In this example, we'll focus on extractive text summarization using Python's NLTK library. We'll demonstrate how to summarize a piece of text by selecting the most relevant sentences based on word frequencies.

First, let's define a function to preprocess the text by tokenizing it into sentences and words, converting words to lowercase, and removing stopwords. We'll then calculate word frequencies and scores, and use them to assign scores to sentences based on the words they contain.

Finally, we'll select the top-ranked sentences and concatenate them to generate the summary.

Let's summarize the following text:
Text summarization is the process of distilling the most important information from a source (or sources) to produce an abridged version for a particular user (or users) and task (or tasks).
"""

summary = summarize_text(text)
print("Summary:")
print(summary)
