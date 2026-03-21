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

<u>**Ingestion**</u>

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

Each chunk would be converted into embeddings and stored in a vector database.

I’d store:
-	chunk text
-	embedding vector
-	metadata
-	document ID / version
-	access-control tags

For indexing:
-	vector index for semantic search
-	optional keyword/full-text index for exact matches
-	hybrid search for best enterprise performance

This is important because enterprise users often search both semantically and exactly, like:
-	“travel reimbursement policy”
-	exact “policy number 1042”

**Retreival layer**

At query time:
-	authenticate the user
-	apply metadata and permission filters
-	convert query to embedding
-	retrieve top-k chunks
-	optionally re-rank results
-	send best evidence to the LLM

I’d use:
-	semantic retrieval for meaning
-	keyword search for exact terms
-	re-ranking to improve final relevance

This is especially useful when documents are large or from mixed departments.

**Generation layer**

The LLM should not answer freely. I’d constrain it with a grounded prompt like:
-	answer only from provided context
-	cite sources
-	if answer is missing, say you don’t know

The output should include:
-	final answer
-	supporting citations
-	confidence or evidence references

This improves trust and reduces hallucinations.

**Security and Governance**

For enterprise RAG, this is critical.

I’d enforce:
-	RBAC / user-based authorization
-	document-level and metadata-based filtering
-	encryption at rest and in transit
-	logging and audit trails
-	PII masking where required
-	prompt injection safeguards
-	approved model usage only

A user should only retrieve documents they are authorized to access.

**Evaluation**

I’d evaluate both retrieval and generation.

Retriever metrics
-	Precision@k
-	Recall@k
-	MRR

Generator metrics
-	faithfulness
-	relevance
-	citation correctness
-	hallucination rate

System metrics
-	latency
-	cost
-	user satisfaction
-	adoption

I’d also include human review and feedback loops.

**Monitoring**

In production I’d monitor:
-	failed retrievals
-	low-confidence queries
-	latency spikes
-	hallucination complaints
-	source freshness
-	drift in document quality

Then use feedback for:
-	chunking improvements
-	retriever tuning
-	prompt changes
-	source cleanup


## How would you scale RAG for millions of documents?
For millions of docs, ingestion must be asynchronous and incremental.

I’d do:
	•	distributed document loading
	•	deduplication
	•	versioning
	•	change detection
	•	incremental re-indexing only for changed documents

Important:
	•	don’t re-embed everything on every update
	•	process only new or modified docs

2. Chunk intelligently

Bad chunking explodes index size.

I’d use:
	•	structure-aware chunking first
	•	then length-based chunking with overlap
	•	metadata per chunk: source, doc type, owner, department, date, permissions

This helps retrieval quality and later filtering.

3. Generate embeddings in batch

Embedding millions of documents is expensive, so I’d:
	•	run batch embedding jobs
	•	parallelize across workers
	•	cache embeddings for unchanged chunks
	•	use queues for ingestion jobs

4. Use a scalable vector store

For millions of chunks, you need:
	•	approximate nearest neighbor search
	•	sharding / partitioning
	•	replication
	•	metadata filtering

I’d choose a vector DB or search platform that supports:
	•	ANN indexes
	•	horizontal scaling
	•	hybrid search
	•	fast metadata filtering

5. Partition the index

A single giant index is inefficient.

I’d partition by useful dimensions like:
	•	business unit
	•	geography
	•	document type
	•	tenant
	•	security boundary

That reduces search space and improves latency.

6. Use hybrid retrieval

At scale, semantic-only search is often not enough.

I’d combine:
	•	vector search for semantic meaning
	•	keyword / BM25 / full-text for exact matches
	•	metadata filters for narrowing scope

This is especially important in enterprise systems with IDs, policy numbers, codes, names.

7. Add re-ranking

Initial retrieval over millions of chunks can be noisy.

Flow:
	•	retrieve top 50–100 candidates cheaply
	•	re-rank top candidates with stronger model
	•	send only best few chunks to LLM

This improves quality without making first-stage retrieval too expensive.

8. Pre-filter before vector search

Don’t search all documents if you already know the scope.

Use:
	•	user permissions
	•	recency
	•	doc type
	•	department
	•	source
	•	language

This is critical for both scale and security.

9. Separate offline and online systems

Use different paths for:
	•	offline ingestion/index building
	•	online low-latency query serving

That way indexing jobs don’t affect live query latency.

10. Cache aggressively

