import requests

# ---------- Data Sources ----------

def fetch_crossref_publications(name, affiliation):
    """
    Fetch public publication metadata from Crossref.
    """
    url = (
        "https://api.crossref.org/works"
        f"?query.author={name}&query.affiliation={affiliation}&rows=10"
    )
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json().get("message", {}).get("items", [])
    except Exception:
        return []

def fetch_orcid_works(orcid_id):
    """
    Fetch public works from ORCID Public API.
    """
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
    headers = {"Accept": "application/json"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        return r.json().get("group", [])
    except Exception:
        return []

# ---------- Core Assessment ----------

def assess_public_verifiability(name, affiliation, sources=None, orcid_id=None):
    """
    Non-adjudicative public verifiability assessment.

    This function does NOT confirm identity.
    It only reports the presence of publicly available evidence.
    """
    collected_sources = []

    if sources:
        collected_sources.extend(sources)

    collected_sources.extend(
        fetch_crossref_publications(name, affiliation)
    )

    if orcid_id:
        collected_sources.extend(
            fetch_orcid_works(orcid_id)
        )

    if not collected_sources:
        level = "LOW"
        description = "No publicly verifiable sources found. Human review required."
    elif len(collected_sources) < 3:
        level = "MEDIUM"
        description = "Limited publicly verifiable sources found. Human review required."
    else:
        level = "HIGH"
        description = "Multiple publicly verifiable sources found. Human review required."

    return {
        "evidence_level": level,
        "source_count": len(collected_sources),
        "description": description,
    }

def verify_identity(name, affiliation, sources=None, orcid_id=None):
    """
    Public API wrapper.
    """
    return assess_public_verifiability(
        name=name,
        affiliation=affiliation,
        sources=sources,
        orcid_id=orcid_id,
    )



