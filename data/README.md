# Data Directory

This directory contains datasets used for spatial analysis and testing.

## Files

### example.geojson

A sample GeoJSON file containing geographic point data for three major cities in Mexico:
- Mexico City (Capital)
- Guadalajara (Second largest city)
- Monterrey (Third largest city)

Each point includes:
- **Coordinates**: [longitude, latitude] in WGS84 (EPSG:4326)
- **Properties**: name, description, and population data

**Purpose**: This example dataset is used for:
- Testing spatial data reading functionality
- Demonstrating GeoJSON format compatibility
- Providing sample data for initial development and testing

**Format**: GeoJSON (RFC 7946 compliant)

## Usage

This data can be used with the `read_space.py` module for processing spatial information and with `visualize.py` for generating maps and visualizations.
