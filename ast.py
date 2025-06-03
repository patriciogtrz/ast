#!/usr/bin/env python python3

# Antipsychotic Switching Tool
# based on the information of The American Association of Psychiatric Pharmacists (AAPP): https://aapp.org/guideline/essentials/antipsychotic-dose-equivalents
# and DRUGBANK: https://go.drugbank.com/

import csv
import sys

# Load drugs information from CSV file
def load_drugs_from_csv(filepath):
    drugs = {}
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            drug_name = row.pop("Drug")
            drugs[drug_name] = {
                key: float(value) if value.replace('.', '', 1).isdigit() else value
                for key, value in row.items()
            }
    return drugs

# Main conversion function
def conversion(reference_drug, reference_dose, target_drug):
    # Handle missing keys with default values
    equivalent_defined_daily_dose = reference_dose / DRUGS[reference_drug]["defined_daily_dose"]
    target_defined_daily_dose = equivalent_defined_daily_dose * DRUGS[target_drug]["defined_daily_dose"]

    # Check for optional keys and calculate only if they exist
    equivalent_effective_dose_95 = (
        reference_dose / DRUGS[reference_drug]["effective_dose_95"]
        if "effective_dose_95" in DRUGS[reference_drug] else None
    )
    target_effective_dose_95 = (
        equivalent_effective_dose_95 * DRUGS[target_drug]["effective_dose_95"]
        if equivalent_effective_dose_95 and "effective_dose_95" in DRUGS[target_drug] else None
    )

    equivalent_minimum_effective_dose = (
        reference_dose / DRUGS[reference_drug]["minimum_effective_dose"]
        if "minimum_effective_dose" in DRUGS[reference_drug] else None
    )
    target_minimum_effective_dose = (
        equivalent_minimum_effective_dose * DRUGS[target_drug]["minimum_effective_dose"]
        if equivalent_minimum_effective_dose and "minimum_effective_dose" in DRUGS[target_drug] else None
    )

    return target_defined_daily_dose, target_effective_dose_95, target_minimum_effective_dose

# Main program function
def main():
    # Check if the CSV file path is provided
    if len(sys.argv) < 2:
        print("\nUsage: python ast4.py <path_to_csv_file>\n")
        return

    # Load the drugs dictionary from the provided CSV file
    csv_filepath = sys.argv[1]
    try:
        global DRUGS
        DRUGS = load_drugs_from_csv(csv_filepath)
    except FileNotFoundError:
        print(f"\nError: File '{csv_filepath}' not found.\n")
        return
    except Exception as e:
        print(f"\nError: Unable to load the CSV file. {e}\n")
        return

    # Program header
    print("")
    print("=" * 30)
    print(" Antipsychotic Switching Tool")
    print("=" * 30)
    print("")
    print("Availables drugs for conversion: \n")
    for key in DRUGS:
        print(f"{key}")

    print("")

    # Main program loop
    try:
       # Choose the reference drug or exit the program
       reference_drug = input("\nEnter current drug name (or exit to quit): ").strip().capitalize()
       if reference_drug == "Exit":
           print("\nExiting the program.\n")
           return
       elif reference_drug not in DRUGS:
           raise ValueError(f"\nDrug '{reference_drug}' not found in equivalency table.\n")

        # Enter the dose of the reference drug
       reference_dose = float(input("\nEnter dose in miligrams: "))
       if reference_dose <= 0:
           raise ValueError("\nDose must be a positive number.\n")
       
        # Choose the target drug
       target_drug = input("\nEnter target drug name: ").strip().capitalize()
       if target_drug not in DRUGS:
           raise ValueError(f"\nDrug '{target_drug}' not found in equivalency table.\n")
       else:
            # Capture the returned values from the conversion function
            target_defined_daily_dose, target_effective_dose_95, target_minimum_effective_dose = conversion(
                reference_drug, reference_dose, target_drug
            )
            
            # Print the results
            print("")
            print("=" * 30)
            print(f"\nReference drug: {reference_drug}")
            print(f"Reference dose: {reference_dose} mg")
            print(f"\nTarget drug: {target_drug}")
            print(f"Target defined daily dose: {target_defined_daily_dose} mg")
            print(f"Target defined half-life: {DRUGS[target_drug]['half-life']}")
            print(f"Target defined CYP450 enzymes: {DRUGS[target_drug]['CYP450']}")
            print("\nConversion results:")
            
            # Special error handling for missing values
            if target_effective_dose_95 is not None:
                print(f"Target 95% effective dose: {target_effective_dose_95} mg")
            else:
                print("Target 95% effective dose: Not available")
            if target_minimum_effective_dose is not None:
                print(f"Target minimum effective dose: {target_minimum_effective_dose} mg\n")
            else:
                print("Target minimum effective dose: Not available\n")

# Error handling
    except ValueError as e:
        print(e)

# Main entry point
if __name__ == "__main__":
    main()
