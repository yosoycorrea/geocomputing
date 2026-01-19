"""
Tests for read_space module.
"""

from src.read_space import read_data_placeholder


def test_read_data_placeholder():
    """
    Test that the read_data_placeholder function runs correctly.
    """
    result = read_data_placeholder()
    assert result is not None
    assert isinstance(result, dict)
    assert result["status"] == "success"
    assert "message" in result
    assert "data_type" in result
