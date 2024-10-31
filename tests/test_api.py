from fastapi.testclient import TestClient
from main import app  # Ensure this import correctly points to your FastAPI app instance

client = TestClient(app)

def test_image_upload():
    # Opening an image file to send with the request
    with open("D:\\Work\\Facial_Color_Extractor\\images\\b.png", "rb") as image:
        response = client.post(
            "/upload/",
            files={"file": ("test_image.jpg", image, "image/jpeg")}
        )
    assert response.status_code == 200
    assert "eye_color" in response.json()
    assert "skin_tone" in response.json()
