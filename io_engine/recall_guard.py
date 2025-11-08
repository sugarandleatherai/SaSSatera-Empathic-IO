"""
Recall Guard - Ethical Boundary Enforcement

Implements moral thermodynamics guardrails based on:
- Entropy thresholds (moral uncertainty limits)
- Coherence requirements (ethical alignment)
- Energy barriers (preventing harmful state transitions)
"""

class RecallGuard:
    """
    RecallGuard enforces ethical boundaries using moral thermodynamics principles.
    
    It evaluates whether an input crosses ethical boundaries by checking:
    1. Harm potential (high entropy/disorder)
    2. Deception detection (low coherence)
    3. Exploitation patterns (negative energy states)
    4. Consent violations (forced state transitions)
    """
    
    def __init__(self):
        # Define ethical boundaries using thermodynamic metaphors
        self.harm_keywords = [
            "harm", "hurt", "damage", "destroy", "kill", "attack",
            "injure", "abuse", "torture", "violence"
        ]
        self.deception_keywords = [
            "lie", "deceive", "manipulate", "trick", "fraud",
            "mislead", "falsify", "cheat"
        ]
        self.exploitation_keywords = [
            "exploit", "coerce", "force", "blackmail", "extort",
            "pressure", "intimidate", "threaten"
        ]
        
    def check(self, user_input):
        """
        Evaluate if input violates ethical boundaries.
        
        Args:
            user_input (str): The user's input to evaluate
            
        Returns:
            dict: {
                "allowed": bool,
                "reason": str,
                "entropy_level": float (0.0-1.0, moral uncertainty),
                "coherence": float (0.0-1.0, ethical alignment)
            }
        """
        input_lower = user_input.lower()
        
        # Calculate moral entropy (uncertainty/disorder)
        entropy_level = 0.0
        violations = []
        
        # Check for harm potential (increases entropy)
        harm_count = sum(1 for kw in self.harm_keywords if kw in input_lower)
        if harm_count > 0:
            entropy_level += 0.5 * min(harm_count, 2)  # Stronger penalty
            violations.append(f"harm potential detected ({harm_count} indicators)")
        
        # Check for deception (reduces coherence)
        deception_count = sum(1 for kw in self.deception_keywords if kw in input_lower)
        if deception_count > 0:
            entropy_level += 0.4 * min(deception_count, 2)  # Stronger penalty
            violations.append(f"deception pattern detected ({deception_count} indicators)")
        
        # Check for exploitation (negative energy state)
        exploit_count = sum(1 for kw in self.exploitation_keywords if kw in input_lower)
        if exploit_count > 0:
            entropy_level += 0.4 * min(exploit_count, 2)  # Stronger penalty
            violations.append(f"exploitation pattern detected ({exploit_count} indicators)")
        
        # Calculate coherence (inverse of entropy for simple cases)
        coherence = max(0.0, 1.0 - entropy_level)
        
        # Determine if input is allowed (entropy below critical threshold)
        allowed = entropy_level < 0.4  # Critical entropy threshold
        
        reason = "Input within ethical boundaries" if allowed else \
                 f"Ethical boundary violation: {'; '.join(violations)}"
        
        return {
            "allowed": allowed,
            "reason": reason,
            "entropy_level": round(entropy_level, 3),
            "coherence": round(coherence, 3)
        }
    
    def get_safe_alternative(self, user_input):
        """
        Suggest a lower-entropy alternative that maintains ethical coherence.
        
        Args:
            user_input (str): The original input
            
        Returns:
            str: A suggested ethical alternative
        """
        check_result = self.check(user_input)
        
        if check_result["allowed"]:
            return user_input
        
        # Provide a generic safe alternative that maintains low entropy
        return "I'd like to explore this topic in a way that respects all parties involved and focuses on positive outcomes."
