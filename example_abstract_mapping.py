#!/usr/bin/env python3
"""
Example usage of the Abstract Mapping Framework

This script demonstrates how to use the abstract_mapper module to visualize
conceptual relationships using the sample data provided.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from abstract_mapper import generate_abstract_map, analyze_graph
import pandas as pd


def main():
    """Main function to demonstrate abstract mapping."""
    
    print("=" * 60)
    print("Abstract Mapping Framework - Example Usage")
    print("=" * 60)
    print()
    
    # Load the example data
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'abstract_sample.csv')
    
    print(f"Loading data from: {data_path}")
    data = pd.read_csv(data_path)
    
    print("\nData preview:")
    print(data)
    print()
    
    # Generate the abstract map with default settings
    print("Generating abstract map with spring layout...")
    graph = generate_abstract_map(
        data,
        layout='spring',
        save_path='abstract_map_spring.png'
    )
    
    # Analyze the generated graph
    print("\nAnalyzing graph structure...")
    metrics = analyze_graph(graph)
    
    print("\nGraph Analysis Results:")
    print(f"  Number of nodes: {metrics['num_nodes']}")
    print(f"  Number of edges: {metrics['num_edges']}")
    print(f"  Network density: {metrics['density']:.3f}")
    print(f"  Average degree: {metrics['avg_degree']:.2f}")
    
    # Generate alternative layouts
    print("\n" + "-" * 60)
    print("Generating alternative layouts...")
    
    layouts = ['circular', 'kamada_kawai']
    for layout in layouts:
        output_path = f'abstract_map_{layout}.png'
        print(f"  Creating {layout} layout -> {output_path}")
        generate_abstract_map(
            data,
            layout=layout,
            save_path=output_path
        )
    
    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == '__main__':
    # Use non-interactive backend if display is not available
    import matplotlib
    matplotlib.use('Agg')
    
    main()
