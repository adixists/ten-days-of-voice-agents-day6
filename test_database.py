#!/usr/bin/env python3

"""
Script to test the fraud cases database
"""

import json
import os

def test_database():
    print("Testing fraud cases database...")
    
    # Define the path to the fraud cases file
    fraud_cases_file = os.path.join(os.path.dirname(__file__), "data", "fraud_cases.json")
    
    # Check if the file exists
    if not os.path.exists(fraud_cases_file):
        print(f"Error: Fraud cases file not found at {fraud_cases_file}")
        return 1
    
    # Try to load the JSON data
    try:
        with open(fraud_cases_file, "r") as f:
            fraud_cases = json.load(f)
        
        print(f"Successfully loaded {len(fraud_cases)} fraud cases from database.")
        
        # Print details of each case
        for i, case in enumerate(fraud_cases, 1):
            print(f"\nCase {i}:")
            print(f"  User Name: {case.get('userName', 'N/A')}")
            print(f"  Card Ending: {case.get('cardEnding', 'N/A')}")
            print(f"  Transaction: {case.get('transactionName', 'N/A')} - {case.get('transactionAmount', 'N/A')}")
            print(f"  Status: {case.get('case', 'N/A')}")
            
        print("\nDatabase test completed successfully!")
        return 0
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in fraud cases file: {e}")
        return 1
    except Exception as e:
        print(f"Error: Failed to load fraud cases: {e}")
        return 1

if __name__ == "__main__":
    exit(test_database())