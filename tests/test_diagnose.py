"""
Tests for diagnose module.
"""

from src.diagnose import diagnose_placeholder, analyze_spatial_distribution


def test_diagnose_placeholder():
    """
    Test that the diagnose_placeholder function runs successfully.
    """
    result = diagnose_placeholder()
    assert result is not None
    assert isinstance(result, dict)
    assert result["status"] == "success"
    assert "message" in result
    assert "tensions_found" in result
    assert result["tensions_found"] >= 0


def test_analyze_spatial_distribution_basic():
    """
    Test basic spatial distribution analysis.
    """
    geojson_data = {
        "data": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [-99.0, 19.0]},
                    "properties": {"name": "Location A", "population": 1000000}
                },
                {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [-100.0, 20.0]},
                    "properties": {"name": "Location B", "population": 100000}
                }
            ]
        }
    }
    
    result = analyze_spatial_distribution(geojson_data)
    assert result["status"] == "success"
    assert "tensions_found" in result
    assert isinstance(result["tensions"], list)


def test_analyze_spatial_distribution_with_disparity():
    """
    Test that population disparity is detected.
    """
    geojson_data = {
        "data": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [-99.0, 19.0]},
                    "properties": {"name": "Big City", "population": 9000000}
                },
                {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [-100.0, 20.0]},
                    "properties": {"name": "Small Town", "population": 100000}
                }
            ]
        }
    }
    
    result = analyze_spatial_distribution(geojson_data)
    assert result["status"] == "success"
    assert result["tensions_found"] > 0
    # Check that a population_disparity tension was found
    disparity_found = any(t["type"] == "population_disparity" for t in result["tensions"])
    assert disparity_found


def test_analyze_spatial_distribution_empty_features():
    """
    Test analysis with empty features list.
    """
    geojson_data = {
        "data": {
            "type": "FeatureCollection",
            "features": []
        }
    }
    
    result = analyze_spatial_distribution(geojson_data)
    assert result["status"] == "success"
    assert result["tensions_found"] == 0
    assert result["feature_count"] == 0
    assert result["analyzed_properties"] == []
