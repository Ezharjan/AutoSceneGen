import matplotlib.pyplot as plt
import numpy as np

# Initialize lists to store the data
epochs = []
train_loss_vals = []
valid_loss_vals = []

# Read the data from the file
# with open('../log/log_curve.txt', 'r') as file:
# with open('../log-original/log_curve.txt', 'r') as file:
# with open('../log-(A5)/log_curve.txt', 'r') as file:
# with open('../log-(A5+B48)/log_curve.txt', 'r') as file:
# with open('../log-(A5+B)/log_curve.txt', 'r') as file:
with open('../log-(B10)/log_curve.txt', 'r') as file:
    for line in file:
        # Split the line by commas and convert to floats
        epoch, train_loss, valid_loss = map(float, line.strip().split(','))
        epochs.append(epoch)
        train_loss_vals.append(train_loss)
        valid_loss_vals.append(valid_loss)

# Convert lists to numpy arrays for easier handling
epochs = np.array(epochs)
train_loss_vals = np.array(train_loss_vals)
valid_loss_vals = np.array(valid_loss_vals)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(epochs, train_loss_vals, label='Training Loss', marker='o')
plt.plot(epochs, valid_loss_vals, label='Validation Loss', marker='x')

# Add titles and labels
plt.title('Log Curve Data Visualization')
plt.xlabel('Epochs')
plt.ylabel('Loss Values')
plt.legend()

# Show the plot
plt.show()