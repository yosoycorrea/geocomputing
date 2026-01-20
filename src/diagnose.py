"""
Module for identifying spatial problems and tensions.
"""


def analyze_spatial_distribution(geojson_data):
    """
    Analyze the spatial distribution of features in GeoJSON data.
    
    This function examines point features and identifies potential spatial
    tensions such as clustering, isolation, or distribution patterns.
    
    Args:
        geojson_data (dict): Parsed GeoJSON data (from read_geojson).
        
    Returns:
        dict: Analysis results including identified tensions.
    """
    if not isinstance(geojson_data, dict):
        return {
            "status": "error",
            "message": "Invalid input: expected dictionary",
            "tensions_found": 0,
            "tensions": []
        }
    
    data = geojson_data.get("data", geojson_data)
    
    if data.get("type") != "FeatureCollection":
        return {
            "status": "success",
            "message": "Only FeatureCollection analysis is supported",
            "tensions_found": 0,
            "tensions": []
        }
    
    features = data.get("features", [])
    tensions = []
    
    # Analyze population if available
    populations = []
    for feature in features:
        props = feature.get("properties", {})
        if "population" in props:
            populations.append({
                "name": props.get("name", "Unknown"),
                "population": props["population"]
            })
    
    if populations:
        # Check for significant population disparities
        pops = [p["population"] for p in populations]
        if len(pops) > 1:
            max_pop = max(pops)
            min_pop = min(pops)
            ratio = max_pop / min_pop if min_pop > 0 else float('inf')
            
            if ratio > 5:  # Significant disparity threshold
                tensions.append({
                    "type": "population_disparity",
                    "severity": "high" if ratio > 10 else "medium",
                    "description": f"Significant population disparity detected (ratio: {ratio:.1f}:1)",
                    "details": {
                        "max_population": max_pop,
                        "min_population": min_pop,
                        "ratio": ratio
                    }
                })
    
    # Check for data completeness
    incomplete_features = sum(1 for f in features if not f.get("properties"))
    if incomplete_features > 0:
        tensions.append({
            "type": "data_quality",
            "severity": "low",
            "description": f"Incomplete data: {incomplete_features} features lack properties",
            "details": {"incomplete_count": incomplete_features}
        })
    
    return {
        "status": "success",
        "message": "Spatial analysis completed",
        "tensions_found": len(tensions),
        "tensions": tensions,
        "feature_count": len(features),
        "analyzed_properties": list(set().union(*[set(f.get("properties", {}).keys()) for f in features])) if features else []
    }


def diagnose_placeholder():
    """
    Placeholder function for diagnosing spatial tensions.
    
    Returns:
        dict: A dictionary containing diagnosis results.
    """
    return {
        "status": "success",
        "message": "Diagnosis completed",
        "tensions_found": 0
    }
