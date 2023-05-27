from easygoogletranslate import EasyGoogleTranslate

translator = EasyGoogleTranslate(
    source_language='se',
    target_language='en',
    timeout=10
)

def translate(text: str) -> str:
    return translator.translate(text)

