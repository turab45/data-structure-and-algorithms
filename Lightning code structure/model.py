import torch
from torch import nn
import torch.nn.functional as F
import lightning as L
import torchmetrics

class NN(L.LightningModule):
  def __init__(self, input_size, learning_rate, num_classes) -> None:
      super().__init__()
      self.lr = learning_rate
      # add network layers
      self.fc1 = nn.Linear(in_features=input_size, out_features=50)
      self.fc2 = nn.Linear(in_features=50, out_features=num_classes)
      self.loss_fn = nn.CrossEntropyLoss()
      self.accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=num_classes)
      self.f1_score = torchmetrics.F1Score(task="multiclass", num_classes=num_classes)
  
  def forward(self, x):
    x = F.relu(self.fc1(x))
    x = self.fc2(x)
    return x
  
  def training_step(self, batch, batch_idx):
    loss, scores, y = self._common_step(batch, batch_idx)
    accuracy = self.accuracy(scores, y)
    f1_score = self.f1_score(scores, y)
    self.log_dict({"train_loss: ":loss, "train_accuracy:":accuracy, "train_f1_score:":f1_score},
                  on_step=False, on_epoch=True, prog_bar=True)
    return loss
  
  def validation_step(self, batch, batch_idx):
    loss, scores, y = self._common_step(batch, batch_idx)
    self.log("Validation loss: ", loss)
    return loss
  
  def test_step(self, batch, batch_idx):
    loss, scores, y = self._common_step(batch, batch_idx)
    self.log("Test loss: ", loss)
    return loss
  
  def predict_step(self, batch, batch_idx):
    x, y = batch
    x = x.reshape(x.size(0), -1)
    scores = self.forward(x)
    preds = torch.argmax(scores, dim=1)
    return preds

  # Optional, just to make the code look clean
  def _common_step(self, batch, batch_idx):
    x, y = batch
    x = x.reshape(x.size(0), -1)
    scores = self.forward(x)
    loss = self.loss_fn(scores, y)
    return loss, scores, y
  
  def configure_optimizers(self):
    optimizer = torch.optim.Adam(self.parameters(), lr=self.lr)
    return optimizer