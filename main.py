from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import tempfile
from fastapi.middleware.cors import CORSMiddleware

import shutil

from src.decripritor.decryptor import Decrypter



app = FastAPI(
    title="Encryption Service API",
    description="API for encrypting and decrypting various types of content",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Decrypter
decrypter = Decrypter()

# Create a temporary directory for file operations
TEMP_DIR = tempfile.mkdtemp()


class TextRequest(BaseModel):
    text: str


class TextResponse(BaseModel):
    encrypted_text: str


@app.post("/encrypt/text", response_model=TextResponse)
async def encrypt_text(request: TextRequest):
    """
    Encrypt text content
    """
    try:
        encrypted = decrypter.encrypt_text(request.text)
        return {"encrypted_text": encrypted.decode()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/decrypt/text")
async def decrypt_text(request: TextRequest):
    """
    Decrypt encrypted text content
    """
    try:
        decrypted = decrypter.decrypt_text(request.text.encode())
        return {"decrypted_text": decrypted}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/encrypt/file")
async def encrypt_file(file: UploadFile = File(...)):
    """
    Encrypt an uploaded file
    """
    try:
        # Create temporary file
        temp_path = os.path.join(TEMP_DIR, file.filename)

        # Save uploaded file
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Encrypt the file
        decrypter.encrypt_file(temp_path)

        # Return the encrypted file
        return FileResponse(
            temp_path,
            media_type='application/octet-stream',
            filename=f"encrypted_{file.filename}"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)


@app.post("/decrypt/file")
async def decrypt_file(file: UploadFile = File(...)):
    """
    Decrypt an encrypted file
    """
    try:
        # Create temporary file
        temp_path = os.path.join(TEMP_DIR, file.filename)

        # Save uploaded file
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Decrypt the file
        decrypter.decrypt_file(temp_path)

        # Return the decrypted file
        return FileResponse(
            temp_path,
            media_type='application/octet-stream',
            filename=f"decrypted_{file.filename}"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)


@app.post("/encrypt/audio")
async def encrypt_audio(file: UploadFile = File(...)):
    """
    Encrypt an audio file
    """
    try:
        # Create temporary file
        temp_path = os.path.join(TEMP_DIR, file.filename)

        # Save uploaded file
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Encrypt the audio
        decrypter.encrypt_audio(temp_path)

        # Return the encrypted file
        return FileResponse(
            temp_path,
            media_type='application/octet-stream',
            filename=f"encrypted_{file.filename}"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)


@app.post("/decrypt/audio")
async def decrypt_audio(file: UploadFile = File(...)):
    """
    Decrypt an encrypted audio file
    """
    try:
        # Create temporary file
        temp_path = os.path.join(TEMP_DIR, file.filename)

        # Save uploaded file
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Decrypt the audio
        decrypter.decrypt_audio(temp_path)

        # Return the decrypted file
        return FileResponse(
            temp_path,
            media_type='application/octet-stream',
            filename=f"decrypted_{file.filename}"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)


@app.post("/encrypt/video")
async def encrypt_video(file: UploadFile = File(...)):
    """
    Encrypt a video file
    """
    try:
        # Validate video format
        if not decrypter.is_supported_video_format(file.filename):
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported video format. Supported formats: {', '.join(decrypter.supported_video_formats)}"
            )

        # Create temporary file
        temp_path = os.path.join(TEMP_DIR, file.filename)

        # Save uploaded file
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Encrypt the video
        decrypter.encrypt_video(temp_path)

        # Return the encrypted file
        return FileResponse(
            temp_path,
            media_type='application/octet-stream',
            filename=f"encrypted_{file.filename}"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)


@app.post("/decrypt/video")
async def decrypt_video(file: UploadFile = File(...)):
    """
    Decrypt an encrypted video file
    """
    try:
        # Validate video format
        if not decrypter.is_supported_video_format(file.filename):
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported video format. Supported formats: {', '.join(decrypter.supported_video_formats)}"
            )

        # Create temporary file
        temp_path = os.path.join(TEMP_DIR, file.filename)

        # Save uploaded file
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Decrypt the video
        decrypter.decrypt_video(temp_path)

        # Return the decrypted file
        return FileResponse(
            temp_path,
            media_type='application/octet-stream',
            filename=f"decrypted_{file.filename}"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)


