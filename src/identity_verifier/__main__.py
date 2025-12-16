"""
Demonstration entry point.

This module is for local demonstration only.
It does NOT accept user input or names.
"""

from identity_verifier.core import assess_public_verifiability

def main():
    # Hard-coded demo records (non-personal, non-identifying)
    demo_records = [
        "University faculty directory (public)",
        "Conference proceedings (public)",
    ]

    result = assess_public_verifiability(demo_records)

    print("=== Demo Output ===")
    print(f"Evidence level: {result['evidence_level']}")
    print(f"Description: {result['description']}")
    print(result["disclaimer"])

if __name__ == "__main__":
    main()
