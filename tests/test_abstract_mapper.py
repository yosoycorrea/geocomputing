"""
Tests for the abstract_mapper module.

This module contains unit tests for the abstract mapping functionality,
ensuring that the module can properly load data, create graphs, and
generate visualizations without errors.
"""

import unittest
import pandas as pd
import networkx as nx
import os
import sys

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.abstract_mapper import generate_abstract_map, analyze_graph


class TestAbstractMapper(unittest.TestCase):
    """Test cases for the abstract_mapper module."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create sample data for testing
        self.sample_data = pd.DataFrame({
            'source': ['A', 'B', 'C', 'A'],
            'target': ['B', 'C', 'D', 'D'],
            'relationship': ['friend', 'colleague', 'mentor', 'family'],
            'weight': [0.8, 0.6, 0.9, 0.7]
        })
        
        # Path to the example CSV file
        self.csv_path = os.path.join(
            os.path.dirname(__file__),
            '..',
            'data',
            'abstract_sample.csv'
        )
    
    def test_generate_abstract_map_with_dataframe(self):
        """Test that generate_abstract_map works with a DataFrame input."""
        # This should not raise any exceptions
        try:
            # Use matplotlib's non-interactive backend for testing
            import matplotlib
            matplotlib.use('Agg')
            
            graph = generate_abstract_map(self.sample_data)
            
            # Verify that a graph was returned
            self.assertIsInstance(graph, nx.DiGraph)
            
            # Verify the graph has the expected number of nodes and edges
            self.assertEqual(graph.number_of_edges(), 4)
            self.assertTrue(graph.number_of_nodes() >= 3)  # At least A, B, C, D
            
        except Exception as e:
            self.fail(f"generate_abstract_map raised an exception: {e}")
    
    def test_generate_abstract_map_with_csv_path(self):
        """Test that generate_abstract_map works with a CSV file path."""
        # Skip if the example file doesn't exist
        if not os.path.exists(self.csv_path):
            self.skipTest(f"Example CSV file not found at {self.csv_path}")
        
        try:
            # Use matplotlib's non-interactive backend for testing
            import matplotlib
            matplotlib.use('Agg')
            
            graph = generate_abstract_map(self.csv_path)
            
            # Verify that a graph was returned
            self.assertIsInstance(graph, nx.DiGraph)
            
            # Verify the graph has nodes and edges
            self.assertGreater(graph.number_of_nodes(), 0)
            self.assertGreater(graph.number_of_edges(), 0)
            
        except Exception as e:
            self.fail(f"generate_abstract_map raised an exception: {e}")
    
    def test_missing_columns_raises_error(self):
        """Test that missing required columns raises a ValueError."""
        # Create data with missing columns
        invalid_data = pd.DataFrame({
            'source': ['A', 'B'],
            'target': ['B', 'C']
            # Missing 'relationship' and 'weight'
        })
        
        with self.assertRaises(ValueError) as context:
            generate_abstract_map(invalid_data)
        
        self.assertIn('Missing required columns', str(context.exception))
    
    def test_different_layouts(self):
        """Test that different layout algorithms work without errors."""
        import matplotlib
        matplotlib.use('Agg')
        
        layouts = ['spring', 'circular', 'kamada_kawai', 'random']
        
        for layout in layouts:
            try:
                graph = generate_abstract_map(self.sample_data, layout=layout)
                self.assertIsInstance(graph, nx.DiGraph)
            except Exception as e:
                self.fail(f"Layout '{layout}' raised an exception: {e}")
    
    def test_invalid_layout_raises_error(self):
        """Test that an invalid layout algorithm raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            generate_abstract_map(self.sample_data, layout='invalid_layout')
        
        self.assertIn('Unknown layout', str(context.exception))
    
    def test_analyze_graph(self):
        """Test the analyze_graph function."""
        # Create a simple graph
        G = nx.DiGraph()
        G.add_edge('A', 'B', weight=1.0)
        G.add_edge('B', 'C', weight=0.5)
        
        metrics = analyze_graph(G)
        
        # Verify metrics are returned
        self.assertIn('num_nodes', metrics)
        self.assertIn('num_edges', metrics)
        self.assertIn('density', metrics)
        self.assertIn('avg_degree', metrics)
        
        # Verify values
        self.assertEqual(metrics['num_nodes'], 3)
        self.assertEqual(metrics['num_edges'], 2)
        self.assertGreater(metrics['avg_degree'], 0)
    
    def test_edge_weights_in_graph(self):
        """Test that edge weights are properly stored in the graph."""
        import matplotlib
        matplotlib.use('Agg')
        
        graph = generate_abstract_map(self.sample_data)
        
        # Check that edges have weight attributes
        for u, v, data in graph.edges(data=True):
            self.assertIn('weight', data)
            self.assertIn('relationship', data)
            self.assertIsInstance(data['weight'], float)
    
    def test_empty_dataframe(self):
        """Test behavior with an empty DataFrame."""
        empty_data = pd.DataFrame(columns=['source', 'target', 'relationship', 'weight'])
        
        import matplotlib
        matplotlib.use('Agg')
        
        # Should not raise an error, just create an empty graph
        graph = generate_abstract_map(empty_data)
        self.assertEqual(graph.number_of_nodes(), 0)
        self.assertEqual(graph.number_of_edges(), 0)


class TestDataLoading(unittest.TestCase):
    """Test cases for loading example data."""
    
    def test_example_csv_exists(self):
        """Test that the example CSV file exists."""
        csv_path = os.path.join(
            os.path.dirname(__file__),
            '..',
            'data',
            'abstract_sample.csv'
        )
        
        self.assertTrue(
            os.path.exists(csv_path),
            f"Example CSV file should exist at {csv_path}"
        )
    
    def test_example_csv_structure(self):
        """Test that the example CSV has the correct structure."""
        csv_path = os.path.join(
            os.path.dirname(__file__),
            '..',
            'data',
            'abstract_sample.csv'
        )
        
        if not os.path.exists(csv_path):
            self.skipTest(f"Example CSV file not found at {csv_path}")
        
        # Load the CSV
        data = pd.read_csv(csv_path)
        
        # Check required columns
        required_columns = {'source', 'target', 'relationship', 'weight'}
        self.assertTrue(
            required_columns.issubset(data.columns),
            f"CSV should have columns: {required_columns}"
        )
        
        # Check that there are at least 5 rows
        self.assertGreaterEqual(
            len(data),
            5,
            "Example CSV should have at least 5 rows"
        )
        
        # Check that weight column is numeric
        self.assertTrue(
            pd.api.types.is_numeric_dtype(data['weight']),
            "Weight column should be numeric"
        )


if __name__ == '__main__':
    unittest.main()
