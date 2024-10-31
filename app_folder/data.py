import torchvision
import torch
from torch.utils.data import Dataloader, random_split

from pathlib import Path



def create_food101_dataset(data_path : str,
                           download : bool=False,
                           subset_size : float=None,
                           transforms=torchvision.transforms.ToTensor()):
    """
    Create Datasets containing images from the Food101 Image Dataset.

    Args:
        data_path (str) : 
        download (bool) : 
        subset_size (float) : 
        transforms : 

    Output : 

    """

    # Create data directory
    data_dir = Path(data_path)
    if data_dir.is_dir():
        None
    else:
        data_dir.mkdir(parents=True, exist_ok=True)

    # Create training & testing datasets from Food101 image dataset
    train_data = torchvision.datasets.Food101(root=data_dir, split="train",
                                        download=download, transform=transforms)
    test_data = torchvision.datasets.Food101(root=data_dir, split="test",
                                    download=download, transform=transforms)
    
    # Create subsets if 'subset_size' is specified
    if subset_size:
        train_subset_length = round(subset_size*len(train_data))
        train_data_subset, _ = random_split(train_data, lengths=[train_subset_length, len(train_data)-train_subset_length])

        test_subset_length = round(subset_size*len(test_data))
        test_data_subset, _ = random_split(test_data, lengths=[test_subset_length, len(test_data)-test_subset_length])

        return train_data_subset, test_data_subset
    else:
        return train_data, test_data


