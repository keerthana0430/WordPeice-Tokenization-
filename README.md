# WordPiece Tokenization From Scratch

## Project Overview

This project demonstrates the implementation of the **WordPiece Tokenization algorithm from scratch using Python in Jupyter Notebook**.

WordPiece is a subword tokenization algorithm widely used by BERT-family models. Instead of selecting the most frequent pair directly, WordPiece calculates a score based on the frequency of the pair and the frequencies of the individual tokens.

This project provides a simple implementation to understand how WordPiece tokenization works internally.

## Objectives

The main objectives of this project are:

* Understand the basic concept of WordPiece tokenization.
* Split words into initial character-level tokens.
* Understand the use of the `##` prefix for continuation tokens.
* Calculate individual token frequencies.
* Calculate adjacent pair frequencies.
* Calculate WordPiece scores.
* Select the highest-scoring pair.
* Merge selected token pairs.
* Tokenize new words using the learned vocabulary.
* Convert tokens into token IDs.
* Understand the use of `[UNK]` for unknown words.

## Tools and Technologies

* Python
* Jupyter Notebook
* Collections module
* Counter

## What is WordPiece?

WordPiece is a subword tokenization algorithm used in models such as BERT.

Instead of treating every complete word as a single token, WordPiece can divide a word into smaller subword units.

For example:

```text
hug
```

can initially be represented as:

```text
h ##u ##g
```

For:

```text
hugs
```

the initial representation is:

```text
h ##u ##g ##s
```

The `##` prefix indicates that the token is a continuation of the same word.

The first token does not contain `##`.

## Training Data

The project uses a small example dataset:

```python
word_freq = {
    "hug": 2,
    "hugs": 1,
    "pug": 1
}
```

The frequency represents how many times each word occurs in the training data.

Initial token splits are:

```python
splits = {
    "hug": ["h", "##u", "##g"],
    "hugs": ["h", "##u", "##g", "##s"],
    "pug": ["p", "##u", "##g"]
}
```

## WordPiece Training Process

The implementation follows these steps:

```text
Training Data
     |
     v
Split Words into Initial Tokens
     |
     v
Calculate Token Frequencies
     |
     v
Calculate Pair Frequencies
     |
     v
Calculate WordPiece Scores
     |
     v
Find Highest-Scoring Pair
     |
     v
Merge the Pair
     |
     v
Update Vocabulary
     |
     v
Repeat the Process
```

## Token Frequency

Token frequency represents how often each individual token occurs in the training data.

For example:

```text
h     = 3
##u   = 4
##g   = 4
##s   = 1
p     = 1
```

These frequencies are used when calculating the WordPiece score.

## Pair Frequency

Pair frequency represents how often two adjacent tokens occur together.

Example:

```text
(h, ##u)       = 3
(##u, ##g)     = 4
(##g, ##s)     = 1
(p, ##u)       = 1
```

## WordPiece Score

The WordPiece score is calculated using:

```text
Score = Pair Frequency / (Frequency of First Token × Frequency of Second Token)
```

In Python:

```python
score = pair_frequency / (
    token_frequency[first] * token_frequency[second]
)
```

The pair with the highest score is selected for merging.

## BPE vs WordPiece

| BPE                            | WordPiece                                            |
| ------------------------------ | ---------------------------------------------------- |
| Selects the most frequent pair | Selects the highest-scoring pair                     |
| Mainly based on pair frequency | Uses pair frequency and individual token frequencies |
| Frequency-based merging        | Score-based merging                                  |
| Used in several NLP models     | Used by BERT-family models                           |

## Token Merging

After calculating the scores, the pair with the highest score is selected.

For example:

```text
##g + ##s
```

can be merged into:

```text
##gs
```

Then:

```text
h ##u ##g ##s
```

becomes:

```text
h ##u ##gs
```

The new token is added to the vocabulary.

This process can be repeated until the desired vocabulary size is reached.

## Tokenization of a New Word

After training, WordPiece tokenization uses the learned vocabulary to tokenize new words.

For example, if the vocabulary contains:

```text
h
p
##u
##g
##s
hu
hug
##gs
```

The word:

```text
hugs
```

can be tokenized as:

```text
["hug", "##s"]
```

WordPiece searches for the longest possible subword from the beginning of the word.

## Token IDs

After tokenization, each token can be converted into a numerical ID using the vocabulary.

Example:

```python
vocab = {
    "[UNK]": 0,
    "h": 1,
    "p": 2,
    "##u": 3,
    "##g": 4,
    "##s": 5,
    "hu": 6,
    "hug": 7,
    "##gs": 8
}
```

For:

```text
hugs
```

the tokens are:

```text
["hug", "##s"]
```

Their token IDs are:

```text
[7, 5]
```

Therefore:

```text
"hugs"
    |
    v
WordPiece Tokenizer
    |
    v
["hug", "##s"]
    |
    v
Vocabulary Lookup
    |
    v
[7, 5]
```

## Handling Unknown Words

If WordPiece cannot completely tokenize a word using the available vocabulary, it returns:

```text
["[UNK]"]
```

For example:

```text
bum
```

may become:

```text
["[UNK]"]
```

This indicates that the complete word could not be represented using the available vocabulary.

## Project Structure

```text
WordPiece-Tokenization/
|
├── WordPiece_Tokenization.ipynb
└── README.md
```

## How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your system.

### Step 2: Install Jupyter Notebook

Open Command Prompt or PowerShell and run:

```bash
python -m pip install notebook
```

### Step 3: Start Jupyter Notebook

Run:

```bash
jupyter notebook
```

### Step 4: Open the Notebook

Open:

```text
WordPiece_Tokenization.ipynb
```

### Step 5: Run the Cells

Run each Python cell one by one using:

```text
Shift + Enter
```

The notebook displays the token frequencies, pair frequencies, WordPiece scores, selected pairs, merged tokens, tokenization results, and token IDs.

## Key Learning Outcomes

After completing this project, the following concepts can be understood:

1. Subword tokenization.
2. Character-level token initialization.
3. Continuation tokens using `##`.
4. Token frequency calculation.
5. Pair frequency calculation.
6. WordPiece score calculation.
7. Token pair merging.
8. Vocabulary construction.
9. Longest-subword matching.
10. Unknown token handling.
11. Conversion of tokens into token IDs.
12. Difference between BPE and WordPiece.

## Conclusion

This project provides a simple implementation of **WordPiece Tokenization from scratch using Python and Jupyter Notebook**.

The implementation helps understand the internal working of WordPiece without relying on pre-built tokenization libraries. It demonstrates how a vocabulary can be constructed by calculating token frequencies, pair frequencies, WordPiece scores, and repeatedly merging the best-scoring token pairs.

The project is useful for understanding the tokenization process used in modern Natural Language Processing and BERT-family models.

