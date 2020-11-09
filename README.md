# dagger
 Class 12 CS Project. 
 Members - Rohith, Kausthuban, Abineshwar, Shylendra Prasad.
 We are doing - Machine learning Bot.
 This bot uses pytorch and nltk to process what a person is talking and gives an appropriate reply.
 it might not be that accurate, but it works.
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

Then, we go to step 2:
creating our bag of words
"bag of words" here is basically a big list of all our words that are present in our intents file.
this bag of words is the reference that our midel will use to identify words.
eg:
bag_of_words=['hi','helo','hello there','hentai']
now this is where the torch module comes in:
it stores each word as a value of zeros and ones. 
eg: hello=[0,1,0,0], hi=[1,0,0,0]
(zero for other words and one for where the words are present)
 This is how our model identifies induvidual words.
 after identifying the word, our bot looks into a pre-trained data.pth file that is made via the training model.py file which makes those bag of words and the intents file into the neural network which helps the bot in linking the various tags, responses and labels
 
 Then, our bot is ready for chatting. when we initiate chat.py, the file uses the data.pth file which contains the training model and the neural networks and then applies probality calculation to using a softmax model which works by backtracking from the sentences to the bag of words identifier. Then the bot takes the input sentences, and gives a reply which it thinks is appropriate.
