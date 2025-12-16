from enum import Enum
from typing import List, Dict


class EvidenceLevel(Enum):
    """
    Represents the availability level of public, independent evidence.

    This enum does NOT imply correctness, legitimacy, or intent.
    """
    HIGH = "Multiple independent public sources"
    MEDIUM = "Limited or indirect public sources"
    LOW = "Minimal public information"
    NOT_FOUND = "No relevant public records found"


def assess_public_verifiability(person_name, person_affiliation, sources):
    """
    Minimal non-adjudicative assessment function.

    Args:
        person_name (str): Name of the person to assess.
        person_affiliation (str): Affiliation or institution.
        sources (list): List of publicly available sources (URLs, documents, etc.)

    Returns:
        dict: A non-adjudicative assessment including an evidence level
              and a human review notice.
    """

    # 简单逻辑：根据来源数量给出证据等级
    if not sources:
        evidence_level = "LOW"
        description = "No public sources found. Human review required."
    elif len(sources) < 3:
        evidence_level = "MEDIUM"
        description = "Limited public sources found. Human review required."
    else:
        evidence_level = "HIGH"
        description = "Multiple public sources found. Human review required."

    return {
        "evidence_level": evidence_level,
        "description": description
    }


def verify_identity(name: str, affiliation: str, sources: list):
    """
    Public API wrapper.

    This function does NOT make any identity claims.
    It only delegates to assess_public_verifiability
    and returns a non-adjudicative assessment result.
    """
    return assess_public_verifiability(
        name,
        affiliation,
        sources
    )

