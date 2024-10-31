from fastapi import FastAPI, File, UploadFile
import uvicorn
import subprocess
import os
from Scripts.Eye_Color_Detection.eye_color import eye_color
from Scripts.skin_tone_detector.skin_tone_name import get_skin_tone_name
from Scripts.dress_color_selection.suggest_dress_color import suggest_dress_color
from Scripts.hair_color_detector.hair_color_detector import HairColorDetector
from Scripts.hair_color_detector.get_hair_color_name import get_hair_color
import sys 
import cv2
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()


origins = [
    "http://localhost:3000",  # Adjust the port if your Next.js app is running on a different port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read():
    return {"hello": "world"}

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Save uploaded file to disk
    print(file.filename)
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())
    

    # Eye color detection
    image = cv2.imread(file_location, cv2.IMREAD_COLOR)

    if image is None:
        print("Error: Could not read the image.")
        sys.exit(1)
    
    eye_color_result = eye_color(image)
    print("eye color extracted: ", eye_color_result)


    # Execute skin tone detection script
    skin_tone_result = subprocess.run(['python', 'Scripts/skin_tone_detector/skin-tone.py', file_location], capture_output=True, text=True)
    skin_tone_extracted = skin_tone_result.stdout.strip()
    print(skin_tone_extracted)

    skin_tone = get_skin_tone_name(skin_tone_extracted)
    print("skin tone extracted: ", skin_tone)

    # Hair Color
    hcd = HairColorDetector()
    result = hcd.get_color(file_location,  save_result=False, n_clusters=10)
    extracted_hair_code = result[-1]
    print(extracted_hair_code)
    hair_color = get_hair_color(np.array(extracted_hair_code))
    print("hair color extracted:", hair_color)

    # Suggest Dress Color
    dress_color = suggest_dress_color(skin_tone, eye_color_result, hair_color)
    print("Suggested dress color: ", dress_color)


    # Remove the file after processing if you don't need to store it
    os.remove(file_location)


    print("returning results...")

    # Return results
    return {"eye_color": eye_color_result, "skin_tone": skin_tone, "hair_color" : hair_color, "dress_color": dress_color}
    # return {"HELLO":"WORLD"}
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




