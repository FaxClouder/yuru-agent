# YuruAgent Roadmap and Phase Plan

YuruAgent is a personal automation agent workspace for building, running, and observing extensible AI agents.

The project roadmap is organized by modules and capability maturity instead of fixed calendar deadlines. The memory module will reference the design ideas of [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU), especially memory file systems, typed memory, source traceability, layered organization, and hybrid retrieval. The first implementation will be a lightweight YuruAgent-native version, not a direct memU integration.

## Technical Direction

```text
Next.js + FastAPI + LangGraph + PostgreSQL + pgvector
```

The first runnable product loop is:

```text
Create Agent
-> Configure Prompt
-> Run Task
-> Stream Output
-> Save Run History
-> Review Trace
-> Enhance Context with Memory and RAG
```

## Phase 0: Project Foundation

Goal: establish the engineering foundation and project management system.

Features:

- Monorepo project structure.
- Next.js frontend foundation.
- FastAPI backend foundation.
- PostgreSQL local development environment.
- README, roadmap, and architecture documentation.
- GitHub Issues, milestones, and labels convention.

Done when:

- Frontend and backend can start locally.
- Backend provides a health check.
- Database connection works.
- Documentation explains the project direction, architecture, and phase rules.

## Phase 1: Agent Workspace

Goal: support agent creation, management, and base configuration.

Core model:

```text
Agent
- id
- name
- description
- system_prompt
- model
- memory_enabled
- rag_enabled
- created_at
- updated_at
```

Features:

- Agent list.
- Agent create, edit, delete.
- Agent detail.
- System prompt configuration.
- Default model configuration.
- Memory and RAG toggles.

Done when:

- Users can create, view, update, and delete agents.
- Agents can save prompt, model, memory, and RAG settings.
- Frontend and backend complete the agent management loop.

## Phase 2: Agent Runner

Goal: implement the minimal runnable agent loop.

Core model:

```text
AgentRun
- id
- agent_id
- user_task
- status
- final_output
- error_message
- started_at
- completed_at
```

Core APIs:

```text
POST /api/agents/{agent_id}/runs
GET  /api/runs/{run_id}
GET  /api/runs/{run_id}/events
```

Features:

- User task input.
- AgentRun creation.
- Single-node LangGraph execution.
- SSE streaming output.
- Final output and error persistence.

Done when:

- Users can run an agent.
- Frontend can display streamed output.
- Successful and failed runs are saved.
- Historical runs can be queried.

## Phase 3: Traceable Runs

Goal: make agent execution traceable, explainable, and reviewable.

Core model:

```text
AgentStep
- id
- run_id
- name
- type
- status
- input_json
- output_json
- error_message
- started_at
- completed_at
```

Features:

- AgentRun detail page.
- Step timeline.
- Step input and output display.
- Failed step identification.
- Execution duration display.

Done when:

- Users can inspect the full step timeline of a run.
- Each step has input, output, status, error, and timing fields.
- Failed runs can be traced to the failed step.

## Phase 4: Agent Memory

Goal: implement an auditable, searchable, source-traceable long-term memory system for agents.

Design principles:

- Memory is not RAG. Memory records user preferences, interaction facts, task experience, and behavior patterns learned from agent runs. RAG retrieves facts from external documents.
- Memory should preserve structured records, not only embeddings.
- Every memory entry should trace back to a source run, message, tool result, or document.
- The first version borrows from memU's `Resource -> RecallEntry -> RecallFile` idea, but uses YuruAgent-native names and schemas.

Core models:

```text
MemorySource
- id
- source_type: agent_run | user_message | assistant_message | tool_result | document
- source_id
- content
- metadata
- created_at

MemoryEntry
- id
- agent_id
- source_id
- memory_type: profile | preference | event | knowledge | behavior | skill | tool
- summary
- content
- importance
- embedding
- status: active | disabled | deleted
- created_at
- updated_at

MemoryCollection
- id
- agent_id
- name
- description
- summary
- embedding
- created_at
- updated_at

MemoryCollectionEntry
- collection_id
- entry_id
```

Core flow:

```text
AgentRun completes
-> Generate run summary
-> Extract MemoryEntry records
-> Group entries into MemoryCollection records
-> Generate collection summary
-> Write embeddings
-> Retrieve relevant memory for later runs
-> Inject selected memory into agent context
```

Initial memory types:

```text
profile      User profile
preference   User preferences
event        Historical events
knowledge    Knowledge learned from interactions
behavior     User or agent behavior patterns
skill        Reusable task experience
tool         Tool usage experience
```

Done when:

- A completed agent run can generate summary memory.
- Later runs can retrieve and use historical memory.
- Users can view, disable, and delete memory.
- Memory detail shows its source.
- Run trace shows which memory entries were used.

## Phase 5: Knowledge Base and RAG

Goal: let agents use external knowledge uploaded by users.

Core models:

```text
KnowledgeBase
- id
- name
- description
- created_at
- updated_at

Document
- id
- knowledge_base_id
- filename
- content_type
- status
- created_at

DocumentChunk
- id
- document_id
- chunk_index
- content
- embedding
- metadata
```

