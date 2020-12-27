import markovify

# Get raw text as string.
with open("gloomarkov.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print a randomly-generated sentence
print(text_model.make_sentence())