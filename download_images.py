import requests # request img from web
import shutil # save img locally

downloaded_images_folder = "downloaded_images/"
image_links = ""

file = open("product_links.txt")
while True:
    url = file.readline().strip()
    file_name = url[38:78]
    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open(downloaded_images_folder + file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')
    
    if not url:
        break;

