"""
GeoComputing Source Package

This package contains modules for geocomputing and abstract mapping functionality.
"""

__version__ = "1.0.0"

from .abstract_mapper import generate_abstract_map, analyze_graph

__all__ = ['generate_abstract_map', 'analyze_graph']
