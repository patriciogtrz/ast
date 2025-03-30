#!/usr/bin/env python python3

# Antipsychotic Switching Tool
# based on the information of The American Association of Psychiatric Pharmacists (AAPP): https://aapp.org/guideline/essentials/antipsychotic-dose-equivalents


# Drugs and doses
DRUGS = {
    "Haloperidol": {
        "generation": "first generation",
        "defined_daily_dose": 0.8,
        "effective_dose_95": 0.42,
        "minimumn_effective_dose": 0.53,
    },
    "Chlorpromazine": {
        "generation": "first generation",
        "defined_daily_dose": 30,
    },
    "Aripiprazole": {
        "generation": "second generation",
        "defined_daily_dose": 1.5,
        "effective_dose_95": 0.76,
        "minimumn_effective_dose": 1.33,
    },
    "Clozapine": {
        "generation": "second generation",
        "defined_daily_dose": 30,
        "minimumn_effective_dose": 40,
    },
    "Olanzapine": {
        "generation": "second generation",
        "defined_daily_dose": 1,
        "effective_dose_95": 1,
        "minimumn_effective_dose": 1,
    },
    "Paliperidone": {
        "generation": "second generation",
        "defined_daily_dose": 0.6,
        "effective_dose_95": 0.88,
        "minimumn_effective_dose": 0.40,
    },
    "Quetiapine": {
        "generation": "second generation",
        "defined_daily_dose": 40,
        "effective_dose_95": 31.78,
        "minimumn_effective_dose": 20,
    },
    "Risperidone": {
        "generation": "second generation",
        "defined_daily_dose": 0.5,
        "effective_dose_95": 0.41,
        "minimumn_effective_dose": 0.27,
    },
    "Ziprasidone": {
        "generation": "second generation",
        "defined_daily_dose": 8,
        "effective_dose_95": 12.29,
        "minimumn_effective_dose": 5.33,
    },
}

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

    equivalent_minimumn_effective_dose = (
        reference_dose / DRUGS[reference_drug]["minimumn_effective_dose"]
        if "minimumn_effective_dose" in DRUGS[reference_drug] else None
    )
    target_minimumn_effective_dose = (
        equivalent_minimumn_effective_dose * DRUGS[target_drug]["minimumn_effective_dose"]
        if equivalent_minimumn_effective_dose and "minimumn_effective_dose" in DRUGS[target_drug] else None
    )

    return target_defined_daily_dose, target_effective_dose_95, target_minimumn_effective_dose

# Main program function
def main():

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
            target_defined_daily_dose, target_effective_dose_95, target_minimumn_effective_dose = conversion(
                reference_drug, reference_dose, target_drug
            )
            
            # Print the results
            print("")
            print("=" * 30)
            print(f"\nReference drug: {reference_drug}")
            print(f"Reference dose: {reference_dose} mg")
            print(f"Target drug: {target_drug}")
            print(f"\nTarget defined daily dose: {target_defined_daily_dose} mg")
            
            # Special error handling for missing values
            if target_effective_dose_95 is not None:
                print(f"Target 95% effective dose 95: {target_effective_dose_95} mg")
            else:
                print("Target 95% effective dose: Not available")
            if target_minimumn_effective_dose is not None:
                print(f"Target minimumn effective dose: {target_minimumn_effective_dose} mg\n")
            else:
                print("Target minimumn effective dose: Not available\n")

# Error handling
    except ValueError as e:
        print(e)

# Main entry point
if __name__ == "__main__":
    main()
