from identity_verifier.core import verify_identity


def test_output_is_non_adjudicative():
    """
    The verifier must not make definitive identity claims.
    It should only provide evidence levels and require human review.
    """

    result = verify_identity(
        name="Test Person",
        affiliation="Test Institute",
        sources=[]
    )

    # 必须包含证据级别
    assert "evidence_level" in result

    # 不允许出现裁决性用语
    forbidden_phrases = [
        "is fake",
        "is real",
        "confirmed",
        "fraud",
        "guilty",
        "legitimate"
    ]

    description = result.get("description", "").lower()

    for phrase in forbidden_phrases:
        assert phrase not in description

    # 必须提示人工审核
    assert "human" in description or "review" in description

