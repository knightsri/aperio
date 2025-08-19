# Project Aperio: AI-Powered Schema Discovery with LangExtract

[![LangExtract](https://img.shields.io/badge/Powered%20by-LangExtract-blue)](https://github.com/google/langextract)
[![Python](https://img.shields.io/badge/Python-3.11+-green)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Zero manual schema writing. Maximum extraction intelligence.**

Interactive Jupyter notebook demonstrating Google's LangExtract capabilities for **AI-powered schema discovery** and structured data extraction from unstructured text. Watch as LangExtract analyzes your data and automatically suggests optimal extraction patterns!

## Live Demo

- **[View Interactive Showcase](https://knightsri.github.io/aperio/)** - Visual demonstration with key results
- **[Technical Notebook](https://knightsri.github.io/aperio/notebook.html)** - Complete implementation details

## Key Features

- **AI Schema Discovery** - No manual YAML configuration required
- **Medical Use Case** - Extract patient data, medications, and diagnoses from clinical notes
- **Scientific Use Case** - Parse research papers for methods, datasets, and findings  
- **Cross-Domain Intelligence** - Same tool, completely different schemas automatically discovered
- **Knowledge Graphs** - Visualize extracted relationships with network graphs
- **Zero Configuration** - Just provide sample text and natural language description

## Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/knightsri/aperio
cd aperio

# Create virtual environment
python -m venv aperio_env
source aperio_env/Scripts/activate  # Windows
# source aperio_env/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Copy the example file and add your key
cp .env.example .env
# Edit .env and add your Gemini API key:
# LANGEXTRACT_API_KEY=your_actual_gemini_api_key_here
```

### 3. Run the Demo

```bash
# Start Jupyter Notebook
jupyter notebook aperio_demo.ipynb

# Or use VS Code
code aperio_demo.ipynb
```

## What You'll See

### Schema Discovery in Action

```python
# Just provide sample text and context
sample_text = "Dr. Smith prescribed 10mg lisinopril for hypertension..."
context = "Extract medical information for healthcare analytics"

# LangExtract automatically discovers:
# PATIENT_DEMO: Age, gender
# MEDICATIONS: Drug names, dosages, frequencies  
# CONDITIONS: Diagnoses, symptoms
# No manual schema required!
```

### Cross-Domain Adaptability

```
MEDICAL DOMAIN → Patient care focus
   • PATIENT_DEMO, MEDICATION, CONDITION, DIAGNOSIS, TREATMENT

SCIENTIFIC DOMAIN → Research focus  
   • METHOD, PERFORMANCE, DATASET, INFRASTRUCTURE, IMPROVEMENT
   
Same LangExtract tool, completely different schemas discovered automatically!
```

## Demo Results

- **Medical Domain**: 8 extractions across 5 categories
- **Scientific Domain**: 7 extractions across 5 categories  
- **Total**: 15 entities extracted with **zero manual schema writing**
- **Configuration Files**: 0 YAML files needed

## Technical Stack

- **AI Engine**: [Google LangExtract](https://github.com/google/langextract)
- **Environment**: Jupyter Notebook
- **Visualization**: NetworkX, Matplotlib
- **Data Processing**: Pandas, NumPy
- **Model**: Gemini 2.0 Flash

## Project Structure

```
aperio/
├── aperio_demo.ipynb          # Main interactive demonstration
├── requirements.txt           # Python dependencies
├── .env.example              # API key template
├── .env                      # Your API keys (create this)
├── DESIGN_SPECIFICATION.md   # Detailed project documentation
└── README.md                 # This file
```

## Educational Value

Perfect for developers who want to:

- **Learn LangExtract** through hands-on examples
- **Understand AI schema discovery** vs traditional extraction
- **See cross-domain adaptability** in action
- **Build their own extraction workflows** using discovered patterns
- **Explore knowledge graph visualizations** of extracted data

## Requirements

- Python 3.11+
- Gemini API key (get from [Google AI Studio](https://aistudio.google.com/))
- ~10 minutes setup time
- Basic familiarity with Jupyter notebooks

## Key Innovations

### 1. Zero-Configuration Extraction

Traditional approach:

```yaml
# Manual schema.yaml - hours of work
extraction_schema:
  patient_info:
    age: "Extract age near 'year-old'"
    gender: "Extract male or female"
  # ... 50+ more lines
```

Aperio approach:

```python
# AI discovers schema automatically
result = lx.extract(
    text=medical_text,
    prompt="Extract patient info for healthcare analytics",
    examples=[simple_example]  # Just one example!
)
```

### 2. Domain Intelligence

LangExtract analyzes text characteristics and automatically adapts extraction patterns:

- **Medical text** → Focus on patient care, treatments, diagnoses
- **Scientific text** → Focus on methods, datasets, performance metrics
- **Legal text** → Would focus on clauses, parties, obligations
- **Business text** → Would focus on metrics, decisions, stakeholders

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Use Cases

- **Healthcare**: Structure clinical notes, extract medication lists, analyze patient data
- **Research**: Parse academic papers, extract methodologies, track research trends
- **Legal**: Extract clauses from contracts, identify key terms and parties
- **Business**: Analyze reports, extract KPIs, structure feedback data
- **Content**: Process articles, extract entities, create knowledge bases

## Disclaimer

This demonstration is for educational and illustrative purposes. For production healthcare applications, ensure compliance with relevant regulations (HIPAA, etc.). LangExtract extraction accuracy may vary based on text complexity and domain specificity.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Google LangExtract Team** for the AI extraction library
- **Medical transcription dataset** from Kaggle
- **arXiv dataset** for scientific paper abstracts
- **Open source community** for Jupyter, NetworkX, and visualization tools

## Show Your Support

If this project helped you understand LangExtract's capabilities, please star this repository and share it with others who might find it useful.

---

**Built with intelligence. Powered by LangExtract. Designed for developers.**
