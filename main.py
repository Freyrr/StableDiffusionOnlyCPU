from diffusers import DiffusionPipeline
import os
from datetime import datetime

# List of available models
AVAILABLE_MODELS = [
    "CompVis/stable-diffusion-v1-4",
    "stabilityai/stable-diffusion-2-1",
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    #"stabilityai/stable-diffusion-3.5-medium",
    "cagliostrolab/animagine-xl-4.0",
    #"black-forest-labs/FLUX.1-dev",
    "prompthero/openjourney"
]

def generate_and_save_image(model_name, prompt, output_dir="out"):
    """
    Generate an image using Stable Diffusion and save it to the specified directory
    
    Args:
        model_name (str): Name of the model to use
        prompt (str): Text description of the image to generate
        output_dir (str): Directory where to save the image (default: 'out')
    
    Returns:
        str: Path of the saved file if successful, None if error
    """
    try:
        # Initialize the model
        pipe = DiffusionPipeline.from_pretrained(model_name)
        
        # Extract model name from path
        model_short_name = model_name.split('/')[-1].replace('-', '_').replace('.', '_')
        
        # Generate the image
        image = pipe(prompt).images[0]
        
        # Create filename with timestamp and model name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(output_dir, f"image_{model_short_name}_{timestamp}.png")
        
        # Save the image
        image.save(output_path)
        print(f"✅ Image saved to: {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Error during image generation/saving with model {model_name}:")
        print(f"   {str(e)}")
        return None
    finally:
        # Free memory
        del pipe

# Define the prompt
prompt = "Create a high-resolution professional logo for an educational farm that should include: a tractor, a sun, a cow, and a chicken."

# Generate and save image for each model
for model in AVAILABLE_MODELS:
    print(f"\nGenerating image with model: {model}")
    generate_and_save_image(model, prompt)