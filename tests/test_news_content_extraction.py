from src.dnt_etl.extract import get_content

def test_extract_content():
    content = get_content("https://www.dn.se/sverige/regionen-kritisk-mot-flytt-av-slussens-bussterminal/")
    assert "För att använda den här funktionen behöver du vara inloggad." in content
