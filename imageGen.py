import openai
import os
import requests
from dotenv import load_dotenv
from PIL import Image
load_dotenv()


class ImageGenerator:
    def __init__(self) -> str:
        self.image_url: str
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.APIKey = openai.api_key
        self.name = None    
    def generateImage(self, Prompt, ImageCount, ImageSize):
        try:
            self.APIKey
            response = openai.Image.create(
            prompt = Prompt,
            n = ImageCount,
            size = ImageSize,
            )
            self.image_url = response['data']

            self.image_url = [image["url"] for image in self.image_url]
            print(self.image_url)
            return self.image_url
        except openai.error.OpenAIError as e:
            print(e.http_status)
            print(e.error)

    def downloadImage(self, names)-> None:
        try:
            self.name = names
            for url in self.image_url:
                image = requests.get(url)
            for name in self.name:
                with open("images/{}.png".format(name), "wb") as f:
                    f.write(image.content)
        except:
            print("An error occured")
            return self.name

# Instantiate the class 
imageGen = ImageGenerator() 

# Generate images:
imageGen.generateImage(
Prompt = "TicTok punching Twitter",
ImageCount = 2,
ImageSize = '1024x1024'
)

# Download the images:
imageGen.downloadImage(names=[
"socialWar"
])