from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.get("/health")
def resume_health():
    return {
        "message": "Resume router is working"
    }


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):
    upload_dir = "app/uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    return {
        "filename": file.filename,
        "size": len(content),
        "status": "uploaded"
    }