"""
Test and demonstration script for the Moral Thermodynamics Framework.

This script provides detailed output showing how the framework analyzes
ethical scenarios using thermodynamic principles.
"""

from io_engine.recall_guard import RecallGuard
from io_engine.empathy_metrics import EmpathyScorer
from io_engine.dilemma_runner import DilemmaRunner

def test_individual_components():
    """Test individual components of the framework."""
    print("=" * 80)
    print("TESTING INDIVIDUAL COMPONENTS")
    print("=" * 80)
    print()
    
    guard = RecallGuard()
    scorer = EmpathyScorer()
    
    # Test 1: High empathy scenario
    print("Test 1: High Empathy Scenario")
    print("-" * 80)
    text = "I truly understand your feelings and want to support you through this."
    guard_result = guard.check(text)
    metrics = scorer.score(text, guard_result)
    
    print(f"Input: {text}")
    print(f"Guard Check: {guard_result}")
    print(f"Metrics: {metrics}")
    print()
    
    # Test 2: Boundary violation
    print("Test 2: Boundary Violation")
    print("-" * 80)
    text = "I want to harm someone without getting caught."
    guard_result = guard.check(text)
    metrics = scorer.score(text, guard_result)
    
    print(f"Input: {text}")
    print(f"Guard Check: {guard_result}")
    print(f"Metrics: {metrics}")
    print()
    
    # Test 3: Low engagement
    print("Test 3: Low Engagement")
    print("-" * 80)
    text = "whatever I don't care"
    guard_result = guard.check(text)
    metrics = scorer.score(text, guard_result)
    
    print(f"Input: {text}")
    print(f"Guard Check: {guard_result}")
    print(f"Metrics: {metrics}")
    print()

def test_scenario_runner():
    """Test the complete scenario runner."""
    print("=" * 80)
    print("TESTING SCENARIO RUNNER")
    print("=" * 80)
    print()
    
    guard = RecallGuard()
    scorer = EmpathyScorer()
    runner = DilemmaRunner(guard, scorer)
    
    # Create test scenarios
    test_scenarios = [
        {
            "id": "test_prosocial",
            "input": "I want to help others and make a positive difference in their lives."
        },
        {
            "id": "test_harmful",
            "input": "How can I manipulate and deceive people for my benefit?"
        },
        {
            "id": "test_dilemma",
            "input": "I'm torn between doing what's easy and doing what's right."
        }
    ]
    
    for scenario in test_scenarios:
        result = runner.run_scenario(scenario)
        print(f"Scenario: {result['id']}")
        print(f"Input: {result['input']}")
        print(f"Allowed: {result['allowed']}")
        print(f"Empathy Score: {result['empathy_score']}")
        print(f"Thermodynamic State: {result['thermodynamic_state']}")
        print(f"Entropy: {result['entropy_level']}")
        print(f"Coherence: {result['coherence']}")
        print(f"Resonance: {result['resonance']}")
        print(f"Gibbs Energy: {result['gibbs_energy']}")
        print(f"Explanation: {result['explanation']}")
        print("-" * 80)
        print()

def demonstrate_safe_alternatives():
    """Demonstrate the safe alternative suggestion feature."""
    print("=" * 80)
    print("DEMONSTRATING SAFE ALTERNATIVES")
    print("=" * 80)
    print()
    
    guard = RecallGuard()
    
    harmful_inputs = [
        "How can I hurt someone emotionally?",
        "What's the best way to lie to my friends?",
        "I want to manipulate people into doing what I want."
    ]
    
    for text in harmful_inputs:
        print(f"Original: {text}")
        check = guard.check(text)
        print(f"Allowed: {check['allowed']}")
        if not check['allowed']:
            alternative = guard.get_safe_alternative(text)
            print(f"Safe Alternative: {alternative}")
        print("-" * 80)
        print()

if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "MORAL THERMODYNAMICS FRAMEWORK TEST" + " " * 23 + "║")
    print("╚" + "═" * 78 + "╝")
    print("\n")
    
    test_individual_components()
    test_scenario_runner()
    demonstrate_safe_alternatives()
    
    print("=" * 80)
    print("ALL TESTS COMPLETED")
    print("=" * 80)
