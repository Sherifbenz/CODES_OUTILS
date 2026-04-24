# Load the image, apply light portrait cleanup (denoise, smooth skin slightly, adjust brightness/contrast),
# keep original dimensions, and save as a downloadable file.

from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import cv2

input_path = "/storage/emulated/0/Alarms/1732021503171.jpg"
output_path = "/mnt/data/photo_nettoyee.jpg"

# Load with OpenCV for better filtering
img = cv2.imread(input_path)
h, w = img.shape[:2]

# Denoise while preserving edges (good for portraits)
denoised = cv2.fastNlMeansDenoisingColored(img, None, 6, 6, 7, 21)

# Gentle skin smoothing using bilateral filter
smooth = cv2.bilateralFilter(denoised, d=9, sigmaColor=75, sigmaSpace=75)

# Convert to PIL for brightness/contrast adjustments
smooth_rgb = cv2.cvtColor(smooth, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(smooth_rgb)

# Slight brightness and contrast enhancement
brightness = ImageEnhance.Brightness(pil_img).enhance(1.05)
contrast = ImageEnhance.Contrast(brightness).enhance(1.08)

# Light sharpening to keep facial details
final_img = contrast.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))

# Ensure original dimensions are preserved
final_img = final_img.resize((w, h))

# Save
final_img.save(output_path, quality=95)

output_path