At scale, many questions repeat.

Cache:
	•	embeddings for repeated queries
	•	retrieval results for popular queries
	•	final answers where safe
	•	reranker outputs if useful

11. Control context size

With millions of docs, retrieval can overwhelm the LLM.

So I’d:
	•	keep top-k small after reranking
	•	compress context if needed
	•	merge duplicate evidence
	•	avoid passing too many similar chunks

12. Monitor retrieval quality and latency

At this scale, monitoring is mandatory.

Track:
	•	Precision@k / Recall@k / MRR
	•	latency per stage
	•	embedding job failures
	•	stale index percentage
	•	cache hit rate
	•	query volume by partition
	•	hallucination / unsupported answer rate

13. Handle freshness and updates

For enterprise docs, freshness matters.

I’d support:
	•	delta ingestion
	•	tombstoning deleted docs
	•	version-aware retrieval
	•	priority indexing for critical docs

14. Secure it properly

For millions of enterprise documents:
	•	enforce row/document-level access
	•	filter by ACL before retrieval
	•	encrypt at rest and in transit
	•	log access and citations


## How do you handle multi-tenant RAG systems?
A multi-tenant RAG system means one platform serves multiple teams, customers, or business units, while keeping their data isolated and secure.
I handle multi-tenant RAG by designing for:
-	strict tenant isolation
-	tenant-aware ingestion and indexing
-	tenant-scoped retrieval
-	access-controlled generation
-	observability and cost tracking per tenant

**Data Isolation**: I would isolate tenant data using one of these patterns -  Separate index per tenant, Shared index with tenant metadata filters or hybrid approach (separate indexes for high-risk / regulated tenants, shared indexes for low-risk tenants)
**Tenant aware isolation**: During ingestion, I would tag every document and chunk with tenant metadata: Tenant source docs
   ->
Parse + chunk
   ->
Attach tenant metadata
   ->
Embed
   ->
Store in tenant-scoped index

**Retrieval security**: At query time, I would enforce isolation before generation.
User query
   ->
Authenticate user
   ->
Resolve tenant + role
   ->
Apply tenant filter + access filter
   ->
Retrieve documents
   ->
Generate response

Important:
-	never retrieve across tenants unless explicitly allowed
-	apply ACL filtering before or during retrieval
-	include document-level permissions, not just tenant-level

Example:
A user from Tenant A should never see chunks from Tenant B, even if they are semantically relevant.

**Separate auth from retrieval logic**
I would integrate with enterprise identity:
-	SSO / OAuth / SAML
-	RBAC / ABAC
-	group membership
-	tenant-scoped tokens

Then pass those claims into retrieval filters.

**Tenant-specific configurations**
Different tenants may need different settings:
-	different embedding models
-	different chunking strategies
-	different prompt templates
-	different LLM providers
-	different retention rules
-	different guardrails

So I’d make the platform configurable per tenant, but through a controlled config layer.
Tenant A → Bedrock + strict compliance prompt
Tenant B → Vertex AI + broader internal search

**Prompt and generation safeguards**
The LLM should only see retrieved context from the allowed tenant scope.

I’d also:
-	include tenant-specific system prompts
-	restrict source usage
-	require citations
-	prevent cross-tenant memory leakage
-	disable shared conversational memory across tenants

This is very important if chat history exists.

**Monitoring and auditability**
For enterprise systems, I’d track metrics per tenant:
-	query volume
-	latency
-	cost
-	retrieval quality
-	hallucination / fallback rate
-	source usage
-	access denials

Also keep audit logs for:
-	who queried what
-	which documents were retrieved
-	what response was generated

This helps with compliance and debugging.

**Overall architecture**

Tenant Sources
   ->
Tenant-aware ingestion pipeline
   ->
Chunking + metadata tagging
   ->
Embeddings
   ->
Vector store / hybrid search
   ->
Tenant + ACL filtered retrieval
   ->
LLM generation with citations
   ->
Per-tenant logging, monitoring, billing

Summary:
"I handle multi-tenant RAG by making the entire pipeline tenant-aware, from ingestion to retrieval and generation. Every document and chunk is tagged with tenant metadata, and retrieval always applies tenant and access-control filters before sending context to the LLM. Depending on security requirements, I would use either separate indexes per tenant or a shared index with strict metadata filtering. I’d also isolate cache keys, prompts, logs, and monitoring by tenant, and support tenant-specific compliance, configuration, and cost tracking."

