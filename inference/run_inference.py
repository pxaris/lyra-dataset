import os
import pickle
import numpy as np
from pathlib import Path
from deep_audio_features.bin import basic_test as btest


INPUT_FILE = os.path.join('inference', 'input.wav')

GENRE_MODEL = os.path.join('models', 'genre.pt')
PLACE_MODEL = os.path.join('models', 'place.pt')
INSTRUMENT_MODELS = [os.path.join('models', 'instruments', instrument) + '.pt' for instrument in [
    'klarino', 'guitar', 'laouto', 'percussion', 'violin', 'voice']]


def convert_audio_to_1channel(input_file, output_file='temp.wav'):
    command = f'ffmpeg -i \"{input_file}\" -ar 8000 -ac 1 {output_file} -y'
    os.system(command)
    return output_file


def get_classes_mapping_of_model(model):
    with open(model, "rb") as f:
        model_params = pickle.load(f)
    return model_params['classes_mapping']


def get_model_inference_result(model, input_audio, is_binary=False):
    d, _ = btest.test_model(model, input_audio,
                            layers_dropped=0, test_segmentation=True)
    count_decisions = np.bincount(d)
    if is_binary:
        positive_probability = count_decisions[0] / np.sum(count_decisions)
        prediction = 0 if positive_probability >= 0.5 else 1
    else:
        prediction = np.argmax(count_decisions)
    return prediction


def get_inference_result(audio_file):
    input_1channel = convert_audio_to_1channel(audio_file)

    # genre
    y_pred = get_model_inference_result(GENRE_MODEL, input_1channel)
    genre_prediction = get_classes_mapping_of_model(GENRE_MODEL)[y_pred]

    # place
    y_pred = get_model_inference_result(PLACE_MODEL, input_1channel)
    place_prediction = get_classes_mapping_of_model(PLACE_MODEL)[y_pred]

    # instruments
    instruments_prediction = []
    for instrument_model in INSTRUMENT_MODELS:
        y_pred = get_model_inference_result(
            instrument_model, input_1channel, is_binary=True)
        if y_pred == 0:
            instruments_prediction.append(
                get_classes_mapping_of_model(instrument_model)[y_pred].title())

    # remove created 1channel file
    Path(input_1channel).unlink(missing_ok=True)

    result = f'\n\n- Inference results for "{audio_file}" audio:\n\
        - genre: {genre_prediction}\n\
        - place of origin: {place_prediction}\n\
        - instruments: {", ".join(sorted(instruments_prediction, reverse=True))}'

    return result


if __name__ == '__main__':
    inference_result = get_inference_result(INPUT_FILE)
    print(inference_result)
