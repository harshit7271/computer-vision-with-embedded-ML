# Electronic Components Classifier 🚀
Deep Learning model classifying electronic components from BMP images using CNNs. Achieved 92% test accuracy on real-world dataset.

---
# 🎯 Results
```bash
Test Accuracy: 92.00%  🎉

Test Loss:    0.1900

Val Accuracy: 90.00%

Val Loss:     0.3957
```

---
# 📁 Dataset
- 300+ BMP images of electronic components

- Classes: Resistor, Capacitor, Transistor, Diode, ICs, etc.

- Organized in electronic_components/ folder structure

- Processed in Google Colab

---
# Quick Start
```bash
git clone https://github.com/harshit7271/computer-vision-with-embedded-ML.git

```
**Upload Dataset**
```bash
# Upload your BMP zip to Colab
from google.colab import files
uploaded = files.upload()
!unzip electronic-components-bmp.zip -d /content/electronic_components/
```
