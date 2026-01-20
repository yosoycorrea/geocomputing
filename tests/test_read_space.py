"""
Tests for read_space module.
"""

import json
import tempfile
from pathlib import Path
from src.read_space import read_data_placeholder, read_geojson


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


def test_read_geojson_valid_file():
    """
    Test reading a valid GeoJSON file.
    """
    # Create a temporary GeoJSON file
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [-99.1332, 19.4326]
                },
                "properties": {
                    "name": "Test Location"
                }
            }
        ]
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.geojson', delete=False) as f:
        json.dump(geojson_data, f)
        temp_path = f.name
    
    try:
        result = read_geojson(temp_path)
        assert result["status"] == "success"
        assert result["data_type"] == "geojson"
        assert result["geojson_type"] == "FeatureCollection"
        assert result["feature_count"] == 1
        assert "data" in result
    finally:
        Path(temp_path).unlink()


def test_read_geojson_file_not_found():
    """
    Test that FileNotFoundError is raised for non-existent files.
    """
    try:
        read_geojson("/nonexistent/path/to/file.geojson")
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        pass


def test_read_geojson_example_data():
    """
    Test reading the example GeoJSON data file.
    """
    example_path = Path(__file__).parent.parent / "data" / "example.geojson"
    if example_path.exists():
        result = read_geojson(example_path)
        assert result["status"] == "success"
        assert result["geojson_type"] == "FeatureCollection"
        assert result["feature_count"] == 3
