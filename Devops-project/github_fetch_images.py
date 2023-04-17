import requests
from PIL import Image
from io import BytesIO

github_url = "https://api.github.com/repos/gauravpatil97886/Machine-learning-Models/contents/Images"
response = requests.get(github_url)

store = []
for item in response.json():
    if item["type"] == "file" and item["name"].lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
        store.append(item["download_url"])

print("List of images present  in your repository:\n")
for i, url in enumerate(store):
    print(f"{i+1}. {url.split('/')[-1]}")

print("\n" + "-"*40)

select = int(input("\nHello Jui, please enter the number of the image you would like to view  :)  "))
image_url = image_urls[select-1]

response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.show()
