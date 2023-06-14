import lightning as L
from lightning.pytorch.callbacks import EarlyStopping
from model import NN
from dataset import MnistDataModule
import config
from lightning.pytorch.loggers import TensorBoardLogger

if __name__ == "__main__":
    logger = TensorBoardLogger("tb_logs", name="mnist_model_v0")

    dm = MnistDataModule(data_dir="dataset/",  batch_size=config.BATCH_SIZE, num_workers=config.NUM_WORKERS)
    # Initialize the network

    model = NN(input_size=config.INPUT_SIZE, learning_rate=config.LEARNING_RATE, num_classes=config.NUM_CLASSES).to(device)
    # Trainer

    trainer = L.Trainer(accelerator=config.ACCELERATOR, 
                        config.DEVICES, 
                        min_epochs=MIN_EPOCHS,
                        max_epochs=config.MX_EPOCHS, 
                        enable_model_summary=True, 
                        precision=config.PRECISION,
                        callbacks=[EarlyStopping(monitor="val_loss", patience=5)],
                        logger=logger
                    )
    #trainer.tune() -> find the optima hyperparameters (lr, batch size etc)
    trainer.fit(model, dm)
    trainer.validate(model, dm)
    trainer.test(model, dm)