Features:

- Knowledge base management.
- Document upload.
- Document parsing.
- Document chunking.
- Embeddings.
- pgvector retrieval.
- Source citation return.
- Agent to knowledge base binding.

Done when:

- Users can upload documents.
- The system can parse, chunk, and vectorize documents.
- Agents can retrieve relevant chunks from bound knowledge bases.
- Agent output can include source references.

## Phase 6: Context Builder

Goal: centrally compose prompt, memory, RAG, and tool context.

Features:

- Read agent system prompt.
- Retrieve relevant MemoryEntry records.
- Retrieve relevant DocumentChunk records.
- Assemble LangGraph input context.
- Record memory and RAG hit results.

Context priority:

```text
system prompt
-> user task
-> selected memory
-> retrieved document chunks
-> tool results
```

Done when:

- Each AgentRun records which memory entries and RAG chunks were used.
- Users can inspect context sources in run detail.
- Memory and RAG can be enabled or disabled independently.

## Phase 7: Tool Registry

Goal: make agent tool usage extensible.

Initial tools:

```text
datetime
calculator
http_fetch
```

Features:

- Tool registration mechanism.
- Tool schema description.
- Tool call records.
- Tool error handling.

Done when:

- Agents can call at least one tool.
- Tool calls are written into AgentStep records.
- Tool failures have clear error records.

## Phase 8: Workflow Workspace

Goal: evolve from single-agent runs into multi-step workflows.

Core nodes:

```text
LLM node
Tool node
Memory retrieval node
RAG retrieval node
Human approval node
Condition node
```

Done when:

- Workflows can combine LLM, tool, memory, and RAG nodes.
- Workflow execution is traceable.
- Human approval nodes can pause and resume execution.

## Phase 9: Agent Templates

Goal: provide reusable agent templates.

Initial templates:

```text
Research Agent
Knowledge QA Agent
Daily Planner Agent
Memory Assistant Agent
Developer Assistant Agent
Browser Task Agent
```

Done when:

- Users can create agents from templates.
- Templates include default prompts, tool configuration, memory strategy, and RAG configuration.

## Phase 10: AgentOps and Evaluation

Goal: improve the engineering quality of agent applications.

Features:

- Prompt version management.
- Memory hit records.
- RAG retrieval quality records.
- Run cost tracking.
- Model call latency.
- Eval case management.
- Failed sample replay.

Done when:

- Users can compare behavior with and without Memory/RAG.
- Users can inspect failed samples.
- Prompt changes can be regression tested.

## Phase Management

Milestones:

```text
Phase 0 - Project Foundation
Phase 1 - Agent Workspace
Phase 2 - Agent Runner
Phase 3 - Traceable Runs
Phase 4 - Agent Memory
Phase 5 - Knowledge Base and RAG
Phase 6 - Context Builder
Phase 7 - Tool Registry
Phase 8 - Workflow Workspace
Phase 9 - Agent Templates
Phase 10 - AgentOps and Evaluation
```

Labels:

```text
phase:foundation
phase:workspace
phase:runner
phase:trace
phase:memory
phase:rag
phase:context
phase:tools
phase:workflow
phase:templates
phase:agentops

type:feature
type:bug
type:docs
type:test
type:refactor
type:infra

priority:p0
priority:p1
priority:p2
```

Issue title examples:

```text
[Memory] Add memory source model
[Memory] Extract typed memories from agent runs
[Memory] Add memory collection summaries
[Context] Inject selected memories into agent context
[RAG] Add document chunking pipeline
[RAG] Retrieve document chunks for agent runs
```

Issue rules:

- One issue should describe one verifiable capability.
- Each issue should include acceptance criteria.
- Finish current-phase `priority:p0` issues before starting the next phase.
- Cross-phase ideas should be captured without interrupting current-phase work.

## Test Plan

- Agent: Agent CRUD works, and Memory/RAG toggles are saved.
- Runner: AgentRun status transitions are correct, and stream events can be consumed.
- Trace: AgentStep records input, output, errors, and timing.
- Memory Source: each MemoryEntry traces back to a source.
- Memory Extraction: run summaries can extract profile, preference, event, knowledge, behavior, skill, and tool memory.
- Memory Retrieval: later runs can retrieve relevant memory and record hit results.
- Memory Management: users can view, disable, and delete memory.
- RAG: documents can be uploaded, parsed, chunked, retrieved, and cited.
- Context Builder: prompt, memory, and RAG context can be composed and recorded.
- Workflow: multi-step flows can combine LLM, tool, memory, and RAG nodes.
- AgentOps: behavior can be compared with and without Memory/RAG.

## Assumptions

- Memory references memU's architecture ideas, but the first version is not a direct memU integration.
- Memory and RAG are separate modules but both enter the agent context through Context Builder.
- Memory supports short-term context and long-term persistent memory.
- RAG uses PostgreSQL with pgvector.
- LangGraph is the main agent orchestration framework.
- Login, permissions, online deployment, and complex multi-user collaboration are not first-priority modules.
