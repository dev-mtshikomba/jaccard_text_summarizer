import math
import nltk
import operator
from textblob import TextBlob

# slip document by of paragraphs
def split_into_paragraphs(doc):
    paragraphs = doc.split("\n")
    return  paragraphs, len(paragraphs)

def number_of_sentences_word_appears(word, sentences_dict):
    count = 0
    for i in range(len(sentences_dict)):
        for w in range(len(sentences_dict[i])):
            if (word == sentences_dict[i][w]):
                count += 1
    return count 

def create_ntf_matrix(sentences_dict, no_dup_words):
    ntf_matrix = []
    for s in range(len(sentences_dict)):
        ntf_matrix.append([0])
        for i in range(len(no_dup_words)):
            ntf_matrix[s].append(sentences_dict[s].count(no_dup_words[i]))
            
def rank_sentences(sentences_dict):
    ranking = {}
    for i in range(len(sentences_dict)):
        ranking[i] = ( len(intersection_of_two_sentences(sentences_dict[0], sentences_dict[i])) 
                       / len(union_of_two_sentences(sentences_dict[0], sentences_dict[i]))
                      )
    return ranking

def intersection_of_two_sentences(sentence_1, sentence_2):
    final = [value for value in sentence_1 if value in sentence_2]
    return final

def union_of_two_sentences(sentence_1, sentence_2):
    return sentence_1 + sentence_2


def summarize_doc(input_file, N):

# read file content
    print('reading '+input_file+' file content...\n')
    f = open(input_file, "r")
    content = f.read()
    
    doc = TextBlob(content)
    
#     get the paragraphs and the length
    paragraphs, parapraph_len = split_into_paragraphs(doc)
    
#     get all the words in the doc
    words = doc.words
    sentences = doc.sentences

# -----------
#     remove stop words
#     doc = TextBlob(doc.words)
# -----------

    print('stemming document and removing file stop words...\n')
#     stem document
    words = words.stem()
    
    
#     remove stop words

    print('summarizing document...\n')
#     Sentences
    sentences_dict = {}
    for i in range(len(sentences)):
        sentences_dict[i] = sentences[i].words.stem()

#     remove duplicate words
    no_dup_words = list(set(words))

#   Jaccard Similarity Rank
    ranking = {}
    ranking = rank_sentences(sentences_dict)
    
#   based off the ranking, return the N top sentences
    sorted_rank = dict(sorted(ranking.items(), key=operator.itemgetter(1), reverse=True))

#    return the top N ranked sentences
    summarized_doc = ''
    for j in range(N):
        summarized_doc += str(sentences[j]) + ' '   
    
    new_file = "summarized_document.smz"
    print('summarized content saved to '+new_file+'...\n')
#   concatinate sentences into a string and add to output file .smz
    f = open(new_file, "w")
    
#   wite to .smz file
    f.write(summarized_doc)
    
    print('done...')