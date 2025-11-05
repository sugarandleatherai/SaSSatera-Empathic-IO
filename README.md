# SaSSatera Empathic IO Engine (prototype)

This repo demonstrates the *minimal viable schema* for an empathy-aware IO loop like the one discussed with xAI/Grok.

**Goals**
- show how an agent can process a user exchange
- run it through a recall/ethics guard
- score it with empathy / coherence metrics
- output an action / response plus trace for audit

This is not production code — it’s the explainer scaffold so reviewers can evaluate “empathic resonance mechanics” and run simple dilemma simulations.

## Run

```bash
python app.py
```

Files
	•	io_engine/recall_guard.py – hard-coded v0.1 guardrails
	•	io_engine/empathy_metrics.py – tiny scoring function (ΔC, ERΔ idea)
	•	io_engine/dilemma_runner.py – runs example dilemmas from examples/demo_scenarios.json