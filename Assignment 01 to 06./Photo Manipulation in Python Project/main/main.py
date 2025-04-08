import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance

# 🎨 App Title
st.title("📸 Photo Manipulation App 🎨")

# 📌 Upload Image
uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    st.image(image, caption="📷 Original Image", use_container_width=True)

    # 🖤 Convert to Grayscale
    if st.button("🖤 Convert to Grayscale"):
        gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        st.image(gray_img, caption="🔳 Grayscale Image", use_container_width=True, channels="GRAY")

    # 🔍 Apply Blur
    blur_intensity = st.slider("🔹 Select Blur Intensity", 1, 25, 5, step=2)
    if st.button("🔍 Apply Blur"):
        blurred_img = cv2.GaussianBlur(img_array, (blur_intensity, blur_intensity), 0)
        st.image(blurred_img, caption="🌫️ Blurred Image", use_container_width=True)

    # 🔄 Rotate Image
    rotate_angle = st.slider("🔄 Rotate Image", -180, 180, 0)
    if rotate_angle != 0:
        (h, w) = img_array.shape[:2]
        center = (w // 2, h // 2)
        matrix = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
        rotated_img = cv2.warpAffine(img_array, matrix, (w, h))
        st.image(rotated_img, caption="🔄 Rotated Image", use_container_width=True)

    # ↔ Flip Image
    flip_option = st.radio("↔ Flip Image", ["None", "Horizontal", "Vertical"])
    if flip_option == "Horizontal":
        flipped_img = cv2.flip(img_array, 1)
        st.image(flipped_img, caption="↔ Horizontally Flipped", use_container_width=True)
    elif flip_option == "Vertical":
        flipped_img = cv2.flip(img_array, 0)
        st.image(flipped_img, caption="↕ Vertically Flipped", use_container_width=True)

    # 🌞 Adjust Brightness & Contrast
    brightness = st.slider("☀️ Adjust Brightness", 0.5, 2.0, 1.0)
    contrast = st.slider("🔆 Adjust Contrast", 0.5, 2.0, 1.0)
    if brightness != 1.0 or contrast != 1.0:
        pil_img = ImageEnhance.Brightness(image).enhance(brightness)
        pil_img = ImageEnhance.Contrast(pil_img).enhance(contrast)
        st.image(pil_img, caption="🌞 Adjusted Brightness & Contrast", use_container_width=True)

    # 🎭 Apply Cartoon Effect
    if st.button("🎭 Apply Cartoon Effect"):
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        blurred = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(img_array, 9, 300, 300)
        cartoon_img = cv2.bitwise_and(color, color, mask=edges)
        st.image(cartoon_img, caption="🎭 Cartoon Effect", use_container_width=True)

    # 🖋 Add Watermark
    watermark_text = st.text_input("🖋 Enter Watermark Text", "Watermark")
    if st.button("➕ Add Watermark"):
        img_copy = img_array.copy()
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img_copy, watermark_text, (50, 50), font, 1, (0, 0, 255), 2)
        st.image(img_copy, caption="🖋 Watermarked Image", use_container_width=True)

    # 📥 Save Image
    st.write("📥 Right-click the image and select **Save As** to download it!")

# 🎨 Footer
st.markdown("💡 **Developed by Saba Muhammad Riaz** | Powered by **Streamlit & OpenCV**")
