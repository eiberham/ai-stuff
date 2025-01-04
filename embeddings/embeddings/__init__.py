import re
from singletokenizer import SingleTokenizer

with open("the-verdict.txt", "r", encoding="utf-8") as f: raw_text = f.read()
print("Total number of character:", len(raw_text))
print(raw_text[:99])

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
all_words = sorted(set(preprocessed))
all_words.extend(["<|endoftext|>", "<|unk|>"])
vocab = {word: i for i, word in enumerate(all_words)}
tokenizer = SingleTokenizer(vocab)
text = """"It's the last he painted, you know,"
       Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)

# decode the ids back to text
print(tokenizer.decode(ids))