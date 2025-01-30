# CPU-Only Stable Diffusion Image Generator

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Freyrr/StableDiffusionOnlyCPU/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![CPU Only](https://img.shields.io/badge/CPU-Only-orange.svg)]()
[![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-v1.4%20|%20v1.5%20|%20v2.1-blue.svg)]()
[![AI Models](https://img.shields.io/badge/AI%20Models-5%2B-purple.svg)]()
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%96%20HuggingFace-Models-yellow.svg)](https://huggingface.co/)

Benvenuti nel progetto CPU-Only Stable Diffusion Image Generator! Questo è un potente strumento che democratizza la generazione di immagini tramite AI, rendendo accessibile a tutti la magia della creazione artistica attraverso l'intelligenza artificiale, anche senza disporre di costose GPU.

Questo progetto innovativo ti permette di sperimentare con diversi modelli di Stable Diffusion e altre architetture AI, tutti ottimizzati per funzionare esclusivamente su CPU. Potrai generare immagini straordinarie semplicemente descrivendo ciò che desideri vedere, e il sistema utilizzerà automaticamente multiple versioni di modelli AI per offrirti diverse interpretazioni della tua idea.

Immagina di poter creare arte digitale, concept art, illustrazioni o qualsiasi altra forma di contenuto visivo semplicemente descrivendo la tua visione in parole. Questo è esattamente ciò che questo progetto ti permette di fare, offrendo:

- La possibilità di confrontare i risultati tra diversi modelli AI
- Un'implementazione ottimizzata per CPU che non richiede hardware specializzato
- Un'interfaccia semplice e intuitiva per la generazione di immagini
- La libertà di sperimentare con diversi stili e approcci artistici

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

## 📊 Performance

- Average generation time: 2-3 minutes per image on CPU
- Memory usage: ~4-6GB RAM during generation
- Disk space required: ~10GB for all models

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

## 🔧 Configuration

You can customize the generation parameters in `config.py`:

```python
# Example configuration
MAX_MEMORY = "4GB"  # Maximum memory usage
BATCH_SIZE = 1      # Number of images to generate
STEPS = 20          # Number of inference steps
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

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for details on the latest updates and modifications.

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

This project's code is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

⚠️ **Important License Notice**

While our code is MIT licensed, the actual usage of this project is subject to the licenses of the AI models being used. Each model has its own terms and conditions that **must** be followed:

1. **CompVis/stable-diffusion-v1-4**: [CreativeML Open RAIL-M License](https://huggingface.co/CompVis/stable-diffusion-v1-4/blob/main/LICENSE)
2. **stabilityai/stable-diffusion-2-1**: [CreativeML Open RAIL-S License](https://huggingface.co/stabilityai/stable-diffusion-2-1/blob/main/LICENSE.md)
3. **stable-diffusion-v1-5**: [CreativeML Open RAIL-M License](https://huggingface.co/runwayml/stable-diffusion-v1-5/blob/main/LICENSE.md)
4. **cagliostrolab/animagine-xl-4.0**: [CreativeML Open RAIL-M License](https://huggingface.co/cagliostrolab/animagine-xl-4.0/blob/main/LICENSE)
5. **prompthero/openjourney**: [CreativeML Open RAIL-M License](https://huggingface.co/prompthero/openjourney/blob/main/LICENSE)

**Your use of this project must comply with all licenses involved, including both our MIT license and the respective AI model licenses.**

However, these permissions are limited by the AI model licenses. For example, some models may:
- ⚠️ Restrict commercial use
- ⚠️ Require attribution
- ⚠️ Have specific usage guidelines
- ⚠️ Prohibit certain types of content generation

**Please review each model's license before using it in your projects.**
