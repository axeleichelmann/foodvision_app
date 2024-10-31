import torchvision
import torch
import torch.nn as nn



def create_effnetb0_classifier(out_features, dropout_p : float=0.2):
    """
    Create EfficientNet B0 Classifier with an adjusted classifier layer
    """

    # Import EfficientNet B0 model architecture & assign it default weights
    model = torchvision.models.efficientnet_b0()
    for param in model.parameters():  # Freeze internal parameters
        param.requires_grad = False

    # Adjust classifier layer
    model.classifier = nn.Sequential(nn.Dropout(p=dropout_p),
                                     nn.Linear(in_features=1280, out_features=out_features))
    return model