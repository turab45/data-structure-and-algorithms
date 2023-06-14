import torch
from torchvision import transforms
from torchvision import datasets
from torch.utils.data.dataset import random_split
from torch.utils.data.dataloader import DataLoader
import lightning as L

class MnistDataModule(L.LightningDataModule):
  def __init__(self, data_dir, batch_size, num_workers):
    super().__init__()
    self.data_dir = data_dir
    self.batch_size = batch_size
    self.num_workers = num_workers
  
  def prepare_data(self): 
    """
    Tip: If you have the dataset already downloaded in a directory, then this step is not necessary. skip this.
    """
    # download, tokenize (text data), etc...
    datasets.MNIST(self.data_dir, train=True, download=True)
    datasets.MNIST(self.data_dir, train=False, download=True)
    
  
  def setup(self, stage: str): #stage: fit, validate, test, predict etc...
    # transform, split, etc...
    entire_dataset = datasets.MNIST(root=self.data_dir,
                           train=True,
                           transform=transforms.ToTensor(),
                           download=False)
    self.train_ds, self.val_ds = random_split(entire_dataset, [50000, 10000])
    self.test_ds = datasets.MNIST(root=self.data_dir,
                           train=False,
                           transform=transforms.ToTensor(),
                           download=False)
  
  def train_dataloader(self):
    return DataLoader(self.train_ds,
                      batch_size=self.batch_size,
                      num_workers=self.num_workers,
                      shuffle=True)
  
  def val_dataloader(self):
    return DataLoader(self.val_ds,
                      batch_size=self.batch_size,
                      num_workers=self.num_workers,
                      shuffle=False)
  
  def test_dataloader(self):
    return DataLoader(self.test_ds,
                      batch_size=self.batch_size,
                      num_workers=self.num_workers,
                      shuffle=False)