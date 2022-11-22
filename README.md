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

- `mel-spectrograms/` - the mel-spectrograms of all music pieces following the naming convention `{id}.npy`.  


## Citing the dataset

Please consider citing [the following publication](https://arxiv.org/abs/2211.11479v1) when using the dataset:

> C. Papaioannou, I. Valiantzas, T. Giannakopoulos, M. Kaliakatsos-Papakostas and A. Potamianos, "A Dataset for Greek Traditional and Folk Music: Lyra", in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022.


## License

- The metadata is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

