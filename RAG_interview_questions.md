# RAG Interview Questions

## What are the key steps involved in the Retrieval-Augmented Generation (RAG) pipeline?

"RAG involves ingesting and chunking documents, generating embeddings, storing them in a vector database, retrieving relevant context based on a user query, and augmenting the prompt to generate grounded responses from an LLM."

## What's your chunking strategy - by length, semantics, or structure?

### Length-based chunking
- Split text by token/character size

### Overlap
- Add overlap between chunks

### Structure-based chunking
Split based on:
- Headings
- Paragraphs
- Sections

### Semantic chunking
- Split based on meaning (embedding similarity)