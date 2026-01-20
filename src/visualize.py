"""
Module for generating dynamic visualizations.
"""


def generate_text_summary(geojson_data, analysis_results=None):
    """
    Generate a text-based summary of spatial data and analysis.
    
    Args:
        geojson_data (dict): Parsed GeoJSON data (from read_geojson).
        analysis_results (dict, optional): Results from spatial analysis.
        
    Returns:
        dict: Visualization information with text summary.
    """
    if not isinstance(geojson_data, dict):
        return {
            "status": "error",
            "message": "Invalid input: expected dictionary",
            "format": "text",
            "content": ""
        }
    
    data = geojson_data.get("data", geojson_data)
    lines = []
    
    # Header
    lines.append("=" * 50)
    lines.append("SPATIAL DATA SUMMARY")
    lines.append("=" * 50)
    
    # Basic info
    geojson_type = data.get("type", "Unknown")
    lines.append(f"\nData Type: {geojson_type}")
    
    if geojson_type == "FeatureCollection":
        features = data.get("features", [])
        lines.append(f"Total Features: {len(features)}")
        
        # List features
        if features:
            lines.append("\nFeatures:")
            lines.append("-" * 50)
            for i, feature in enumerate(features, 1):
                props = feature.get("properties", {})
                name = props.get("name", f"Feature {i}")
                lines.append(f"\n{i}. {name}")
                
                # Add properties
                for key, value in props.items():
                    if key != "name":
                        lines.append(f"   - {key}: {value}")
                
                # Add coordinates
                geom = feature.get("geometry", {})
                if geom.get("type") == "Point":
                    coords = geom.get("coordinates", [])
                    if len(coords) >= 2:
                        lines.append(f"   - Coordinates: [{coords[0]:.4f}, {coords[1]:.4f}]")
    
    # Add analysis results if provided
    if analysis_results and isinstance(analysis_results, dict):
        tensions = analysis_results.get("tensions", [])
        if tensions:
            lines.append("\n" + "=" * 50)
            lines.append("SPATIAL TENSIONS DETECTED")
            lines.append("=" * 50)
            
            for i, tension in enumerate(tensions, 1):
                lines.append(f"\n{i}. {tension.get('type', 'Unknown').upper()}")
                lines.append(f"   Severity: {tension.get('severity', 'unknown')}")
                lines.append(f"   Description: {tension.get('description', 'N/A')}")
    
    lines.append("\n" + "=" * 50)
    
    content = "\n".join(lines)
    
    return {
        "status": "success",
        "message": "Text visualization generated",
        "format": "text",
        "content": content
    }


def visualize_placeholder():
    """
    Placeholder function for creating visualizations.
    
    Returns:
        dict: A dictionary containing visualization information.
    """
    return {
        "status": "success",
        "message": "Visualization generated",
        "format": "placeholder"
    }
