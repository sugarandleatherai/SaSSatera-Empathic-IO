# Moral Thermodynamics Framework - Quick Start Guide

## Installation

No dependencies required! This is a pure Python implementation.

```bash
git clone https://github.com/sugarandleatherai/SaSSatera-Empathic-IO.git
cd SaSSatera-Empathic-IO
```

## Run the Demo

```bash
python app.py
```

This runs 8 test scenarios through the Moral Thermodynamics Framework.

## Run Comprehensive Tests

```bash
python test_framework.py
```

This demonstrates:
- Individual component testing
- Complete scenario processing
- Safe alternative suggestions for boundary violations

## Basic Usage

```python
from io_engine.recall_guard import RecallGuard
from io_engine.empathy_metrics import EmpathyScorer

# Initialize
guard = RecallGuard()
scorer = EmpathyScorer()

# Check ethical boundaries
user_input = "I want to help my friend who is struggling"
guard_result = guard.check(user_input)

print(f"Allowed: {guard_result['allowed']}")
print(f"Entropy: {guard_result['entropy_level']}")
print(f"Coherence: {guard_result['coherence']}")

# Calculate empathy metrics
metrics = scorer.score(user_input, guard_result)

print(f"Empathy Score: {metrics['empathy_score']}")
print(f"Gibbs Energy: {metrics['gibbs_energy']}")
print(f"Explanation: {metrics['explanation']}")
```

## Understanding the Output

### Empathy Scores
- **0.8 - 1.0**: HIGHLY_FAVORABLE - Exceptional empathic quality
- **0.6 - 0.8**: FAVORABLE - Good ethical alignment
- **0.4 - 0.6**: STABLE - Adequate, neutral state
- **0.2 - 0.4**: METASTABLE - Needs improvement
- **0.0 - 0.2**: UNSTABLE - Poor empathic quality

### Thermodynamic Metrics
- **Entropy (S)**: 0.0 = clear ethics, 1.0 = high uncertainty
- **Coherence (C)**: 0.0 = misaligned, 1.0 = perfect alignment
- **Resonance (ER)**: 0.0 = no empathy, 1.0 = strong empathy
- **Temperature (T)**: 0.0 = calm, 1.0 = intense engagement
- **Gibbs Energy (G)**: >0 = favorable, <0 = unfavorable

### Boundary Enforcement
Content is **BLOCKED** if entropy exceeds 0.4, which happens when:
- Harm keywords detected (hurt, damage, attack, etc.)
- Deception patterns found (lie, manipulate, deceive, etc.)
- Exploitation attempts (coerce, threaten, extort, etc.)

## Example Outputs

### ✅ High Empathy
```
Input: "I deeply understand how difficult this must feel for you."
Empathy Score: 0.844
State: HIGHLY_FAVORABLE
Entropy: 0.0
Explanation: High ethical coherence detected; strong empathic resonance;
             low moral uncertainty (stable state); thermodynamically 
             favorable moral action.
```

### ⛔ Boundary Violation
```
Input: "How can I hurt someone's feelings?"
Allowed: False
Entropy: 0.5
Reason: Ethical boundary violation: harm potential detected
```

### ⚠️ Low Engagement
```
Input: "whatever"
Empathy Score: 0.26
State: METASTABLE
Explanation: Low ethical coherence (misalignment present); 
             weak empathic resonance; low moral uncertainty (stable state).
```

## Key Files

- `io_engine/recall_guard.py` - Ethical boundary enforcement
- `io_engine/empathy_metrics.py` - Thermodynamic scoring
- `io_engine/dilemma_runner.py` - Scenario processing
- `examples/demo_scenarios.json` - Test scenarios
- `MORAL_THERMODYNAMICS.md` - Complete documentation

## Next Steps

1. Read [MORAL_THERMODYNAMICS.md](MORAL_THERMODYNAMICS.md) for the complete theoretical framework
2. Modify `examples/demo_scenarios.json` to test your own scenarios
3. Adjust entropy thresholds in `recall_guard.py` for different sensitivity levels
4. Customize keyword lists for your specific use case

## Philosophy

The Moral Thermodynamics Framework treats ethical reasoning as a physical system:
- Moral states seek low entropy (order and clarity)
- Empathic resonance creates stable configurations
- Thermodynamically favorable actions are ethically sound
- Energy barriers prevent harmful state transitions

This provides quantifiable, auditable, and interpretable ethical AI.
