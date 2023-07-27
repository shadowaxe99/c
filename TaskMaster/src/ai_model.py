```python
import torch
import torch.nn as nn
import torch.optim as optim

class TaskMasterModel(nn.Module):
    def __init__(self):
        super(TaskMasterModel, self).__init__()
        self.layer1 = nn.Linear(100, 200)
        self.layer2 = nn.Linear(200, 100)
        self.layer3 = nn.Linear(100, 50)
        self.output_layer = nn.Linear(50, 10)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = torch.relu(self.layer3(x))
        x = self.output_layer(x)
        return x

def train_model(model, train_loader, criterion, optimizer, n_epochs):
    model.train()
    for epoch in range(n_epochs):
        for data, target in train_loader:
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

def save_model(model, path):
    torch.save(model.state_dict(), path)

def load_model(model, path):
    model.load_state_dict(torch.load(path))
    model.eval()

model = TaskMasterModel()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Assuming train_loader is defined and provides the training data
# train_model(model, train_loader, criterion, optimizer, n_epochs=10)

# Save the trained model
# save_model(model, "TaskMaster/FINISHED/taskmaster_model.pth")

# Load the trained model
# load_model(model, "TaskMaster/FINISHED/taskmaster_model.pth")
```