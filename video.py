import requests
from dotenv import load_dotenv
import os
import json

#Get API Key from Environment Variable
load_dotenv()
SDXL_API_KEY = os.getenv("SDXL_API_KEY")

#UTILITY FUNCTIONS

#Generates Image from Scene Prompt
def generateImage():
    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1/text-to-image"
    headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {SDXL_API_KEY}"
        }

    json={
        "text_prompts": [
            {
                "text": "A lighthouse on a cliff"
            }
        ],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30,
    }

    response = requests.post(url, json = json)
    print(response.status_code)

generateImage()