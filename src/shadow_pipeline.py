
import cv2
import numpy as np


def load_image(path):
    bgr = cv2.imread(str(path))
    if bgr is None:
        raise FileNotFoundError(f"Cannot load: {path}")
    return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)


def load_sample(img_dir, mask_dir, filename):
    import os
    img  = load_image(os.path.join(img_dir, filename))
    mask = cv2.imread(os.path.join(mask_dir, filename),
                      cv2.IMREAD_GRAYSCALE)
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    return img, mask


def generate_raw_mask(img_rgb, v_upper=90, s_lower=20):
    hsv   = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    lower = np.array([0,   s_lower, 0      ], dtype=np.uint8)
    upper = np.array([180, 255,     v_upper], dtype=np.uint8)
    return cv2.inRange(hsv, lower, upper)


def clean_mask(raw_mask, open_size=5, close_size=11):
    k_open  = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                         (open_size,  open_size))
    k_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                         (close_size, close_size))
    opened = cv2.morphologyEx(raw_mask, cv2.MORPH_OPEN,  k_open)
    return  cv2.morphologyEx(opened,   cv2.MORPH_CLOSE, k_close)


def create_overlay(img_rgb, mask,
                   shadow_color=(70, 130, 230), alpha=0.45):
    overlay = img_rgb.copy()
    overlay[mask == 255] = shadow_color
    return cv2.addWeighted(img_rgb, 1 - alpha, overlay, alpha, 0)


def detect(img_rgb, v_upper=90, s_lower=20,
           open_size=5, close_size=11):
    """
    Main entry point. Pass any RGB image, get back a results dict.
    """
    raw   = generate_raw_mask(img_rgb, v_upper=v_upper, s_lower=s_lower)
    clean = clean_mask(raw, open_size=open_size, close_size=close_size)
    return {
        "raw_mask"   : raw,
        "clean_mask" : clean,
        "overlay"    : create_overlay(img_rgb, clean),
        "shadow_pct" : (np.sum(clean == 255) / clean.size) * 100,
    }
