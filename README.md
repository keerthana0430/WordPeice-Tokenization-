# WordPeice-Tokenization-
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
