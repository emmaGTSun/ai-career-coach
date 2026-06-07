from fastapi import APIRouter

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.get("/health")
def resume_health():
    return {
        "message": "Resume router is working"
    }