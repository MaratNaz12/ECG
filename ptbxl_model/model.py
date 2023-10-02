import torch.nn as nn




class RhythmECGClassification(nn.Module):

    def __init__(self, in_channels, out_channels):

        super(RhythmECGClassification, self).__init__()

        self.in_channels = in_channels

        self.relu = nn.ReLU()

        self.block0 = nn.Sequential(nn.Conv1d(in_channels, 64, kernel_size=7, stride=2, padding=3),
                                    nn.BatchNorm1d(64),
                                    nn.ReLU(), nn.MaxPool1d(kernel_size=3, stride=2, padding=1))

        self.block1 = nn.Sequential(nn.Conv1d(64,64, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(64),
                                    nn.ReLU(),
                                    nn.Conv1d(64,64, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(64))

        self.block2 = nn.Sequential(nn.Conv1d(64,128, kernel_size = 3, stride = 2, padding = 1),
                                    nn.BatchNorm1d(128),
                                    nn.ReLU(),
                                    nn.Conv1d(128,128, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(128))

        self.block3 = nn.Sequential(nn.Conv1d(128,128, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(128),
                                    nn.ReLU(),
                                    nn.Conv1d(128,128, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(128))

        self.block4 = nn.Sequential(nn.Conv1d(128,256, kernel_size = 3, stride = 2, padding = 1),
                                    nn.BatchNorm1d(256),
                                    nn.ReLU(),
                                    nn.Conv1d(256,256, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(256))

        self.block5 = nn.Sequential(nn.Conv1d(256,256, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(256),
                                    nn.ReLU(),
                                    nn.Conv1d(256,256, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(256))

        self.block6 = nn.Sequential(nn.Conv1d(256,512, kernel_size = 3, stride = 2, padding = 1),
                                    nn.BatchNorm1d(512),
                                    nn.ReLU(),
                                    nn.Conv1d(512,512, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(512))

        self.block7 = nn.Sequential(nn.Conv1d(512,512, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(512),
                                    nn.ReLU(),
                                    nn.Conv1d(512,512, kernel_size = 3, stride = 1, padding = 1),
                                    nn.BatchNorm1d(512))

        self.block8 = nn.Sequential(nn.AdaptiveAvgPool1d(1), nn.Flatten(),
                                    nn.Linear(512, 1000), nn.ReLU(),
                                    nn.Linear(1000,out_channels), nn.Sigmoid())

        self.ident1 = nn.Sequential(nn.Conv1d(64, 128, kernel_size=3, stride=2, padding=1),
                                    nn.BatchNorm1d(128))

        self.ident2 = nn.Sequential(nn.Conv1d(128, 256, kernel_size=3, stride=2, padding=1),
                                    nn.BatchNorm1d(256))

        self.ident3 = nn.Sequential(nn.Conv1d(256, 512, kernel_size=3, stride=2, padding=1),
                                    nn.BatchNorm1d(512))


    def forward(self, x):

        x = self.block0(x)

        for i in range (3):
            identity = x
            x = self.block1(x) + identity
            x = self.relu(x)

        identity = self.ident1(x)
        x = self.block2(x) + identity
        x = self.relu(x)

        for i in range (3):
            identity = x
            x = self.block3(x) + identity
            x = self.relu(x)

        identity = self.ident2(x)
        x = self.block4(x) + identity
        x = self.relu(x)

        for i in range (5):
            identity = x
            x = self.block5(x) + identity
            x = self.relu(x)

        identity = self.ident3(x)
        x = self.block6(x) + identity
        x = self.relu(x)

        for i in range (2):
            identity = x
            x = self.block7(x) + identity
            x = self.relu(x)

        x = self.block8(x)
        return x


    def training_step(self,batch):
        signals,targets = batch
        preds = self(signals)
        loss = nn.BCELoss(reduction='sum')
        return loss(preds, targets.unsqueeze(1))


    def validation_step(self,batch):
        signals,targets = batch
        preds = self(signals.float())
        return preds