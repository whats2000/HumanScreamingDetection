# HumanScreamingDetection

## Description
HumanScreamingDetection is a Python-based application designed to detect human screaming sounds in audio data. This project uses machine learning techniques, specifically with a focus on audio processing, to identify screaming sounds. It can be applied in various safety and monitoring systems.

## Installation
Clone the repository and install the required dependencies:
```
git clone https://github.com/whats2000/HumanScreamingDetection.git
cd HumanScreamingDetection
pip install -r requirements.txt
```

## Dataset
To download the dataset, you have two options:
1. Directly from Kaggle: [Human Screaming Detection Dataset](https://www.kaggle.com/datasets/whats2000/human-screaming-detection-dataset)
2. Using the provided Jupyter notebooks:
   - Download control audio data: `HumanScreamingDetection/DownloadControlAudioData.ipynb`
   - Download sample audio data: `HumanScreamingDetection/DownloadSampleAudioData.ipynb`

## Data Preprocessing
The data cleaning and preprocessing methods are detailed in the Jupyter notebook `HumanScreamingDetection/TransformData.ipynb`.

## Model Training
The model training process is conducted in the notebook `HumanScreamingDetection/Resnet34Train.ipynb`.

## Usage
To run the application, navigate to the `AppForTesting` directory and execute `App.py`:
```
cd AppForTesting
python App.py
```

## Contributing
Contributions to the HumanScreamingDetection project are welcome. 

## License
This project is licensed under the GPL-3.0 license License - see the [LICENSE](https://github.com/whats2000/HumanScreamingDetection/blob/main/LICENSE) file for details.

## Contact
For any queries or contributions, please contact Create Issue here.
