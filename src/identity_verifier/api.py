from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .core import verify_identity

app = FastAPI(
    title="Academic Identity Verifier",
    description=(
        "Provides non-adjudicative assessments of publicly "
        "verifiable academic identity information."
    ),
    version="0.1.0-pre",
)

class IdentityRequest(BaseModel):
    name: str = Field(..., description="Person's full name")
    affiliation: str = Field(..., description="Affiliated institution")
    sources: list = Field(default_factory=list, description="Optional external sources")
    orcid_id: str = Field(None, description="Optional ORCID iD")

class IdentityResponse(BaseModel):
    evidence_level: str
    source_count: int
    description: str

@app.post("/verify", response_model=IdentityResponse)
def verify(request: IdentityRequest):
    try:
        return verify_identity(
            name=request.name,
            affiliation=request.affiliation,
            sources=request.sources,
            orcid_id=request.orcid_id,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal assessment error")


