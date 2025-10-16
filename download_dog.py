import requests 

# get http response
dog_json = requests.get("https://dog.ceo/api/breeds/image/random").json()

img_url = dog_json["message"]
# image url is stored in "message" value

image_response = requests.get(img_url)
# use requests library to download random dog picture

with open("dog.jpg", "wb") as file:
    # create dog.jpg in binary write mode
    for chunk in image_response.iter_content():
        # .iter_content() to download in chunks to save working memory
        file.write(chunk)   # write chunk from image_response input to file
