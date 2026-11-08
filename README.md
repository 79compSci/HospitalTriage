# Hospital Triage System — CSC 223

A Python **scheduling simulation** using `heapq` and the Priority Queue ADT. This is **not** a clinical triage protocol.

## Run

```bash
python main.py
python -m unittest discover -v
```

No third-party dependencies are required.

## Design

`TriageSystem` stores patients in a private heap as `(-severity, arrival_order, name)`. Larger severity values have smaller negative keys, so they are processed first. The monotonically increasing arrival counter preserves FIFO order among patients with equal severity, independent of alphabetical name order. Inputs are validated before pushing a tuple or advancing the counter. `bool` values are rejected as severity despite being Python `int` subclasses.

Public methods are `add_patient`, `process_next`, `peek_next`, `is_empty`, `size`, and `clear`. Retrieval returns `(name, severity)` rather than internal keys. Empty peek/process operations return `None`.

## Complexity

| Method | Time | Explanation |
| --- | --- | --- |
| `add_patient()` | O(log n) | Heap insertion may bubble upward |
| `process_next()` | O(log n) | Heap removal may sift downward |
| `peek_next()` | O(1) | Read heap root |
| `is_empty()` | O(1) | Check list emptiness |
| `size()` | O(1) | Read list length |
| `clear()` | O(n) | Release up to `n` stored references |

The queue uses O(n) space for `n` waiting patients.

## Required sample

Arrival order: Sofia (5), Bob (2), Charlie (4), Diana (3), Eli (1), Tom (4), Alice (5), Rachel (4).

Expected treatment order: **Sofia, Alice, Charlie, Tom, Rachel, Diana, Bob, Eli**.

## Testing

Run `python -m unittest discover -v` to check severity order, stable ties, non-destructive peek, empty queue behavior, invalid inputs, state operations, interleaved arrivals, sample ordering, and independent instances. Record actual test results and your own observations in the course report. Disclose substantive AI assistance per your course policy.
