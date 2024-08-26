import pickle

# Load the pickled object
with open('/content/pipe.pkl', 'rb') as file:
    data = pickle.load(file)

# Print the type of the loaded object
print(f"Type of loaded object: {type(data)}")

# Optionally, print some content if it's not too large
print(data)
