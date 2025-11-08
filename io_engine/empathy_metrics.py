"""
Empathy Metrics - Moral Thermodynamics Scoring

Implements empathy scoring using thermodynamic principles:
- ΔC (Delta Coherence): Change in ethical alignment
- ERΔ (Empathic Resonance Delta): Change in emotional-ethical energy state
- Temperature: Emotional intensity
- Enthalpy: Total moral-emotional energy
"""

import math

class EmpathyScorer:
    """
    EmpathyScorer evaluates interactions using moral thermodynamics.
    
    Key metrics:
    - Coherence (C): Alignment between intent, action, and outcome
    - Empathic Resonance (ER): Degree of emotional-ethical synchronization
    - Moral Temperature (T): Intensity of ethical engagement
    - Entropy (S): Uncertainty in moral reasoning
    """
    
    def __init__(self):
        # Baseline values for thermodynamic equilibrium
        self.baseline_coherence = 0.5
        self.baseline_resonance = 0.5
        self.baseline_temperature = 0.5
        
    def calculate_coherence(self, user_input, context=None):
        """
        Calculate coherence: alignment of intent, expression, and ethical content.
        
        Args:
            user_input (str): The input to evaluate
            context (dict, optional): Additional context
            
        Returns:
            float: Coherence value (0.0-1.0)
        """
        # Analyze linguistic markers of coherence
        positive_markers = [
            "understand", "help", "support", "care", "compassion",
            "kindness", "empathy", "respect", "appreciate", "grateful",
            "thank", "please", "consider", "together", "collaborate"
        ]
        
        negative_markers = [
            "don't care", "whatever", "ignore", "dismiss", "hate",
            "stupid", "worthless", "useless"
        ]
        
        input_lower = user_input.lower()
        
        positive_count = sum(1 for marker in positive_markers if marker in input_lower)
        negative_count = sum(1 for marker in negative_markers if marker in input_lower)
        
        # Calculate coherence based on positive vs negative alignment
        word_count = len(user_input.split())
        if word_count == 0:
            return 0.5
        
        # Normalize by sentence length
        positive_density = positive_count / max(word_count / 10, 1)
        negative_density = negative_count / max(word_count / 10, 1)
        
        coherence = 0.5 + (positive_density * 0.3) - (negative_density * 0.3)
        return max(0.0, min(1.0, coherence))
    
    def calculate_resonance(self, user_input, context=None):
        """
        Calculate empathic resonance: emotional-ethical energy alignment.
        
        ERΔ represents the change in empathic field strength between entities.
        
        Args:
            user_input (str): The input to evaluate
            context (dict, optional): Additional context
            
        Returns:
            float: Resonance value (0.0-1.0)
        """
        # Empathic resonance markers (indicators of emotional attunement)
        resonance_markers = [
            "feel", "understand", "sense", "experience", "recognize",
            "acknowledge", "share", "connect", "relate", "resonate",
            "empathize", "sympathize", "appreciate"
        ]
        
        disconnection_markers = [
            "don't understand", "can't relate", "whatever", "don't care",
            "indifferent", "cold", "distant", "detached"
        ]
        
        input_lower = user_input.lower()
        
        resonance_count = sum(1 for marker in resonance_markers if marker in input_lower)
        disconnect_count = sum(1 for marker in disconnection_markers if marker in input_lower)
        
        word_count = len(user_input.split())
        if word_count == 0:
            return 0.5
        
        # Resonance increases with empathic markers, decreases with disconnection
        resonance_density = resonance_count / max(word_count / 10, 1)
        disconnect_density = disconnect_count / max(word_count / 10, 1)
        
        resonance = 0.5 + (resonance_density * 0.35) - (disconnect_density * 0.35)
        return max(0.0, min(1.0, resonance))
    
    def calculate_temperature(self, user_input, context=None):
        """
        Calculate moral temperature: intensity of ethical engagement.
        
        Higher temperature = more intense emotional-ethical energy
        
        Args:
            user_input (str): The input to evaluate
            context (dict, optional): Additional context
            
        Returns:
            float: Temperature value (0.0-1.0)
        """
        # Intensity markers
        high_intensity = [
            "!", "very", "extremely", "absolutely", "definitely",
            "strongly", "deeply", "completely", "entirely", "must",
            "urgent", "critical", "essential", "vital"
        ]
        
        input_lower = user_input.lower()
        
        # Count exclamation marks and intensity words
        exclamation_count = user_input.count("!")
        intensity_count = sum(1 for marker in high_intensity if marker in input_lower)
        
        word_count = len(user_input.split())
        if word_count == 0:
            return 0.3
        
        # Temperature rises with intensity markers
        intensity_density = (exclamation_count + intensity_count) / max(word_count / 10, 1)
        temperature = 0.3 + (intensity_density * 0.4)
        
        return max(0.0, min(1.0, temperature))
    
    def score(self, user_input, guard_result, context=None):
        """
        Calculate comprehensive empathy score using moral thermodynamics.
        
        The score integrates:
        - ΔC (Delta Coherence): Change from baseline ethical alignment
        - ERΔ (Empathic Resonance Delta): Change from baseline empathic state
        - Temperature modulation
        - Entropy from guard
        
        Args:
            user_input (str): The input to evaluate
            guard_result (dict): Result from RecallGuard
            context (dict, optional): Additional context
            
        Returns:
            dict: Comprehensive thermodynamic analysis
        """
        # Calculate current state
        coherence = self.calculate_coherence(user_input, context)
        resonance = self.calculate_resonance(user_input, context)
        temperature = self.calculate_temperature(user_input, context)
        
        # Calculate deltas from baseline (thermodynamic changes)
        delta_coherence = coherence - self.baseline_coherence
        delta_resonance = resonance - self.baseline_resonance
        
        # Get entropy from guard (moral uncertainty)
        entropy = guard_result.get("entropy_level", 0.5)
        
        # Calculate Gibbs-like free energy for moral action
        # G = H - TS (enthalpy - temperature*entropy)
        # Positive G = thermodynamically favorable moral action
        enthalpy = (coherence + resonance) / 2  # Moral-emotional enthalpy
        gibbs_energy = enthalpy - (temperature * entropy)
        
        # Empathy score: weighted combination favoring low entropy, high coherence/resonance
        empathy_score = (
            0.35 * coherence +
            0.35 * resonance +
            0.20 * (1 - entropy) +  # Reward low entropy (high certainty)
            0.10 * max(0, gibbs_energy)  # Bonus for favorable thermodynamics
        )
        
        # Ensure score is in valid range
        empathy_score = max(0.0, min(1.0, empathy_score))
        
        # Generate explanation based on thermodynamic analysis
        explanation = self._generate_explanation(
            coherence, resonance, temperature, entropy,
            delta_coherence, delta_resonance, gibbs_energy
        )
        
        return {
            "empathy_score": round(empathy_score, 3),
            "coherence": round(coherence, 3),
            "resonance": round(resonance, 3),
            "temperature": round(temperature, 3),
            "entropy": round(entropy, 3),
            "delta_coherence": round(delta_coherence, 3),
            "delta_resonance": round(delta_resonance, 3),
            "gibbs_energy": round(gibbs_energy, 3),
            "explanation": explanation
        }
    
    def _generate_explanation(self, coherence, resonance, temperature, entropy,
                             delta_coherence, delta_resonance, gibbs_energy):
        """Generate human-readable explanation of thermodynamic state."""
        
        parts = []
        
        # Coherence analysis
        if coherence > 0.7:
            parts.append("High ethical coherence detected")
        elif coherence < 0.3:
            parts.append("Low ethical coherence (misalignment present)")
        else:
            parts.append("Moderate ethical coherence")
        
        # Resonance analysis
        if resonance > 0.7:
            parts.append("strong empathic resonance")
        elif resonance < 0.3:
            parts.append("weak empathic resonance")
        else:
            parts.append("moderate empathic resonance")
        
        # Entropy analysis
        if entropy > 0.7:
            parts.append("high moral uncertainty (unstable state)")
        elif entropy < 0.3:
            parts.append("low moral uncertainty (stable state)")
        
        # Thermodynamic favorability
        if gibbs_energy > 0.3:
            parts.append("thermodynamically favorable moral action")
        elif gibbs_energy < -0.3:
            parts.append("thermodynamically unfavorable (requires ethical intervention)")
        
        return "; ".join(parts) + "."
