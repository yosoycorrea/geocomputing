"""
Module for reading and processing spatial data.
"""

import json
from pathlib import Path


def read_geojson(file_path):
    """
    Read and parse a GeoJSON file.
    
    Args:
        file_path (str or Path): Path to the GeoJSON file.
        
    Returns:
        dict: Parsed GeoJSON data with metadata.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        ValueError: If the file is not valid GeoJSON.
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Validate basic GeoJSON structure
    if "type" not in data:
        raise ValueError("Invalid GeoJSON: missing 'type' field")
    
    if data["type"] not in ["FeatureCollection", "Feature", "Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon", "GeometryCollection"]:
        raise ValueError(f"Invalid GeoJSON type: {data['type']}")
    
    # Extract metadata
    feature_count = 0
    if data["type"] == "FeatureCollection":
        feature_count = len(data.get("features", []))
    elif data["type"] == "Feature":
        feature_count = 1
    
    return {
        "status": "success",
        "message": "GeoJSON data read successfully",
        "data_type": "geojson",
        "geojson_type": data["type"],
        "feature_count": feature_count,
        "data": data
    }


def read_data_placeholder():
    """
    Placeholder function for reading spatial data.
    
    Returns:
        dict: A dictionary containing status and basic spatial data info.
    """
    return {
        "status": "success",
        "message": "Data read successfully",
        "data_type": "spatial"
    }
