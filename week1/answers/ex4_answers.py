"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = {"matches": [], "count": 0}

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
For the first query instead of returning two venues `The Albanach` and `The Haymarket Vaults` it returned a single venue (The Haymarket Vaults) as `The Albanach` was status was updated to full leaving only The Haymarket Vaults matching the constraints given in the prompt.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 0   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides a standardized, runtime interface for discovering and using tools, enabling dynamic integration without redeploying models. 
It supports interoperability across services, stateful workflows, and centralized control. 
This improves scalability, reuse, security, and observability—far beyond simply separating tool definitions into another file.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- The Planner is a reasoning-heavy model that decomposes a user task into ordered subgoals; it lives in the autonomous-loop half and feeds structured plans downstream to avoid ambiguity in execution.
- The Executor is a tool-using ReAct-style agent that carries out each subgoal step-by-step; it lives in the structured-agent half and focuses on reliable tool invocation rather than high-level reasoning.
- The Memory store (filesystem + RAG) persists past runs, documents, and intermediate outputs; it lives in the shared layer and supports both halves with retrieval and long-term context.
- The Handoff bridge translates Planner outputs into Executor-readable actions and returns results upstream; it lives between the two halves and enforces schema and control flow.
- The MCP tool layer exposes external tools (APIs, scrapers, databases) via a standardized interface; it lives in the shared layer so both Planner and Executor can access capabilities consistently.
- The Observability module logs traces, tool calls, and failures; it lives in the shared layer and enables debugging, evaluation, and production monitoring.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The research phase clearly fits the Planner-style agent, while the call/execution phase fits the Executor. 
In my runs, research required branching reasoning, revising queries, and synthesizing multiple sources—something the structured agent struggled with because it over-committed to early tool calls. 
The Executor, however, performed well when given explicit steps, reliably calling tools and completing tasks without drifting.

When I swapped them, it felt wrong because the Planner overthought simple actions, adding latency and unnecessary steps, 
while the Executor failed at open-ended research, getting stuck in shallow loops or incomplete retrieval. 
The split works because each agent is optimized for a different cognitive load: exploration vs. execution.
"""