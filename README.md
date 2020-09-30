# dagger
 Class 12 CS Project. 
 Members - Rohith, Kausthuban, Abineshwar, Shylendra Prasad.
 We are doing - Machine learning Bot.
 This bot uses pytorch and nltk to process what a person is talking and gives an appropriate reply.
 it might not be that accurate, but it works and no one can deny that fact.
 so what basically happens in the processing is this:
 
part 1: sentence preprocessing
 example sentence = "Hi, how long does delivery take?"
 it first uses NLTK(Natural Language ToolKit) to break up or "tokenize" the sentence like this:
 ["Hi",",","how","long","does","delivery","take","?"]
 then we remove puntuation marks and convert capital letters(if any) to lowercase for the sake of simplicity. so after this step it looks like this:
 ["hi","how","long","does","delivery","take"] 
 now it uses a process called stemming which looks for common words in our intents database and strips them down to it's root word
eg:["organ","organizing","organize","organizer"]
after stemming
["organ","organ","organ","organ"]

this finishes sentence preprocessing.
 
