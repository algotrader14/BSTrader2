from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array, save_img

# Load an image
img = image.load_img('images.jpg', target_size=(100, 100))

# Convert image to numpy array
img_array = img_to_array(img)


print(img_array)
save_img('processed_image.jpg', img_array)
