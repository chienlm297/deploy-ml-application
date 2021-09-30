from fastapi import BackgroundTasks, FastAPI, File, Request, UploadFile
from fastapi.templating import Jinja2Templates
from storage import save_images, get_client
from config import config
import logging
from botocore.exceptions import ClientError


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/v1/extract_text")
async def extract_text(image: UploadFile = File(...)):
    print("[INFO] filename: ", image.filename)
    image_data = await image.read()
    save_images([image_data], "chien")
    return {"status": True}


@app.on_event("startup")
async def startup_event():
    s3_client = get_client()
    if s3_client is None:
        return
    try:
        response = s3_client.list_buckets()
        if config["BUCKET_IMAGE"] not in [
            bucket["Name"] for bucket in response["Buckets"]
        ]:
            s3_client.create_bucket(Bucket=config["BUCKET_IMAGE"])

    except ClientError as e:
        logging.error(e)
