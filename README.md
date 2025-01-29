# CPU-Only Stable Diffusion Image Generator

A lightweight and efficient implementation of Stable Diffusion that runs entirely on CPU, making it accessible for users without dedicated GPUs. This project leverages multiple state-of-the-art AI models to provide diverse image generation capabilities, allowing users to experiment with different model architectures and styles.

## 🌟 Features

- **Multiple AI Models**: Automatically generates images using several pre-trained models:
  - Stable Diffusion v1.4 (CompVis)
  - Stable Diffusion v2.1 (Stability AI)
  - Stable Diffusion v1.5
  - Animagine XL 4.0 (Specialized in anime-style images)
  - OpenJourney (Midjourney-style images)
- **CPU-Only Operation**: Generate images without requiring a GPU
- **Memory Efficient**: Automatic memory management and cleanup
- **Easy to Use**: Simple interface for image generation
- **Organized Output**: Generated images are saved with model name and timestamp

## 🤖 AI Models in Detail

The project includes several carefully selected AI models, each with its own strengths:

1. **CompVis/stable-diffusion-v1-4**
   - Base Stable Diffusion model
   - Good all-around performance
   - Excellent for general-purpose image generation

2. **stabilityai/stable-diffusion-2-1**
   - Improved image quality over v1
   - Better understanding of prompts
   - Enhanced detail generation

3. **stable-diffusion-v1-5**
   - Refined version of v1.4
   - Better consistency in outputs
   - Improved handling of complex prompts

4. **cagliostrolab/animagine-xl-4.0**
   - Specialized in anime and manga-style images
   - High-quality character generation
   - Excellent for artistic and stylized content

5. **prompthero/openjourney**
   - Midjourney-inspired model
   - Artistic and creative outputs
   - Great for unique artistic interpretations

Each model will process the same prompt, allowing you to compare different interpretations and choose the best result for your needs.

## System Requirements

- Python 3.12 or higher
- Minimum 8GB RAM recommended for CPU processing
- Sufficient disk space for models and generated images

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone [url-repository]
   cd StableDiffusionOnlyCPU
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/MacOS
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Project Structure

```
StableDiffusionOnlyCPU/
├── ML/                 # Models and output directory
├── out/               # Generated images directory (one per model)
├── main.py            # Main script
├── requirements.txt   # Project dependencies
└── README.md         # Documentation
```

## 🎨 Usage

To generate images with all available models:

```bash
python main.py
```

This will:
1. Load each model sequentially
2. Generate an image from your prompt with each model
3. Save the results in the `out` directory with the format: `image_[model_name]_[timestamp].png`

## ⚙️ Customization

You can easily customize the image generation by:
1. Modifying the prompt in `main.py`
2. Enabling/disabling specific models in the `AVAILABLE_MODELS` list
3. Adjusting the output directory in the `generate_and_save_image` function

## Main Dependencies

- diffusers>=0.24.0
- torch>=2.1.0
- transformers>=4.36.0
- accelerate>=0.25.0

## Notes

- The first run will require downloading the model (approximately 4GB)
- CPU processing may take longer than GPU processing
- The model will be downloaded automatically on the first run

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License is a permissive license that is short and to the point. It lets people do anything they want with your code as long as they provide attribution back to you and don't hold you liable. Specifically, this means:

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ✅ Sublicensing

Note: While this project's code is MIT licensed, the AI models used have their own licenses and terms of use. Please refer to each model's documentation for their specific usage terms.
