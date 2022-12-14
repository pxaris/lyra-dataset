# The Lyra Dataset

**Lyra** is a dataset for Greek Traditional and Folk music that includes 1570 pieces, summing in around 80 hours of data. The dataset incorporates YouTube timestamped links for retrieving audio and video, along with rich metadata information with regards to instrumentation, geography and genre, among others.


## Structure

### Data files in [`data`](data)

- `raw.tsv` - raw file with all metadata

- `split/` - training and test set split
    - `training.tsv` - raw file with all metadata of samples used for the training
    - `test.tsv` - raw file with all metadata of the test set samples

- `metadata-information/` - information about metadata
    - `genres_hierarchy.json` - hierarchical relationships between all genres
    - `places_coordinates.json` - coordinates of each place
    - `places_hierarchy.json` - hierarchical relationships of each place
    - `vocabulary.json` - vocabulary with the definitions of the terms evident in the dataset 

- `mel-spectrograms/` - the mel-spectrograms of all music pieces following the naming convention `{id}.npy` can be downloaded from [here](https://drive.google.com/file/d/10SH2gfYSf_qUVPUHA3O1lgq4C24k38I0/view?usp=sharing).  


## Using the trained models for [`inference`](inference)

### Requirements

* [FFmpeg](https://ffmpeg.org/download.html) 
* Python 3.8 or later
* Create virtual environment and install requirements
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Get inference results

1. Download trained models from [here](https://drive.google.com/file/d/1nFu3G4WX8OAtiSX4UlkqI0KvfW2FIn0u/view?usp=sharing) and put them under `models/` directory.
2. Place an `input.wav` file under `inference/` or use a different name and adjust `INPUT_FILE` at `run_inference.py` accordingly.
3. Run: `python inference/run_inference.py`
4. The inference results will be printed in the terminal.


## Citing the dataset

Please consider citing [the following publication](https://arxiv.org/abs/2211.11479v1) when using the dataset:

> C. Papaioannou, I. Valiantzas, T. Giannakopoulos, M. Kaliakatsos-Papakostas and A. Potamianos, "A Dataset for Greek Traditional and Folk Music: Lyra", in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022.


## License

- The metadata is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

