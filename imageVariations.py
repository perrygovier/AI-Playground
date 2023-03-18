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
        self.sourceName = None
        
    def imageVariations(self, ImageName, VariationCount, ImageSize):
        self.sourceName = ImageName
        response = openai.Image.create_variation(
            image = open("images/{}.png".format(ImageName), "rb"),
            n = VariationCount,
            size = ImageSize
            )
        
        self.image_url = response['data']
            
        self.image_url = [image["url"] for image in self.image_url]
        print(self.image_url)
        return self.image_url
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

# Generate variations for an existing image
imageGen.imageVariations(
    ImageName = "AbeBear",
    VariationCount = 2,
    ImageSize = "1024x1024"
)

# Download the variations
imageGen.downloadImage(names=[
    "{}Variation".format(imageGen.sourceName),
    # "AbeBearVariation2",
    ]
)