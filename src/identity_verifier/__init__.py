"""
identity_verifier

A non-adjudicative library for assessing the public verifiability
of claimed academic or professional identities.

This package does NOT determine truth, fraud, or intent.
"""

from .core import assess_public_verifiability, verify_identity

__all__ = [
    "assess_public_verifiability",
    "verify_identity",
]

