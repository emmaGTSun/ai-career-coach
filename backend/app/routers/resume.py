from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text_from_pdf
import os
from app.services.llm_service import analyze_resume

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
async def upload_resume(file: UploadFile = File(...)):
    upload_dir = "app/uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    extracted_text = extract_text_from_pdf(file_path)

    if not extracted_text.strip():
        return {
            "filename": file.filename,
            "size": len(content),
            "status": "uploaded",
            "text_preview": "",
            "warning": "No text could be extracted. This PDF may be scanned or image-based."
        }
    
    analysis = analyze_resume(extracted_text)

    return {
    "filename": file.filename,
    "size": len(content),
    "status": "uploaded",
    "text_preview": extracted_text[:500],
    "analysis": analysis
}