"""Heap-backed, stable priority queue for a simulated emergency-room triage system.

This is a scheduling exercise, not a clinical decision-making protocol.
"""

import heapq


class TriageSystem:
    """Treat higher severity first; preserve arrival order for equal severity."""

    def __init__(self):
        self._patients = []
        self._arrival_counter = 0

    def add_patient(self, name, severity):
        """Add a validated patient; raise ValueError for invalid inputs."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name must be a nonempty string")
        if type(severity) is not int or not 1 <= severity <= 5:
            raise ValueError("Severity must be an integer from 1 to 5")
        heapq.heappush(self._patients, (-severity, self._arrival_counter, name))
        self._arrival_counter += 1

    def process_next(self):
        """Remove and return (name, severity), or None if empty."""
        if self.is_empty():
            return None
        negative_severity, _, name = heapq.heappop(self._patients)
        return (name, -negative_severity)

    def peek_next(self):
        """Return the next (name, severity) without removal, or None."""
        if self.is_empty():
            return None
        negative_severity, _, name = self._patients[0]
        return (name, -negative_severity)

    def is_empty(self):
        return not self._patients

    def size(self):
        return len(self._patients)

    def clear(self):
        """Remove all waiting patients; retain the arrival counter."""
        self._patients.clear()
