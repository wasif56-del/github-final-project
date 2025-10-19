#!/usr/bin/env python3
"""
Simple Interest Calculator
A micro-finance tool for calculating simple interest on loans.
"""

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest and total amount.
    
    Args:
        principal (float): The initial loan amount
        rate (float): Annual interest rate (as percentage)
        time (float): Time period in years
    
    Returns:
        tuple: (interest, total_amount)
    """
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    return interest, total_amount

def main():
    """Main function to run the simple interest calculator."""
    print("=== Simple Interest Calculator for Micro-Finance ===")
    print()
    
    try:
        # Get user input
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (%): "))
        time = float(input("Enter the time period (years): "))
        
        # Calculate interest
        interest, total = calculate_simple_interest(principal, rate, time)
        
        # Display results
        print("\n--- Calculation Results ---")
        print(f"Principal: ${principal:,.2f}")
        print(f"Annual Interest Rate: {rate}%")
        print(f"Time Period: {time} years")
        print(f"Simple Interest: ${interest:,.2f}")
        print(f"Total Amount: ${total:,.2f}")
        
    except ValueError:
        print("Error: Please enter valid numerical values.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()