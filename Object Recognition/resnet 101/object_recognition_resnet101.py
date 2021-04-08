#object recognition using resnet101 , a pretrained model
from torchvision import models
dir(models)
alexnet=models.AlexNet()
resnet=models.resnet101(pretrained=True) #downloads all the weights of this model

from torchvision import transforms
preprocess = transforms.Compose([
transforms.Resize(256),
transforms.CenterCrop(224),
transforms.ToTensor(),
transforms.Normalize(
mean=[0.485, 0.456, 0.406],
std=[0.229, 0.224, 0.225]
)])
from PIL import Image
#img=Image.open('C:/Users/91884/Pictures/IMG_20190918_193240_465.jpg')
img=Image.open('C:/Users/91884/Pictures/dog.jpg')
img.show()
img_t=preprocess(img)

import torch
batch_t=torch.unsqueeze(img_t,0)
resnet.eval()
out=resnet(batch_t)
out

with open('C:/Users/91884/Desktop/ImageNet Labels/imagenet_classes.txt') as f:
	labels=[line.strip() for line in f.readlines()]

_,index=torch.max(out,1)

percentage=torch.nn.functional.softmax(out,dim=1)[0]*100
print('Label:',labels[index[0]])
print('Percentage:',percentage[index[0]].item())
