import random
import json
import torch

from bot_model import NeuralNet
from sentence_preprocessing import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Linda"
print("Let's chat! (type 'quit' to exit and 'features' to see the extras that have been tacked on!")
while True:
    sentence = input("You: ")
    if sentence == "quit":
        break
    if sentence == "features":
        print("these are the extra features of this chatbot:")
        print("1. Fortune Teller")
        print("2. Random facts")
        print("3. Number Memory Test")
        print("")
        choice = int(input("enter the corresponding number to the feature you want to use:"))
        if choice == 1:
            import Fortune_Teller
        if choice == 2:
            import random_fact
        if choice == 3:
            import number_memory_module
        if choice == 4:
            pass


    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand...")
        
    
