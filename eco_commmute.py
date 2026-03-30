import sys

# --- Constants & Configuration ---
# CO2 grams per kilometer (Source: Approximate Global Averages)
EMISSION_FACTORS = {
    "car": 192,
    "bus": 105,
    "train": 41,
    "electric_car": 53,
    "bike": 0,
    "walk": 0
}
GAS_CAR_BASELINE = 192  # Used to calculate "Savings"

def calculate_co2(mode, distance):
    """Calculates emissions and savings compared to a gas car."""
    emissions = EMISSION_FACTORS[mode] * distance
    baseline = GAS_CAR_BASELINE * distance
    saved = baseline - emissions
    return emissions, saved

def get_valid_mode():
    """Ensures the user picks a transport mode that exists in our data."""
    print(f"\nAvailable modes: {', '.join(EMISSION_FACTORS.keys())}")
    while True:
        choice = input("Enter mode of transport: ").lower().strip()
        if choice in EMISSION_FACTORS:
            return choice
        print("Invalid mode. Please choose from the list above.")

def get_valid_distance():
    """Ensures the user enters a positive numerical value for distance."""
    while True:
        try:
            dist = float(input("Enter distance in km: "))
            if dist > 0:
                return dist
            print("Distance must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 5.5).")

def main():
    trips = []
    print("--- Welcome to the Eco-Commute Tracker ---")
    print("Track your daily travels and see your carbon impact.")

    while True:
        mode = get_valid_mode()
        distance = get_valid_distance()
        
        # Logic for "The Guilt Factor" (Originality point)
        if mode == "car" and distance < 2:
            print(">> Note: For such a short trip, walking or biking would be much greener!")

        emissions, saved = calculate_co2(mode, distance)
        
        # Store trip data in a dictionary
        trips.append({
            "mode": mode,
            "dist": distance,
            "co2": emissions,
            "saved": saved
        })

        again = input("\nAdd another trip? (y/n): ").lower()
        if again != 'y':
            break

    # --- Final Report Generation ---
    print("\n" + "="*45)
    print(f"{'MODE':<12} | {'DIST (km)':<10} | {'CO2 (g)':<10} | {'SAVED (g)':<8}")
    print("-" * 45)
    
    total_co2 = 0
    total_saved = 0
    
    for t in trips:
        print(f"{t['mode']:<12} | {t['dist']:<10.2f} | {t['co2']:<10.1f} | {t['saved']:<8.1f}")
        total_co2 += t['co2']
        total_saved += t['saved']

    print("-" * 45)
    print(f"TOTAL CO2 PRODUCED: {total_co2:.1f} g")
    print(f"TOTAL CO2 PREVENTED: {total_saved:.1f} g")
    
    if total_saved > 0:
        print("\nGreat job! You reduced your footprint today.")
    
    print("="*45)

if __name__ == "__main__":
    main()