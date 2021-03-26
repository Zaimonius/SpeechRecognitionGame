import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets
import utils
import train
import game



mode = 4

#------------------------------------------------
#Train
if mode == 1:
    trainer = train.Trainer(file_path="librispeechmodel.txt", epochs=5)
    trainer.test()

#------------------------------------------------
#Test
if mode == 2:
    trainer = train.Trainer(file_path="librispeechmodel.txt", epochs=0)
    trainer.test()

#------------------------------------------------
#use on own wav
if mode == 3:
    trainer = train.Trainer(file_path="librispeechmodel.txt", epochs=0, batch_size=1)
    trainer.speech_to_text('./wavfilename.wav')

if mode == 4:
    game = game.Game(1280, 720, 16)
    game.run()