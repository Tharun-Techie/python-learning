from kreuzberg import extract_bytes
from kreuzberg import ExtractionResult


async def process_upload(file_content: bytes, mime_type: str) -> ExtractionResult:
    """Process uploaded file content with known MIME type."""
    return await extract_bytes(
        file_content,
        mime_type=mime_type,
    )


# Example usage with different file types
async def handle_uploads(docx_bytes: bytes, pdf_bytes: bytes, image_bytes: bytes):
    # Process PDF upload
    pdf_result = await process_upload(pdf_bytes, mime_type="PAM2018.pdf")
    print(f"PDF content: {pdf_result.content}")
    print(f"PDF metadata: {pdf_result.metadata}")

    # Process image upload (will use OCR)
    img_result = await process_upload(image_bytes, mime_type="image/jpeg")
    print(f"Image text: {img_result.content}")

    # Process Word document upload
    docx_result = await process_upload(
        docx_bytes,
        mime_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    print(f"Word content: {docx_result.content}")