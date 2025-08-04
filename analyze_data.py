#!/usr/bin/env python3
"""
Data analysis script for the PsychoPy text presentation experiment.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def load_data(filename='data/experiment_data.csv'):
    """Load experiment data from CSV file."""
    try:
        df = pd.read_csv(filename)
        print(f"✓ Loaded data from {filename}")
        print(f"  Number of pages: {len(df)}")
        return df
    except FileNotFoundError:
        print(f"✗ Data file '{filename}' not found.")
        print("Please run the experiment first to generate data.")
        return None
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return None

def analyze_timing_data(df):
    """Analyze timing data and print summary statistics."""
    if df is None or df.empty:
        print("No data to analyze.")
        return
    
    print("\n" + "="*50)
    print("TIMING ANALYSIS")
    print("="*50)
    
    # Basic statistics
    print(f"\nTotal experiment duration: {df['Duration'].sum():.2f} seconds")
    print(f"Average page duration: {df['Duration'].mean():.2f} seconds")
    print(f"Standard deviation: {df['Duration'].std():.2f} seconds")
    
    # Per-page analysis
    print("\nPer-page timing:")
    print("-" * 40)
    for _, row in df.iterrows():
        print(f"{row['Page_Name']:15} {row['Duration']:6.2f}s")
    
    # Find fastest and slowest pages
    fastest = df.loc[df['Duration'].idxmin()]
    slowest = df.loc[df['Duration'].idxmax()]
    
    print(f"\nFastest page: {fastest['Page_Name']} ({fastest['Duration']:.2f}s)")
    print(f"Slowest page: {slowest['Page_Name']} ({slowest['Duration']:.2f}s)")

def create_visualizations(df):
    """Create visualizations of the timing data."""
    if df is None or df.empty:
        print("No data to visualize.")
        return
    
    # Ensure data directory exists
    import os
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Bar plot of page durations
    ax1.bar(range(len(df)), df['Duration'], color='skyblue', edgecolor='navy')
    ax1.set_xlabel('Page Index')
    ax1.set_ylabel('Duration (seconds)')
    ax1.set_title('Page Duration by Order')
    ax1.set_xticks(range(len(df)))
    ax1.set_xticklabels([name.split('_')[0] for name in df['Page_Name']], rotation=45)
    
    # Timeline plot
    start_times = df['Start_Time'] - df['Start_Time'].iloc[0]
    ax2.plot(start_times, df['Duration'], 'o-', linewidth=2, markersize=8)
    ax2.set_xlabel('Time from Start (seconds)')
    ax2.set_ylabel('Duration (seconds)')
    ax2.set_title('Timeline of Page Durations')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('data/experiment_timing_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved visualization to 'data/experiment_timing_analysis.png'")
    
    # Show plot if in interactive environment
    try:
        plt.show()
    except:
        pass

def export_summary(df, filename='data/experiment_summary.txt'):
    """Export a text summary of the experiment results."""
    if df is None or df.empty:
        print("No data to export.")
        return
    
    # Ensure data directory exists
    import os
    data_dir = os.path.dirname(filename)
    if data_dir and not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    with open(filename, 'w') as f:
        f.write("PSYCHOPY TEXT EXPERIMENT SUMMARY\n")
        f.write("=" * 40 + "\n\n")
        
        f.write(f"Total pages presented: {len(df)}\n")
        f.write(f"Total experiment duration: {df['Duration'].sum():.2f} seconds\n")
        f.write(f"Average page duration: {df['Duration'].mean():.2f} seconds\n")
        f.write(f"Standard deviation: {df['Duration'].std():.2f} seconds\n\n")
        
        f.write("DETAILED TIMING DATA:\n")
        f.write("-" * 30 + "\n")
        for _, row in df.iterrows():
            f.write(f"{row['Page_Name']:15} {row['Duration']:6.2f}s\n")
        
        f.write(f"\nFastest page: {df.loc[df['Duration'].idxmin(), 'Page_Name']}\n")
        f.write(f"Slowest page: {df.loc[df['Duration'].idxmax(), 'Page_Name']}\n")
    
    print(f"✓ Exported summary to '{filename}'")

def main():
    """Main analysis function."""
    print("PSYCHOPY EXPERIMENT DATA ANALYSIS")
    print("=" * 40)
    
    # Load data
    df = load_data()
    
    if df is not None:
        # Analyze timing
        analyze_timing_data(df)
        
        # Create visualizations
        print("\nCreating visualizations...")
        create_visualizations(df)
        
        # Export summary
        print("\nExporting summary...")
        export_summary(df)
        
        print("\n✓ Analysis complete!")
        print("Files created:")
        print("  - data/experiment_timing_analysis.png (visualization)")
        print("  - data/experiment_summary.txt (text summary)")
    else:
        print("\n✗ No data available for analysis.")
        print("Please run the experiment first: python experiment.py")

if __name__ == "__main__":
    main() 