# import torch
# from torch.nn import nn 
# from torch.utils.data import Dataset, DataLoader

# import numpy as np 
import random 
import json 

# from model import IntentModelClassifier

with open('intents.json', 'r') as f:
    intents = json.load(f)

print(intents)


