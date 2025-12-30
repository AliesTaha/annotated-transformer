import numpy as np
import matplotlib.pyplot as plt

def get_positional_encoding(max_seq_len, d_model):
    # Initialize the matrix with zeros
    encoding = np.zeros((max_seq_len, d_model))
    
    # Calculate the positions (t) and the frequencies (based on k)
    positions = np.arange(max_seq_len)[:, np.newaxis] # Shape: (max_seq_len, 1)
    # The 'k' index is divided by 2 because we use it for both sine and cosine
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))
    
    # Apply sine to even indices (2i)
    encoding[:, 0::2] = np.sin(positions * div_term)
    
    # Apply cosine to odd indices (2i + 1)
    encoding[:, 1::2] = np.cos(positions * div_term)
    
    return encoding

# Parameters matching a standard small Transformer
MAX_LEN = 128
D_MODEL = 512

pe = get_positional_encoding(MAX_LEN, D_MODEL)

# Visualization
plt.figure(figsize=(12, 8))
plt.pcolormesh(pe, cmap='RdBu')
plt.xlabel('Embedding Dimension (d_model)')
plt.ylabel('Token Position (t)')
plt.colorbar(label='Encoding Value')
plt.title("Positional Encoding Matrix")
plt.show()