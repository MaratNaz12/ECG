import torch.optim
import hydra
from omegaconf import DictConfig
import logging
log = logging.getLogger(__name__)

import data_preparation as dp
import model as mdl
import training as tr
import visualization as vs
import evaluation as evl


@hydra.main(version_base=None, config_path="conf", config_name="config")
def train(cfg : DictConfig) -> None:

    train_dataset,valid_dataset,test_dataset = dp.DatasetCreation(cfg.dataset)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    model = mdl.RhythmECGClassification(12,1)

    optim = hydra.utils.instantiate(cfg.optim)
  

    trained_model, train_history = tr.train_model (model, optim, device, train_dataset, valid_dataset, cfg.epoches)

    vs.visual_resisual_res(train_history, cfg.epoches)

    log.info(f'train_history: {train_history}')

    test_metrics = evl.evaluate(trained_model, test_dataset,device)

    log.info(f'history: {test_metrics}')



    
train()