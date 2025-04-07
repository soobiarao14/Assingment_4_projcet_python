# photo_manipulation.py application

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

def adjust_brightness(image, brightness):
    """Adjust image brightness"""
    if brightness != 0:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        
        if brightness > 0:
            lim = 255 - brightness
            v[v > lim] = 255
            v[v <= lim] += brightness
        else:
            brightness = -brightness
            lim = brightness
            v[v < lim] = 0
            v[v >= lim] -= brightness
            
        final_hsv = cv2.merge((h, s, v))
        image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return image

def adjust_contrast(image, contrast):
    """Adjust image contrast"""
    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        
        image = cv2.addWeighted(image, alpha_c, image, 0, gamma_c)
    return image

def apply_blur(image, blur):
    """Apply Gaussian blur to image"""
    if blur > 0:
        blur = blur if blur % 2 == 1 else blur + 1
        image = cv2.GaussianBlur(image, (blur, blur), 0)
    return image

def adjust_rgb_channels(image, red, green, blue):
    """Adjust individual RGB channels"""
    b, g, r = cv2.split(image)
    
    if red > 0:
        r = cv2.add(r, red)
    elif red < 0:
        r = cv2.subtract(r, -red)
        
    if green > 0:
        g = cv2.add(g, green)
    elif green < 0:
        g = cv2.subtract(g, -green)
        
    if blue > 0:
        b = cv2.add(b, blue)
    elif blue < 0:
        b = cv2.subtract(b, -blue)
        
    return cv2.merge((b, g, r))

def apply_grayscale(image):
    """Convert image to grayscale"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_sepia(image):
    """Apply sepia filter"""
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    return cv2.filter2D(image, -1, kernel)

def apply_negative(image):
    """Convert image to negative"""
    return cv2.bitwise_not(image)

def apply_warm(image):
    """Add warm tone effect"""
    b, g, r = cv2.split(image)
    r = cv2.add(r, 10)
    b = cv2.subtract(b, 10)
    return cv2.merge((b, g, r))

def apply_cool(image):
    """Add cool tone effect"""
    b, g, r = cv2.split(image)
    b = cv2.add(b, 10)
    r = cv2.subtract(r, 10)
    return cv2.merge((b, g, r))

def main():
    st.title("📷 Photo Manipulation App")
    st.markdown("Adjust colors, brightness, contrast, and apply filters to your images")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Read the image file
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        # Convert BGR to RGB for display
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_rgb, caption="Original Image",  use_container_width=True)
        
        # Sidebar controls
        st.sidebar.header("Basic Adjustments")
        brightness = st.sidebar.slider("Brightness", -100, 100, 0)
        contrast = st.sidebar.slider("Contrast", -100, 100, 0)
        blur = st.sidebar.slider("Blur", 0, 30, 0)
        
        st.sidebar.header("Color Adjustments")
        red = st.sidebar.slider("Red Channel", -100, 100, 0)
        green = st.sidebar.slider("Green Channel", -100, 100, 0)
        blue = st.sidebar.slider("Blue Channel", -100, 100, 0)
        
        st.sidebar.header("Color Effects")
        grayscale = st.sidebar.checkbox("Grayscale")
        sepia = st.sidebar.checkbox("Sepia")
        negative = st.sidebar.checkbox("Negative")
        warm = st.sidebar.checkbox("Warm Tone")
        cool = st.sidebar.checkbox("Cool Tone")
        
        # Apply adjustments
        adjusted = adjust_brightness(image, brightness)
        adjusted = adjust_contrast(adjusted, contrast)
        adjusted = apply_blur(adjusted, blur)
        adjusted = adjust_rgb_channels(adjusted, red, green, blue)
        
        # Apply color effects
        if grayscale:
            adjusted = apply_grayscale(adjusted)
        elif sepia:
            adjusted = apply_sepia(adjusted)
        elif negative:
            adjusted = apply_negative(adjusted)
        elif warm:
            adjusted = apply_warm(adjusted)
        elif cool:
            adjusted = apply_cool(adjusted)
        
        # Convert adjusted image to RGB for display
        if len(adjusted.shape) == 2:  # Grayscale
            adjusted_rgb = cv2.cvtColor(adjusted, cv2.COLOR_GRAY2RGB)
        else:
            adjusted_rgb = cv2.cvtColor(adjusted, cv2.COLOR_BGR2RGB)
        
        with col2:
            st.image(adjusted_rgb, caption="Adjusted Image",  use_container_width=True)
        
        # Download button for the adjusted image
        pil_image = Image.fromarray(adjusted_rgb)
        buf = io.BytesIO()
        pil_image.save(buf, format="JPEG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="💾 Download adjusted image",
            data=byte_im,
            file_name="adjusted_image.jpg",
            mime="image/jpeg"
        )

if __name__ == "__main__":
    main()