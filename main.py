"""CSC 223 demonstration of the heap-backed hospital triage queue."""

from triage_system import TriageSystem


SAMPLE_PATIENTS = [
    ("Sofia", 5), ("Bob", 2), ("Charlie", 4), ("Diana", 3),
    ("Eli", 1), ("Tom", 4), ("Alice", 5), ("Rachel", 4),
]


def main():
    triage = TriageSystem()
    for name, severity in SAMPLE_PATIENTS:
        triage.add_patient(name, severity)
        print(f"Arrived: {name} (severity {severity})")

    previous_size = triage.size()
    print(f"\nNext patient: {triage.peek_next()}")
    print(f"Size unchanged after peek: {triage.size() == previous_size}")

    print("\nTreatment order:")
    while not triage.is_empty():
        name, severity = triage.process_next()
        print(f"{name} (severity {severity})")

    print(f"\nPeek on empty queue: {triage.peek_next()}")
    print(f"Process on empty queue: {triage.process_next()}")
    try:
        triage.add_patient("", 4)
    except ValueError as error:
        print(f"Invalid patient rejected: {error}")


if __name__ == "__main__":
    main()
