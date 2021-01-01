from . import utils, constants
from .video import Video


def get_subtitles(
        video_path: str, lang='eng', time_start='0:00', time_end='',
        conf_threshold=65, sim_threshold=90, use_fullframe=False, engine=constants.OCR_ENGINE_TESSERACT) -> str:
    if engine == constants.OCR_ENGINE_TESSERACT:
        utils.download_lang_data(lang)
    elif engine not in [constants.OCR_ENGINE_TESSERACT, constants.OCR_ENGINE_EASYOCR]:
        raise ValueError('Invalid OCR engine "{}"'.format(engine))

    v = Video(video_path)
    v.run_ocr(lang, time_start, time_end, conf_threshold, use_fullframe, engine)
    return v.get_subtitles(sim_threshold)


def save_subtitles_to_file(
        video_path: str, file_path='subtitle.srt', lang='eng',
        time_start='0:00', time_end='', conf_threshold=65, sim_threshold=90,
        use_fullframe=False, engine=constants.OCR_ENGINE_TESSERACT) -> None:
    with open(file_path, 'w+', encoding='utf-8') as f:
        f.write(get_subtitles(
            video_path, lang, time_start, time_end, conf_threshold,
            sim_threshold, use_fullframe, engine))
