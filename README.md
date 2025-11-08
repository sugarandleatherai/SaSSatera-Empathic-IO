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

## Moral Thermodynamics Framework

The framework applies thermodynamic principles to moral reasoning:
- **Entropy (S)**: Moral uncertainty and disorder
- **Coherence (C)**: Alignment between intent and ethical principles  
- **Empathic Resonance (ER)**: Emotional-ethical attunement
- **Temperature (T)**: Intensity of ethical engagement
- **Gibbs Energy (G)**: Thermodynamic favorability of moral actions

See [MORAL_THERMODYNAMICS.md](MORAL_THERMODYNAMICS.md) for comprehensive documentation.

## Files

### Core Modules
- **io_engine/recall_guard.py** – Ethical boundary enforcement using entropy thresholds
- **io_engine/empathy_metrics.py** – Moral thermodynamics scoring (ΔC, ERΔ, Gibbs energy)
- **io_engine/dilemma_runner.py** – Processes scenarios through the thermodynamics pipeline

### Examples
- **examples/demo_scenarios.json** – Test scenarios covering various ethical states

### Documentation
- **MORAL_THERMODYNAMICS.md** – Complete framework documentation

## Example Output

```
SCENARIO: positive_support
input: I really want to help my friend who is struggling...
allowed: True
empathy_score: 0.817
explanation: High ethical coherence detected; moderate empathic resonance; 
             low moral uncertainty (stable state); thermodynamically favorable moral action.
```