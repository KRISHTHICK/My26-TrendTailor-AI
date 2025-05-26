import os
import numpy as np
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity

def extract_feature_vector(image, size=(100, 100)):
    img = image.resize(size).convert('L')
    return np.array(img).flatten().astype(np.float32)

def find_similar_outfits(uploaded_vec, folder="outfits"):
    results = []
    for file in os.listdir(folder):
        if file.endswith((".jpg", ".png", ".jpeg")):
            ref_img = Image.open(os.path.join(folder, file))
            ref_vec = extract_feature_vector(ref_img)
            sim = cosine_similarity([uploaded_vec], [ref_vec])[0][0]
            results.append((file, sim))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:3]  # top 3 matches

def generate_fashion_advice(category):
    tips = {
        "top": "Pair it with high-waisted jeans or a midi skirt.",
        "bottom": "Tuck in a solid-color blouse or wear with crop tops.",
        "dress": "Add a belt to define your waist, and pair with ankle boots.",
        "jacket": "Layer over a graphic tee and straight pants.",
        "default": "Choose complementary colors and balance your proportions."
    }
    return tips.get(category.lower(), tips["default"])
