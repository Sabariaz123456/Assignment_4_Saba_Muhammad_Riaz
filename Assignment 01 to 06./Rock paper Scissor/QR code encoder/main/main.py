import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# ----- PAGE CONFIG -----
st.set_page_config(
    page_title="QR Code Generator | Elegant & Stylish",
    page_icon="🔳",
    layout="centered"
)

# ----- CUSTOM CSS STYLING -----
st.markdown("""
    <style>
        /* Page background */
        .stApp {
            background: linear-gradient(to right top, #e9f0f4, #ffffff);
            font-family: 'Segoe UI', sans-serif;
            padding: 2rem;
        }

        /* Title styling */
        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 800;
            color: #2d3e50;
            margin-bottom: 0.3rem;
        }

        .sub-title {
            text-align: center;
            font-size: 1.1rem;
            color: #555c66;
            margin-bottom: 2.5rem;
        }

        /* Section headers */
        .section-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #3a4750;
            margin-top: 1.5rem;
        }

        /* Card style preview */
        .qr-preview {
            background-color: #ffffffcc;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 8px 18px rgba(0,0,0,0.1);
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ----- TITLE -----
st.markdown('<div class="main-title">🔳QR Code Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Create high-quality, customizable QR codes in seconds!</div>', unsafe_allow_html=True)

# ----- INPUT -----
st.markdown('<div class="section-title">✍️ Step 1: Enter Your Data</div>', unsafe_allow_html=True)
user_input = st.text_input("Enter the text, link, phone number or anything you want to encode:", placeholder="e.g. https://yourdomain.com")

# ----- CUSTOMIZATION OPTIONS -----
st.markdown('<div class="section-title">🎨 Step 2: Customize</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    fill_color = st.color_picker("QR Color", "#000000")
with col2:
    bg_color = st.color_picker("Background Color", "#ffffff")

size = st.slider("Adjust QR Code Size", min_value=5, max_value=20, value=10)

add_logo = st.checkbox("🖼️ Add Center Logo")
logo_file = None
if add_logo:
    logo_file = st.file_uploader("Upload Logo (PNG/JPG)", type=["png", "jpg", "jpeg"])

# ----- GENERATE QR -----
if st.button("🚀 Generate My QR Code"):
    if user_input.strip() != "":
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,
            border=4,
        )
        qr.add_data(user_input)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=bg_color).convert("RGB")

        # Add logo if applicable
        if logo_file is not None:
            logo = Image.open(logo_file)
            logo_size = int(min(img.size) * 0.25)
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
            img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

        # ----- PREVIEW QR CODE -----
        st.markdown('<div class="section-title">✅ Step 3: Preview Your QR</div>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="qr-preview">', unsafe_allow_html=True)
            st.image(img, caption="Your Custom QR Code", use_container_width=False)
            st.markdown('</div>', unsafe_allow_html=True)

        # ----- DOWNLOAD -----
        buffered = BytesIO()
        img.save(buffered, format="PNG")

        st.markdown('<div class="section-title">📥 Step 4: Download Your QR</div>', unsafe_allow_html=True)
        st.download_button(
            label="⬇️ Download as PNG",
            data=buffered.getvalue(),
            file_name="qr_code.png",
            mime="image/png",
            help="Download your QR code to use it anywhere!"
        )
        st.success("✅ QR Code successfully created!")
    else:
        st.warning("⚠️ Please enter something to generate a QR code.")






