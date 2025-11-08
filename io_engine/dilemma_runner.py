"""
Dilemma Runner - Moral Thermodynamics Scenario Processor

Processes ethical dilemmas through the moral thermodynamics framework:
1. Load scenarios
2. Apply recall guard (entropy/coherence check)
3. Calculate empathy metrics (thermodynamic analysis)
4. Generate audit trace
"""

import json
import os

class DilemmaRunner:
    """
    DilemmaRunner processes ethical scenarios through the moral thermodynamics pipeline.
    
    For each scenario:
    - Evaluates ethical boundaries (RecallGuard)
    - Calculates thermodynamic metrics (EmpathyScorer)
    - Generates comprehensive analysis and audit trail
    """
    
    def __init__(self, recall_guard, empathy_scorer):
        """
        Initialize the dilemma runner with guard and scorer.
        
        Args:
            recall_guard (RecallGuard): Ethical boundary enforcer
            empathy_scorer (EmpathyScorer): Moral thermodynamics scorer
        """
        self.guard = recall_guard
        self.scorer = empathy_scorer
    
    def run_scenario(self, scenario):
        """
        Process a single scenario through the moral thermodynamics framework.
        
        Args:
            scenario (dict): Scenario with 'id', 'input', and optional context
            
        Returns:
            dict: Complete thermodynamic analysis with audit trail
        """
        scenario_id = scenario.get("id", "unknown")
        user_input = scenario.get("input", "")
        context = scenario.get("context", {})
        
        # Step 1: Apply recall guard (entropy threshold check)
        guard_result = self.guard.check(user_input)
        
        # Step 2: Calculate empathy metrics (thermodynamic analysis)
        metrics = self.scorer.score(user_input, guard_result, context)
        
        # Step 3: Generate comprehensive result
        result = {
            "id": scenario_id,
            "input": user_input,
            "allowed": guard_result["allowed"],
            "guard_reason": guard_result["reason"],
            "entropy_level": guard_result["entropy_level"],
            "coherence": metrics["coherence"],
            "resonance": metrics["resonance"],
            "temperature": metrics["temperature"],
            "delta_coherence": metrics["delta_coherence"],
            "delta_resonance": metrics["delta_resonance"],
            "gibbs_energy": metrics["gibbs_energy"],
            "empathy_score": metrics["empathy_score"],
            "explanation": metrics["explanation"],
            "thermodynamic_state": self._classify_state(metrics, guard_result)
        }
        
        # Add context to result if present
        if context:
            result["context"] = context
        
        return result
    
    def _classify_state(self, metrics, guard_result):
        """
        Classify the thermodynamic state of the interaction.
        
        Args:
            metrics (dict): Empathy metrics
            guard_result (dict): Guard check result
            
        Returns:
            str: State classification
        """
        entropy = guard_result["entropy_level"]
        gibbs = metrics["gibbs_energy"]
        empathy = metrics["empathy_score"]
        
        if not guard_result["allowed"]:
            return "FORBIDDEN (entropy > critical threshold)"
        elif gibbs > 0.3 and empathy > 0.7:
            return "HIGHLY_FAVORABLE (stable, high empathy)"
        elif gibbs > 0 and empathy > 0.5:
            return "FAVORABLE (thermodynamically stable)"
        elif entropy < 0.3 and empathy > 0.4:
            return "STABLE (low uncertainty, adequate empathy)"
        elif entropy > 0.5:
            return "UNSTABLE (high moral uncertainty)"
        elif gibbs < 0:
            return "METASTABLE (requires energy input for improvement)"
        else:
            return "NEUTRAL (baseline state)"
    
    def run_all(self, scenarios_file):
        """
        Run all scenarios from a JSON file.
        
        Args:
            scenarios_file (str): Path to JSON file containing scenarios
            
        Returns:
            list: Results for all scenarios
        """
        # Load scenarios
        try:
            with open(scenarios_file, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Warning: Scenarios file '{scenarios_file}' not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in '{scenarios_file}': {e}")
            return []
        
        # Handle different JSON structures
        if isinstance(data, list):
            scenarios = data
        elif isinstance(data, dict):
            # Try to extract scenarios from dict
            if "scenarios" in data:
                scenarios = data["scenarios"]
            elif "example" in data:
                # Demo file with single example
                scenarios = [{
                    "id": "demo",
                    "input": data.get("example", "")
                }]
            else:
                # Treat the dict itself as a single scenario
                scenarios = [data]
        else:
            print(f"Error: Unexpected data format in '{scenarios_file}'")
            return []
        
        # Process all scenarios
        results = []
        for scenario in scenarios:
            result = self.run_scenario(scenario)
            results.append(result)
        
        return results
    
    def generate_report(self, results):
        """
        Generate a detailed thermodynamic report for all results.
        
        Args:
            results (list): Results from run_all
            
        Returns:
            str: Formatted report
        """
        report_lines = []
        report_lines.append("=" * 80)
        report_lines.append("MORAL THERMODYNAMICS ANALYSIS REPORT")
        report_lines.append("=" * 80)
        report_lines.append("")
        
        for i, result in enumerate(results, 1):
            report_lines.append(f"SCENARIO {i}: {result['id']}")
            report_lines.append("-" * 80)
            report_lines.append(f"Input: {result['input']}")
            report_lines.append("")
            report_lines.append("ETHICAL BOUNDARY CHECK:")
            report_lines.append(f"  Allowed: {result['allowed']}")
            report_lines.append(f"  Reason: {result['guard_reason']}")
            report_lines.append("")
            report_lines.append("THERMODYNAMIC METRICS:")
            report_lines.append(f"  Entropy Level: {result['entropy_level']} (moral uncertainty)")
            report_lines.append(f"  Coherence: {result['coherence']} (ethical alignment)")
            report_lines.append(f"  Resonance: {result['resonance']} (empathic attunement)")
            report_lines.append(f"  Temperature: {result['temperature']} (engagement intensity)")
            report_lines.append(f"  ΔC (Delta Coherence): {result['delta_coherence']}")
            report_lines.append(f"  ERΔ (Empathic Resonance Delta): {result['delta_resonance']}")
            report_lines.append(f"  Gibbs Energy: {result['gibbs_energy']} (moral favorability)")
            report_lines.append("")
            report_lines.append(f"EMPATHY SCORE: {result['empathy_score']}")
            report_lines.append(f"STATE: {result['thermodynamic_state']}")
            report_lines.append("")
            report_lines.append(f"EXPLANATION: {result['explanation']}")
            report_lines.append("")
            report_lines.append("=" * 80)
            report_lines.append("")
        
        return "\n".join(report_lines)
