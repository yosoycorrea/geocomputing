"""
Tests for visualize module.
"""

from src.visualize import visualize_placeholder, generate_text_summary


def test_visualize_placeholder():
    """
    Test that the visualize_placeholder function works correctly.
    """
    result = visualize_placeholder()
    assert result is not None
    assert isinstance(result, dict)
    assert result["status"] == "success"
    assert "message" in result
    assert "format" in result


def test_generate_text_summary_basic():
    """
    Test basic text summary generation.
    """
    geojson_data = {
        "data": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [-99.1332, 19.4326]},
                    "properties": {"name": "Test City", "population": 500000}
                }
            ]
        }
    }
    
    result = generate_text_summary(geojson_data)
    assert result["status"] == "success"
    assert result["format"] == "text"
    assert "content" in result
    assert "Test City" in result["content"]


def test_generate_text_summary_with_analysis():
    """
    Test text summary generation with analysis results.
    """
    geojson_data = {
        "data": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [-99.0, 19.0]},
                    "properties": {"name": "Location A"}
                }
            ]
        }
    }
    
    analysis_results = {
        "tensions": [
            {
                "type": "test_tension",
                "severity": "medium",
                "description": "Test tension description"
            }
        ]
    }
    
    result = generate_text_summary(geojson_data, analysis_results)
    assert result["status"] == "success"
    assert "SPATIAL TENSIONS DETECTED" in result["content"]
    assert "test_tension" in result["content"].lower()
