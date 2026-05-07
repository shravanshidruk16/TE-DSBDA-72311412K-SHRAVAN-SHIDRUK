# Simple Medical Expert System

"""
Time Complexity

O(1) - Only fixed conditions are checked.

Space Complexity

O(1) - Uses constant memory.

"""

print("=== Medical Expert System ===\n")

# Take user symptoms
fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()

print("\nDiagnosis Result:\n")

# Rule-based decisions
if fever == "yes" and cough == "yes":
    print("You may have Flu.")

elif fever == "yes" and headache == "yes":
    print("You may have Viral Fever.")

elif cough == "yes":
    print("You may have Cold.")

else:
    print("You seem healthy.")