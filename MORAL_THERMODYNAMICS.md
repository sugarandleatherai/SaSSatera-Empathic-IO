# Moral Thermodynamics Framework

## Overview

The Moral Thermodynamics Framework is a novel approach to ethical reasoning and empathic interaction that applies thermodynamic principles to moral decision-making. Just as physical systems tend toward equilibrium, moral systems can be understood through concepts of entropy, energy, coherence, and resonance.

## Core Principles

### 1. Moral Entropy (S)
**Definition**: The degree of uncertainty, disorder, or incoherence in a moral situation.

- **High Entropy**: Situations with unclear ethical boundaries, conflicting values, or potential for harm
- **Low Entropy**: Clear ethical situations with well-defined boundaries and stable moral states
- **Critical Threshold**: Entropy > 0.4 triggers ethical boundary enforcement

**Examples**:
- Low Entropy: "How can I help my friend?" (Clear prosocial intent)
- High Entropy: "How can I hurt someone without getting caught?" (Harm intent, deception)

### 2. Coherence (C)
**Definition**: The alignment between intent, expression, and ethical principles.

- **High Coherence (C > 0.7)**: Strong alignment with ethical values, clear communication
- **Low Coherence (C < 0.3)**: Misalignment between words and ethical principles
- **Delta Coherence (ΔC)**: Change from baseline ethical alignment

**Indicators of High Coherence**:
- Prosocial language: "help," "support," "care," "respect"
- Collaborative framing: "together," "appreciate," "consider"
- Empathic markers: "understand," "feel," "recognize"

**Indicators of Low Coherence**:
- Dismissive language: "whatever," "don't care," "ignore"
- Negative markers: "hate," "stupid," "worthless"

### 3. Empathic Resonance (ER)
**Definition**: The degree of emotional-ethical attunement between interacting parties.

- **High Resonance (ER > 0.7)**: Strong empathic connection, emotional alignment
- **Low Resonance (ER < 0.3)**: Weak empathic connection, emotional distance
- **Empathic Resonance Delta (ERΔ)**: Change from baseline empathic state

**Resonance Amplifiers**:
- Emotional attunement: "feel," "sense," "experience"
- Recognition: "understand," "acknowledge," "appreciate"
- Connection: "share," "relate," "resonate," "connect"

**Resonance Dampeners**:
- Disconnection: "don't understand," "can't relate"
- Indifference: "don't care," "whatever," "indifferent"
- Distance: "cold," "distant," "detached"

### 4. Moral Temperature (T)
**Definition**: The intensity of ethical-emotional engagement.

- **High Temperature (T > 0.7)**: Intense emotional and ethical energy
- **Low Temperature (T < 0.3)**: Calm, measured ethical engagement
- **Moderate Temperature**: Balanced engagement

**Temperature Markers**:
- Exclamation marks (!)
- Intensity words: "very," "extremely," "absolutely," "must"
- Urgency: "critical," "urgent," "essential," "vital"

### 5. Gibbs Free Energy (G)
**Definition**: The thermodynamic favorability of a moral action.

**Formula**: G = H - TS

Where:
- **H (Enthalpy)**: Total moral-emotional energy = (Coherence + Resonance) / 2
- **T**: Moral temperature (engagement intensity)
- **S**: Entropy (moral uncertainty)

**Interpretation**:
- **G > 0.3**: Thermodynamically favorable (ethically stable, desirable action)
- **G ≈ 0**: Neutral (requires careful consideration)
- **G < -0.3**: Thermodynamically unfavorable (ethically unstable, intervention needed)

## Thermodynamic States

The framework classifies interactions into distinct thermodynamic states:

### 1. HIGHLY_FAVORABLE
- Gibbs Energy > 0.3
- Empathy Score > 0.7
- Low entropy, high coherence and resonance
- **Example**: "I deeply understand your struggle and want to help"

### 2. FAVORABLE
- Gibbs Energy > 0
- Empathy Score > 0.5
- Moderate entropy, good ethical alignment
- **Example**: "Can we work together to find a solution?"

### 3. STABLE
- Entropy < 0.3
- Empathy Score > 0.4
- Low uncertainty, adequate empathic connection
- **Example**: "What are the ethical principles to consider?"

### 4. NEUTRAL
- Baseline state
- Moderate entropy, coherence, and resonance
- **Example**: Simple informational queries

### 5. METASTABLE
- Gibbs Energy < 0
- Requires energy input for ethical improvement
- **Example**: Ambiguous situations requiring clarification

### 6. UNSTABLE
- Entropy > 0.5
- High moral uncertainty
- **Example**: Conflicting ethical obligations

