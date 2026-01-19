"""
Abstract Mapper Module

This module provides functionality for creating and visualizing abstract maps
that represent conceptual relationships between entities using graph structures.
Unlike geographic maps, abstract maps focus on connections, relationships, and
interactions in non-spatial contexts.
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from typing import Optional, Union


def generate_abstract_map(
    data: Union[pd.DataFrame, str],
    layout: str = 'spring',
    node_size: int = 500,
    with_labels: bool = True,
    edge_labels: bool = True,
    save_path: Optional[str] = None,
    figsize: tuple = (12, 8)
) -> nx.DiGraph:
    """
    Generate an abstract map visualization from relational data.
    
    This function creates a network graph from data representing relationships
    between entities. It visualizes the connections using various layout algorithms
    and provides customization options for the visualization.
    
    Parameters
    ----------
    data : pd.DataFrame or str
        Input data containing relationship information. Can be either:
        - A pandas DataFrame with columns: source, target, relationship, weight
        - A string path to a CSV file with the same structure
    
    layout : str, optional (default='spring')
        Layout algorithm for positioning nodes. Options include:
        - 'spring': Force-directed layout (spring_layout)
        - 'circular': Nodes arranged in a circle (circular_layout)
        - 'kamada_kawai': Force-directed layout using Kamada-Kawai algorithm
        - 'random': Random positioning
    
    node_size : int, optional (default=500)
        Size of the nodes in the visualization
    
    with_labels : bool, optional (default=True)
        Whether to display node labels
    
    edge_labels : bool, optional (default=True)
        Whether to display relationship labels on edges
    
    save_path : str, optional (default=None)
        If provided, saves the figure to the specified path
    
    figsize : tuple, optional (default=(12, 8))
        Figure size as (width, height) in inches
    
    Returns
    -------
    nx.Graph
        The generated NetworkX graph object containing all nodes and edges
    
    Examples
    --------
    >>> import pandas as pd
    >>> from abstract_mapper import generate_abstract_map
    >>> 
    >>> # Load data from CSV
    >>> data = pd.read_csv('data/abstract_sample.csv')
    >>> 
    >>> # Generate and display the map
    >>> graph = generate_abstract_map(data)
    >>> 
    >>> # Save the visualization
    >>> graph = generate_abstract_map(data, save_path='output/network.png')
    
    Notes
    -----
    The input data should have the following columns:
    - source: The origin node of the relationship
    - target: The destination node of the relationship
    - relationship: The type or description of the relationship
    - weight: Numeric value indicating the strength of the relationship
    """
    
    # Step 1: Load and validate data
    if isinstance(data, str):
        # Load from file path
        data = pd.read_csv(data)
    
    # Validate required columns
    required_columns = {'source', 'target', 'relationship', 'weight'}
    if not required_columns.issubset(data.columns):
        missing = required_columns - set(data.columns)
        raise ValueError(f"Missing required columns: {missing}")
    
    # Step 2: Create graph structure
    # Initialize a directed graph to represent relationships
    G = nx.DiGraph()
    
    # Add edges from the data
    # Each row represents an edge with attributes
    for _, row in data.iterrows():
        G.add_edge(
            row['source'],
            row['target'],
            relationship=row['relationship'],
            weight=float(row['weight'])
        )
    
    # Step 3: Choose layout algorithm
    # Different layouts provide different visual representations
    layout_functions = {
        'spring': nx.spring_layout,
        'circular': nx.circular_layout,
        'kamada_kawai': nx.kamada_kawai_layout,
        'random': nx.random_layout
    }
    
    if layout not in layout_functions:
        raise ValueError(f"Unknown layout: {layout}. Choose from {list(layout_functions.keys())}")
    
    # Calculate node positions using the selected layout
    pos = layout_functions[layout](G)
    
    # Step 4: Create visualization
    plt.figure(figsize=figsize)
    
    # Draw nodes
    nx.draw_networkx_nodes(
        G, pos,
        node_size=node_size,
        node_color='lightblue',
        alpha=0.9,
        edgecolors='navy',
        linewidths=2
    )
    
    # Draw edges with varying thickness based on weight
    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]
    
    # Normalize weights for edge thickness (1-5 range)
    if weights:
        max_weight = max(weights)
        min_weight = min(weights)
        if max_weight > min_weight:
            normalized_weights = [1 + 4 * (w - min_weight) / (max_weight - min_weight) for w in weights]
        else:
            normalized_weights = [2.5] * len(weights)
    else:
        normalized_weights = []
    
    nx.draw_networkx_edges(
        G, pos,
        width=normalized_weights,
        edge_color='gray',
        alpha=0.6,
        arrows=True,
        arrowsize=20,
        arrowstyle='->'
    )
    
    # Draw node labels
    if with_labels:
        nx.draw_networkx_labels(
            G, pos,
            font_size=10,
            font_weight='bold',
            font_color='darkblue'
        )
    
    # Draw edge labels (relationship types)
    if edge_labels:
        edge_labels_dict = nx.get_edge_attributes(G, 'relationship')
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=edge_labels_dict,
            font_size=8,
            font_color='red',
            alpha=0.7
        )
    
    # Step 5: Finalize plot
    plt.title('Abstract Relationship Map', fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    
    # Save if path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Map saved to: {save_path}")
    
    # Display the plot
    plt.show()
    
    # Return the graph object for further analysis
    return G


def analyze_graph(graph: nx.Graph) -> dict:
    """
    Perform basic network analysis on a graph.
    
    Parameters
    ----------
    graph : nx.Graph
        NetworkX graph object to analyze
    
    Returns
    -------
    dict
        Dictionary containing analysis metrics:
        - num_nodes: Number of nodes in the graph
        - num_edges: Number of edges in the graph
        - density: Graph density
        - avg_degree: Average node degree
    """
    
    metrics = {
        'num_nodes': graph.number_of_nodes(),
        'num_edges': graph.number_of_edges(),
        'density': nx.density(graph),
    }
    
    # Calculate average degree
    if graph.number_of_nodes() > 0:
        degrees = [d for n, d in graph.degree()]
        metrics['avg_degree'] = sum(degrees) / len(degrees)
    else:
        metrics['avg_degree'] = 0
    
    return metrics
