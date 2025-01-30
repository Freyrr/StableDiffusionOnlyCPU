"""
Configuration settings for the Stable Diffusion CPU-only image generator.
This file contains all the customizable parameters for the image generation process.
"""

# Memory and Performance Settings
MAX_MEMORY = "4GB"  # Maximum memory usage for model loading
BATCH_SIZE = 1      # Number of images to generate per run
STEPS = 20          # Number of inference steps for generation
HEIGHT = 512        # Output image height
WIDTH = 512         # Output image width
GUIDANCE_SCALE = 7.5  # How strictly the image follows the prompt (higher = more strict)

# Model Settings
AVAILABLE_MODELS = [
    "CompVis/stable-diffusion-v1-4",
    "stabilityai/stable-diffusion-2-1",
    "runwayml/stable-diffusion-v1-5",
    "cagliostrolab/animagine-xl-4.0",
    "prompthero/openjourney"
]

# Output Settings
OUTPUT_DIR = "out"  # Directory where generated images will be saved
SAVE_FORMAT = "png"  # Format for saving generated images
FILENAME_PREFIX = "generated_image"  # Prefix for generated image filenames

# Advanced Settings
ENABLE_ATTENTION_SLICING = True  # Reduces memory usage at cost of speed
ENABLE_MODEL_CPU_OFFLOAD = True  # Offloads model to CPU when not in use
SEED = None  # Random seed for reproducibility (None for random)

# Safety Settings
SAFETY_CHECKER_ENABLED = True  # Enable/disable NSFW filter
ENABLE_WATERMARK = True  # Add watermark to generated images

# Logging Settings
ENABLE_LOGGING = True  # Enable detailed logging
LOG_LEVEL = "INFO"  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