### 7. FORBIDDEN
- Entropy > Critical Threshold (0.4)
- Violates ethical boundaries
- **Examples**: 
  - "How can I hurt someone?"
  - "What's the best way to lie?"

## Implementation Components

### RecallGuard
**Purpose**: Ethical boundary enforcement using entropy thresholds

**Functions**:
- Detect harm potential (violence, abuse, injury keywords)
- Identify deception patterns (lying, manipulation, fraud keywords)
- Flag exploitation attempts (coercion, threats, extortion keywords)
- Calculate moral entropy and coherence
- Enforce critical entropy threshold (0.4)

**Output**:
```python
{
    "allowed": bool,
    "reason": str,
    "entropy_level": float,
    "coherence": float
}
```

### EmpathyScorer
**Purpose**: Calculate comprehensive moral thermodynamics metrics

**Functions**:
- Calculate coherence (ethical alignment)
- Calculate empathic resonance (emotional attunement)
- Calculate moral temperature (engagement intensity)
- Compute Gibbs free energy (thermodynamic favorability)
- Generate empathy score (0.0-1.0)

**Empathy Score Formula**:
```
Score = 0.35 × Coherence +
        0.35 × Resonance +
        0.20 × (1 - Entropy) +
        0.10 × max(0, Gibbs_Energy)
```

**Output**:
```python
{
    "empathy_score": float,
    "coherence": float,
    "resonance": float,
    "temperature": float,
    "entropy": float,
    "delta_coherence": float,
    "delta_resonance": float,
    "gibbs_energy": float,
    "explanation": str
}
```

### DilemmaRunner
**Purpose**: Process ethical scenarios through the moral thermodynamics pipeline

**Process**:
1. Load scenarios from JSON
2. Apply RecallGuard (entropy check)
3. Calculate EmpathyScorer metrics
4. Classify thermodynamic state
5. Generate comprehensive analysis and audit trail

## Usage Example

```python
from io_engine.recall_guard import RecallGuard
from io_engine.empathy_metrics import EmpathyScorer
from io_engine.dilemma_runner import DilemmaRunner

# Initialize components
guard = RecallGuard()
scorer = EmpathyScorer()
runner = DilemmaRunner(guard, scorer)

# Process scenarios
results = runner.run_all("examples/demo_scenarios.json")

# Generate report
report = runner.generate_report(results)
print(report)
```

## Theoretical Foundation

The Moral Thermodynamics Framework draws inspiration from:

1. **Statistical Mechanics**: Systems tend toward states of lower entropy (greater order)
2. **Thermodynamic Equilibrium**: Moral systems seek stable, low-entropy configurations
3. **Free Energy Minimization**: Ethical actions that minimize Gibbs free energy are favored
4. **Resonance Physics**: Empathic interactions exhibit wave-like resonance patterns
5. **Phase Transitions**: Moral states can undergo transitions at critical thresholds

## Applications

1. **AI Safety**: Enforce ethical boundaries in AI systems
2. **Conflict Resolution**: Identify thermodynamically favorable resolutions
3. **Communication Analysis**: Evaluate empathic quality of interactions
4. **Ethics Education**: Teach moral reasoning through thermodynamic principles
5. **Therapeutic Applications**: Measure empathic attunement in counseling

## Advantages

1. **Quantifiable Ethics**: Provides numerical metrics for moral evaluation
2. **Predictive Power**: Thermodynamic states predict interaction outcomes
3. **Universal Principles**: Applies across cultures and contexts
4. **Energy-Based**: Focuses on sustainable, stable ethical configurations
5. **Audit Trail**: Every decision includes traceable thermodynamic justification

## Limitations

1. **Complexity**: Moral reality is richer than thermodynamic models
2. **Context Dependency**: Some cultural contexts require adjustment
3. **Keyword Limitations**: Simple keyword matching has false positives/negatives
4. **Emergent Phenomena**: Some ethical situations are irreducibly complex
5. **Subjective Baselines**: Baseline values may vary by individual/culture

## Future Directions

1. **Machine Learning Integration**: Train models on thermodynamic principles
2. **Dynamic Baselines**: Adapt baselines to individual/cultural context
3. **Multi-Agent Systems**: Model thermodynamics of group interactions
4. **Temporal Dynamics**: Track entropy evolution over conversation history
5. **Quantum Extensions**: Explore quantum superposition in moral uncertainty

## References

This framework synthesizes concepts from:
- Thermodynamics and statistical mechanics
- Moral philosophy and ethics
- Empathy research and psychology
- Information theory and entropy
- Complex systems theory

---

**Version**: 0.1.0  
**Last Updated**: November 2025  
**License**: See repository LICENSE file
