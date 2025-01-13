import markitdown
from markitdown import MarkItDown

md = MarkItDown(ocr_client="easyocr")
result = md.convert("/Users/vdaleke/Projects/markitdown/tests/test_files/test.jpg")

print(result.text_content)
