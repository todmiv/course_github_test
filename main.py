#!/usr/bin/env python3
"""
Main module for the Course GitHub Test project.

This script demonstrates basic Git operations and branching strategies.
"""

import sys
import os

def main():
    """
    Main function to run the project.

    This function prints a welcome message and demonstrates basic functionality.
    """
    print("Welcome to Course GitHub Test!")
    print("This is a test project for learning Git and GitHub.")

    # Check Python version
    if sys.version_info < (3, 6):
        print("Error: Python 3.6 or higher is required.")
        return 1

    # Get current working directory
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")

    # List files in the directory
    files = os.listdir('.')
    print("Files in directory:")
    for file in files:
        print(f"  - {file}")

    return 0

if __name__ == "__main__":
    # Run the main function
    exit_code = main()
    sys.exit(exit_code)
