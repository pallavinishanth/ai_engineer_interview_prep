# LLM Interview Questions

## How does LLM works high-level?
An LLM works by predicting the next token (word/part of word) based on the context of previous tokens.
- Input → Tokenization (Text is broken into tokens)
- Convert to Embeddings (Tokens are converted into vectors (numbers))
- Transformer Processing (self-attention → understands relationships between words, multiple layers → learns deeper patterns)
- Context Understanding (Model looks at all tokens and assigns importance)
- Next Token Prediction (Predicts probability of next token)
- Output Generation (Generates tokens one by one)

## Explain transformer architecture in simplest way?
A Transformer is a model that understands text by looking at all words at once and deciding which words are important to each other using attention. Instead of reading word-by-word, it asks: Which words should I focus on? example:
"The bank of the river" -> “bank” pays attention to:“river” (not money)

## Encoder vs Decoder
“The encoder processes and understands the input sequence, while the decoder generates the output sequence token by token using that context.”
Encoder - Takes input text and understands context
Decoder - Uses that understanding to generate output step by step
Encoder-only models (e.g., BERT) - classification, embeddings
Decoder-only models (e.g., GPT) - text generation
Encoder-Decoder models (e.g., T5) - translation, summarization

## What is tokenization and why is it important in LLMs?
Tokenization is the process of breaking text into smaller units called tokens (words, subwords, or characters) so that a model can process it.
- Models understand numbers, not text
- Handles large vocabulary efficiently (Instead of storing every word uses subwords, this reduces vocabulary size)
- Enables context processing (LLM processes sequence of tokens, not characters)
- Affects context window (Limits are based on tokens, not words)
- Impacts cost & performance (More tokens → more cost (API usage), More tokens → higher latency)
Types of tokenization - word-level, sub-word (most common), character-level

## What is context window?
The context window is the maximum number of tokens an LLM can consider at once (input + output). Example: If a model has a 4,000 token context window:Input tokens + Output tokens ≤ 4000
