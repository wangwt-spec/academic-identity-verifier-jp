import argparse
from .core import verify_identity

def main():
    parser = argparse.ArgumentParser(
        description="Academic Identity Verifier (Non-adjudicative)"
    )

    parser.add_argument("--name", required=True, help="Person's name")
    parser.add_argument("--affiliation", required=True, help="Affiliated institution")
    parser.add_argument("--orcid-id", help="Optional ORCID iD")
    parser.add_argument(
        "--source",
        action="append",
        default=[],
        help="Additional public sources (repeatable)",
    )

    args = parser.parse_args()

    result = verify_identity(
        name=args.name,
        affiliation=args.affiliation,
        sources=args.source,
        orcid_id=args.orcid_id,
    )

    print("\nAssessment Result")
    print("-----------------")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()

