from torchvision import transforms
from torchvision.datasets import ImageFolder
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from model import ConvNet

# Load dataset into ImageFolder
dataset_root = "../image_data"

#transform image to the same size
transforms = transforms.Compose([
    transforms.RandomResizedCrop(size=(28, 28), antialias=True),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.ToTensor(),
])
dataset = ImageFolder(dataset_root, transform=transforms)

# user cuda to run if cuda is available
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Define the sizes for training, validation, and test sets
# Split dataset into DataLoader
train_size = int(0.8 * len(dataset))  
test_size = len(dataset) - train_size

train_set, test_set = random_split(dataset, [train_size, test_size])
train_loader = DataLoader(train_set, batch_size=32, shuffle=True)
test_loader = DataLoader(test_set, batch_size=32, shuffle=False)

# Model
model = ConvNet(len(dataset.classes))
model.to(device)

# Train & Test
# Define epochs_size, loss function and optimizer
epochs_size=30
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=0.001)

# Train the model
def train(model, train_loader, criterion, optimizer, num_epochs=epochs_size):
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        print(f"Epoch {epoch+1}/{num_epochs}, "
              f"Train Loss: {running_loss/len(train_loader):.4f}, ")

# Call the train function
train(model, train_loader, criterion, optimizer, num_epochs=epochs_size)

# Test the model
def test(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f"Test Accuracy: {(correct/total)*100:.2f}%")

# Call the test function
test(model, test_loader)

# Save the model
torch.save(model.state_dict(), 'model_'+str(epochs_size)+'.pth')