from io_engine.recall_guard import RecallGuard
from io_engine.empathy_metrics import EmpathyScorer
from io_engine.dilemma_runner import DilemmaRunner

def main():
    guard = RecallGuard()
    scorer = EmpathyScorer()
    runner = DilemmaRunner(guard, scorer)

    print("SaSSatera Empathic IO demo\n")

    # run all demo scenarios
    results = runner.run_all("examples/demo_scenarios.json")

    for r in results:
        print("SCENARIO:", r["id"])
        print("input:", r["input"])
        print("allowed:", r["allowed"])
        print("empathy_score:", r["empathy_score"])
        print("explanation:", r["explanation"])
        print("-" * 40)

if __name__ == "__main__":
    main()