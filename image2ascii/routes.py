from fastapi import APIRouter, Query, UploadFile, File
from image2ascii.logger import get_default_logger
from image2ascii.services.converter import get_say_hello
import cv2 as cv
import numpy as np

router = APIRouter(tags=["Say"])
logger = get_default_logger()


@router.get("/say_hello/")
async def say_hello(name: str = Query(example="Mahdi")):
    return get_say_hello(name)


@router.post("/upload/")
async def create_upload_file(file: UploadFile = File()):
    content = await file.read()
    print("..................................................................................")
    return len(content)
