import lightning as L
from model import NN
from dataset import MnistDataModule
import config

if __name__ == "__main__":

    dm = MnistDataModule(data_dir="dataset/",  batch_size=config.BATCH_SIZE, num_workers=config.NUM_WORKERS)
    # Initialize the network

    model = NN(input_size=config.INPUT_SIZE, learning_rate=config.LEARNING_RATE, num_classes=config.NUM_CLASSES).to(device)
    # Trainer

    trainer = L.Trainer(accelerator=config.ACCELERATOR, 
                        config.DEVICES, 
                        min_epochs=MIN_EPOCHS,
                        max_epochs=config.MX_EPOCHS, 
                        enable_model_summary=True, 
                        precision=config.PRECISION
                    )
    #trainer.tune() -> find the optima hyperparameters (lr, batch size etc)
    trainer.fit(model, dm)
    trainer.validate(model, dm)
    trainer.test(model, dm)