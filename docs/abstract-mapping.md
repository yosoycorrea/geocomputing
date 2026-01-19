# Abstract Mapping

## Definition

Abstract mapping is a framework for visualizing and analyzing conceptual relationships that are not necessarily tied to geographic space. Unlike traditional geographic mapping, abstract mapping focuses on representing connections, relationships, and interactions between entities in a graph-based structure.

## Purpose

The abstract mapping framework enables:

- **Conceptual Visualization**: Representing non-spatial relationships between entities (people, ideas, organizations, etc.)
- **Network Analysis**: Understanding the structure and patterns of connections
- **Relationship Exploration**: Discovering hidden patterns and clusters in complex systems
- **Data-Driven Insights**: Extracting meaningful insights from relational data

## Use Cases

### Social Networks
- Mapping connections between individuals, groups, or communities
- Analyzing influence patterns and information flow
- Identifying key nodes and community structures

### Cultural Interactions
- Visualizing cultural exchange and influence between regions or groups
- Mapping the spread of ideas, practices, or traditions
- Understanding cross-cultural collaboration patterns

### Organizational Networks
- Analyzing collaboration patterns within organizations
- Mapping dependencies between teams or projects
- Identifying communication bottlenecks

### Knowledge Graphs
- Representing relationships between concepts or topics
- Mapping academic citations and research connections
- Visualizing semantic relationships in data

## Installation

Before using the abstract mapping framework, install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install networkx matplotlib pandas numpy scipy
```

## How to Use

### 1. Prepare Your Data

Create a CSV file with the following structure:
```
source,target,relationship,weight
```

- `source`: The origin node of the relationship
- `target`: The destination node of the relationship
- `relationship`: The type or label of the relationship
- `weight`: The strength or importance of the connection (numeric)

### 2. Import the Module

```python
from src.abstract_mapper import generate_abstract_map
```

### 3. Load Your Data

```python
import pandas as pd

# Load your data
data = pd.read_csv('data/abstract_sample.csv')
```

### 4. Generate the Abstract Map

```python
# Generate and visualize the abstract map
generate_abstract_map(data)
```

This will create a network visualization showing:
- Nodes representing entities (source and target)
- Edges representing relationships
- Edge weights indicating relationship strength
- Visual layout optimized for clarity

### 5. Customize (Advanced)

The `generate_abstract_map()` function accepts optional parameters:

```python
generate_abstract_map(
    data,
    layout='spring',        # Layout algorithm: 'spring', 'circular', 'kamada_kawai'
    node_size=500,          # Size of nodes in the visualization
    with_labels=True,       # Show node labels
    edge_labels=True,       # Show relationship labels on edges
    save_path=None          # Optional path to save the figure
)
```

## Integration with GEO Ecosystem

The abstract mapping framework complements the GEO 2026 ecosystem by:

- Adding a layer for representing **symbolic space** (non-physical relationships)
- Enabling analysis of social and cultural dimensions alongside physical territory
- Providing tools for understanding the "lived" dimension of space through relationship networks

## Dependencies

- `networkx`: For graph data structures and algorithms
- `matplotlib`: For visualization
- `pandas`: For data handling
- `numpy`: For numerical operations

## Future Enhancements

- Interactive visualizations using Plotly or D3.js
- Advanced graph analytics (centrality measures, community detection)
- Temporal analysis for dynamic networks
- Integration with geographic mapping for hybrid spatial-relational visualizations
