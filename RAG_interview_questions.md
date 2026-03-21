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

“The best chunking strategy is hybrid—starting with structure-aware splitting to preserve semantic meaning, followed by length-based chunking with overlap. This balances retrieval accuracy, context preservation, and performance.”

## How do you evaluate RAG pipeline?

Evaluating a RAG system involves assessing both retrieval and generation. Retrieval is measured using metrics like Precision@k, Recall@k, and (Mean Reciprocal Rank) MRR to ensure relevant documents are returned. Generation is evaluated for faithfulness (avoiding hallucinations) and relevance using benchmarks, llm-as-a-judge, semantic similarity, and overlap with the query. Finally, human evaluation and user feedback are essential to assess usefulness, trustworthiness, and overall response quality.

## How do you reduce hallucinations in RAG based application?
Improve retrieval quality, Use better chunking, Re-rank retrieved results, Limit context to high-quality evidence, Use a strong grounding prompt, Allow “I don’t know”, Add citations, Validate retrieval confidence, Query rewriting, Filter stale or conflicting documents, Use answer verification, Tune generation settings, Add guardrails.

## When to use RAG and when to fine-tune?
Use RAG when you need up-to-date, external knowledge retrieval, and use fine-tuning when you want the model to learn specific behavior, style, or domain patterns.

Use RAG when:
	•	data changes frequently
	•	you need real-time / up-to-date info
	•	large document corpus
	•	need citations / traceability
	•	enterprise knowledge base
Use fine-tuning when:
	•	you want consistent behavior/style
	•	domain-specific language needed
	•	structured outputs required
	•	repeated task pattern

## What is indexing in RAG?
Indexing is the process of converting raw documents into a structured, searchable format (usually embeddings) so they can be retrieved efficiently. Load Data -> chunking (split data into smaller pieces) -> convert each chunk into embedding vector -> store in vector database -> Index creation (Vector DB organizes vectors for fast search using ANN or similarity search)

Indexing is essential for fast retrieval, enables semantic search, scales to large data, improves RAG quality (better chunks -> better response)

## Explain Document loading/ingestion step in RAG? 
For RAG applications we might have to read data from multiple sources/formats like PDF's, Word docs, text files, web pages, from cloud, databases, API's etc. In LangChain Document Loaders convert any data to Document objects with page_content and metadata. Metadata is important for citations, filtering, debugging and access control. 

Loading is just reading documents, where as ingestion is broader than just loading its full pipeline to make them searchable in RAG. Ingestion includes loading, cleaning, normalization, deduplication, chunking, embedding, indexing into vector store.

## How do you secure data in overall RAG pipeline?
Secure a RAG pipeline by enforcing access control, protecting data at rest and in transit, filtering sensitive data, applying guardrails at the LLM layer, and ensuring auditability and monitoring across the pipeline.
Think in layers "Data Source → Ingestion → Storage → Retrieval → LLM → Response"
- Data Source: protect raw data using role-based access control (RBAC), Encryption at rest (S3, DB), secure API's
- Ingestion: While loading data mask or remove PII, validate sources, avoid ingesting sensitive data/unapproved data
- Storage: encryption at rest, access policies, metadata-based filtering
- Retrieval security: Enforce access control during retreival
- LLM layer security: prevent prompt injection, prevent data leakage, ground responses
- Response security: redact sensitive info, apply output filters, limit exposure
  
Above all monitoring & logging, audit & compliance, network security, identity and access are also important.

## Design a RAG system for enterprise documents?

**Ingestion**

First, I’d ingest documents from multiple enterprise sources:
- SharePoint, Confluence, internal portals
- PDFs, Word docs, policies, SOPs
- structured sources like databases or APIs

At ingestion time I’d:
- extract text
- preserve metadata like source, owner, document type, department, created date, sensitivity
- normalize format
- deduplicate documents
- version documents so updates don’t create confusion

For parsing, I’d use source-specific loaders and a common document schema.

**Chunking strategy**

For enterprise documents, I would use a hybrid chunking strategy:
- structure-aware first, using headings, sections, tables where possible
- then length-based chunking with overlap

Typical setup:
- 500–1000 token chunks
- 10–20% overlap

Why:
- keeps business meaning intact
- avoids losing context at boundaries
- improves retrieval precision

**Embeddings and Indexing**

For enterprise documents, I would use a hybrid chunking strategy:
	•	structure-aware first, using headings, sections, tables where possible
	•	then length-based chunking with overlap

Typical setup:
	•	500–1000 token chunks
	•	10–20% overlap

Why:
	•	keeps business meaning intact
	•	avoids losing context at boundaries
	•	improves retrieval precision

**Retreival layer**

At query time:
	1.	authenticate the user
	2.	apply metadata and permission filters
	3.	convert query to embedding
	4.	retrieve top-k chunks
	5.	optionally re-rank results
	6.	send best evidence to the LLM

I’d use:
	•	semantic retrieval for meaning
	•	keyword search for exact terms
	•	re-ranking to improve final relevance

This is especially useful when documents are large or from mixed departments.

**Generation layer**

The LLM should not answer freely. I’d constrain it with a grounded prompt like:
	•	answer only from provided context
	•	cite sources
	•	if answer is missing, say you don’t know

The output should include:
	•	final answer
	•	supporting citations
	•	confidence or evidence references

This improves trust and reduces hallucinations.

**Security and Governance**

For enterprise RAG, this is critical.

I’d enforce:
	•	RBAC / user-based authorization
	•	document-level and metadata-based filtering
	•	encryption at rest and in transit
	•	logging and audit trails
	•	PII masking where required
	•	prompt injection safeguards
	•	approved model usage only

A user should only retrieve documents they are authorized to access.

**Evaluation**

I’d evaluate both retrieval and generation.

Retriever metrics
	•	Precision@k
	•	Recall@k
	•	MRR

Generator metrics
	•	faithfulness
	•	relevance
	•	citation correctness
	•	hallucination rate

System metrics
	•	latency
	•	cost
	•	user satisfaction
	•	adoption

I’d also include human review and feedback loops.

**Monitoring**

In production I’d monitor:
	•	failed retrievals
	•	low-confidence queries
	•	latency spikes
	•	hallucination complaints
	•	source freshness
	•	drift in document quality

Then use feedback for:
	•	chunking improvements
	•	retriever tuning
	•	prompt changes
	•	source cleanup

	
## How would you build a chatbot over internal data?
## How would you scale RAG for millions of documents?
## How do you handle multi-tenant RAG systems?
