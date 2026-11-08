"""Unit tests for CSC 223 Hospital Triage System."""

import unittest
from triage_system import TriageSystem


class TestTriageSystem(unittest.TestCase):
    def setUp(self):
        self.triage = TriageSystem()

    def test_higher_severity_first(self):
        self.triage.add_patient("Low", 1)
        self.triage.add_patient("High", 5)
        self.triage.add_patient("Middle", 3)
        self.assertEqual([self.triage.process_next() for _ in range(3)],
                         [("High", 5), ("Middle", 3), ("Low", 1)])

    def test_equal_severity_arrival_order(self):
        for name in ("Zara", "Amy", "Ben"):
            self.triage.add_patient(name, 4)
        self.assertEqual([self.triage.process_next()[0] for _ in range(3)],
                         ["Zara", "Amy", "Ben"])

    def test_peek_does_not_remove(self):
        self.triage.add_patient("Sofia", 5)
        self.assertEqual(self.triage.peek_next(), ("Sofia", 5))
        self.assertEqual(self.triage.size(), 1)
        self.assertEqual(self.triage.peek_next(), ("Sofia", 5))

    def test_empty_queue(self):
        self.assertIsNone(self.triage.peek_next())
        self.assertIsNone(self.triage.process_next())
        self.assertTrue(self.triage.is_empty())
        self.assertEqual(self.triage.size(), 0)

    def test_invalid_severity_does_not_change_queue(self):
        self.triage.add_patient("Valid", 3)
        for severity in (0, 6, 2.5, "3", True, None):
            with self.subTest(severity=severity):
                with self.assertRaises(ValueError):
                    self.triage.add_patient("Invalid", severity)
        self.assertEqual(self.triage.size(), 1)
        self.assertEqual(self.triage.process_next(), ("Valid", 3))

    def test_invalid_name_does_not_change_queue(self):
        for name in ("", "   ", None, 42):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    self.triage.add_patient(name, 5)
        self.assertTrue(self.triage.is_empty())

    def test_size_is_empty_and_clear(self):
        self.assertTrue(self.triage.is_empty())
        self.triage.add_patient("A", 2)
        self.triage.add_patient("B", 4)
        self.assertEqual(self.triage.size(), 2)
        self.triage.process_next()
        self.assertEqual(self.triage.size(), 1)
        self.triage.clear()
        self.assertEqual(self.triage.size(), 0)
        self.assertTrue(self.triage.is_empty())
        self.assertIsNone(self.triage.process_next())

    def test_interleaved_arrival_and_processing(self):
        self.triage.add_patient("First", 4)
        self.triage.add_patient("Second", 4)
        self.assertEqual(self.triage.process_next(), ("First", 4))
        self.triage.add_patient("Third", 5)
        self.assertEqual(self.triage.process_next(), ("Third", 5))
        self.assertEqual(self.triage.process_next(), ("Second", 4))

    def test_sample_eight_patients(self):
        arrivals = [("Sofia", 5), ("Bob", 2), ("Charlie", 4),
                    ("Diana", 3), ("Eli", 1), ("Tom", 4),
                    ("Alice", 5), ("Rachel", 4)]
        for name, severity in arrivals:
            self.triage.add_patient(name, severity)
        self.assertEqual([self.triage.process_next()[0] for _ in arrivals],
                         ["Sofia", "Alice", "Charlie", "Tom", "Rachel",
                          "Diana", "Bob", "Eli"])

    def test_invalid_insertion_does_not_advance_counter(self):
        self.triage.add_patient("First", 3)
        before = self.triage._arrival_counter
        with self.assertRaises(ValueError):
            self.triage.add_patient("Bad", 7)
        self.assertEqual(self.triage._arrival_counter, before)
        self.triage.add_patient("Second", 3)
        self.assertEqual(self.triage.process_next(), ("First", 3))
        self.assertEqual(self.triage.process_next(), ("Second", 3))

    def test_independent_queues(self):
        other = TriageSystem()
        self.triage.add_patient("A", 2)
        other.add_patient("B", 5)
        self.assertEqual(self.triage.process_next(), ("A", 2))
        self.assertEqual(other.process_next(), ("B", 5))


if __name__ == "__main__":
    unittest.main()
