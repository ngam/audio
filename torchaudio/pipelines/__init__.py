from ._wav2vec2.impl import (
    Wav2Vec2Bundle,
    Wav2Vec2ASRBundle,
    WAV2VEC2_BASE,
    WAV2VEC2_LARGE,
    WAV2VEC2_LARGE_LV60K,
    WAV2VEC2_ASR_BASE_10M,
    WAV2VEC2_ASR_BASE_100H,
    WAV2VEC2_ASR_BASE_960H,
    WAV2VEC2_ASR_LARGE_10M,
    WAV2VEC2_ASR_LARGE_100H,
    WAV2VEC2_ASR_LARGE_960H,
    WAV2VEC2_ASR_LARGE_LV60K_10M,
    WAV2VEC2_ASR_LARGE_LV60K_100H,
    WAV2VEC2_ASR_LARGE_LV60K_960H,
    WAV2VEC2_XLSR53,
    VOXPOPULI_ASR_BASE_10K_EN,
    VOXPOPULI_ASR_BASE_10K_ES,
    VOXPOPULI_ASR_BASE_10K_DE,
    VOXPOPULI_ASR_BASE_10K_FR,
    VOXPOPULI_ASR_BASE_10K_IT,
    HUBERT_BASE,
    HUBERT_LARGE,
    HUBERT_XLARGE,
    HUBERT_ASR_LARGE,
    HUBERT_ASR_XLARGE,
)
from ._tts import (
    Tacotron2TTSBundle,
    TACOTRON2_GRIFFINLIM_CHAR_LJSPEECH,
    TACOTRON2_GRIFFINLIM_PHONE_LJSPEECH,
    TACOTRON2_WAVERNN_CHAR_LJSPEECH,
    TACOTRON2_WAVERNN_PHONE_LJSPEECH,
)

__all__ = [
    'Wav2Vec2Bundle',
    'Wav2Vec2ASRBundle',
    'WAV2VEC2_BASE',
    'WAV2VEC2_LARGE',
    'WAV2VEC2_LARGE_LV60K',
    'WAV2VEC2_ASR_BASE_10M',
    'WAV2VEC2_ASR_BASE_100H',
    'WAV2VEC2_ASR_BASE_960H',
    'WAV2VEC2_ASR_LARGE_10M',
    'WAV2VEC2_ASR_LARGE_100H',
    'WAV2VEC2_ASR_LARGE_960H',
    'WAV2VEC2_ASR_LARGE_LV60K_10M',
    'WAV2VEC2_ASR_LARGE_LV60K_100H',
    'WAV2VEC2_ASR_LARGE_LV60K_960H',
    'WAV2VEC2_XLSR53',
    'VOXPOPULI_ASR_BASE_10K_EN',
    'VOXPOPULI_ASR_BASE_10K_ES',
    'VOXPOPULI_ASR_BASE_10K_DE',
    'VOXPOPULI_ASR_BASE_10K_FR',
    'VOXPOPULI_ASR_BASE_10K_IT',
    'HUBERT_BASE',
    'HUBERT_LARGE',
    'HUBERT_XLARGE',
    'HUBERT_ASR_LARGE',
    'HUBERT_ASR_XLARGE',
    'Tacotron2TTSBundle',
    'TACOTRON2_GRIFFINLIM_CHAR_LJSPEECH',
    'TACOTRON2_GRIFFINLIM_PHONE_LJSPEECH',
    'TACOTRON2_WAVERNN_CHAR_LJSPEECH',
    'TACOTRON2_WAVERNN_PHONE_LJSPEECH',
]
