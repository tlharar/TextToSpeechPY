from transformers import VitsModel, AutoTokenizer
import torch
import numpy as np
from pydub import AudioSegment
from IPython.display import Audio


def readText(text):


    model = VitsModel.from_pretrained("facebook/mms-tts-tur")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-tur")

    text = str(text)
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs).waveform


    output_np = output.cpu().numpy()


    output_normalized = (output_np / np.max(np.abs(output_np)) * 32767).astype(np.int16)

    audio = AudioSegment(
        output_normalized.tobytes(),
        frame_rate=model.config.sampling_rate,
        sample_width=output_normalized.dtype.itemsize,
        channels=1
    )

    audio.export("techno.wav", format="wav")

    Audio("techno.wav", rate=model.config.sampling_rate)
