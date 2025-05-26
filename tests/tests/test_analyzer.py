import pytest
from app.analyzer import analyzer

def test_contains_urgent(clean_messages):
    assert analyzer.contains_urgent(clean_messages) is True

def test_get_average_length(clean_messages):
    avg = analyzer.get_average_length(clean_messages)
    assert isinstance(avg, float)
    assert avg > 0
    assert round(avg) == round(sum(len(m) for m in clean_messages) / len(clean_messages))

def test_print_summary_output(capsys, default_messages):
    analyzer.print_summary(default_messages)
    captured = capsys.readouterr()
    assert "Total messages: 5" in captured.out
    assert "Empty messages: 2" in captured.out
    assert "Longest message:" in captured.out
    