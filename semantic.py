import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
  for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))
      
      
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)
      
# Write a note about what you found interesting about the similarities between cat, monkey and banana
# ● Cat and monkey seem to be similar because they are both animals;
# ● Similarly, banana and apple are similar because they are both fruits;
# ● Interestingly, monkey and banana have a higher similarity than monkey and apple.
#   So we can assume that the model already puts together that monkeys eat bananas and that is why there is a significant similarity.
# ● Another interesting fact is that cat does not have any significant similarity with any of the fruits although monkey does.
#   So, the model does not explicitly seem to recognise transitive relationships in its calculation.

# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from the model 'en_core_web_md'.
# I have no clue
