#Creating Tokens

with open ("the-verdict.txt", "r", encoding = "utf-8") as f:
    raw_text = f.read()

print("Total number of character:", len(raw_text))
print(raw_text[:99])

import re
from SimpleTokenizer import SimpleTokenizerV1
from SimpleTokenizer import SimpleTokenizerV2

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)',raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed[:30])

#Creating Token ID's

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)

print(vocab_size) 

vocab = {token:integer for integer,token in enumerate(all_words)}

for i, item in enumerate(vocab.items()):
    print(item)
    if i>= 50:
        break

tokenizer = SimpleTokenizerV1(vocab)
text = raw_text
ids = tokenizer.encode(text)
print(ids)

ad = tokenizer.decode(ids)


#################
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

vocab = {token:integer for integer, token in enumerate(all_tokens)}

tokenizer2 = SimpleTokenizerV2(vocab)
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = "<|endoftext|>".join((text1, text2))
print(text)

print(tokenizer2.encode(text))

print(tokenizer2.decode(tokenizer2.encode(text)))


