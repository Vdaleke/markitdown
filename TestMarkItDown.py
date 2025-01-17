import markitdown
from markitdown import MarkItDown

# EasyOCR usecase
import easyocr

md = MarkItDown(ocr_client=easyocr.Reader(lang_list=["en", "ru"], gpu=False))
result = md.convert("/Users/vdaleke/Projects/markitdown/tests/test_files/test.jpg")

print(result.text_content)

# Yandex Visual OCR usecase
from markitdown import OCRClient
from typing import Any, List
import requests
import base64

class YandexVisualOCRClient(OCRClient):
    def __init__(self, iam_token: str, folder_id: str):
        self.iam_token = iam_token
        self.folder_id = folder_id
    
    @staticmethod  
    def __get_file_mime_type(self, file_path):
        file_extension = file_path.split('.')[-1].lower()

        if file_extension == 'jpg' or file_extension == 'jpeg':
            return 'JPEG'
        elif file_extension == 'png':
            return 'PNG'
        elif file_extension == 'pdf':
            return 'PDF'
        else:
            return 'Unknown file type'

    @staticmethod
    def __encode_file(self, file_path):
        with open(file_path, "rb") as fid:
            file_content = fid.read()
        return base64.b64encode(file_content).decode("utf-8")
    
    def readtext(self, local_path) -> List[tuple[Any, str, Any]]:
        data = {"mimeType": self.__get_file_mime_type(local_path),
                "languageCodes": ["*"],
                "content": self.__encode_file(local_path)}
        
        url = "https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText"
        
        headers= {"Content-Type": "application/json",
                "Authorization": "Bearer {:s}".format(self.iam_token),
                "x-folder-id": self.folder_id,
                "x-data-logging-enabled": "true"}
        
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        
        result = []
        if 'result' not in response_data or 'textAnnotation' not in response_data['result']:
            return result

        text_annotations = response_data['result']['textAnnotation']
        blocks = text_annotations.get('blocks', [])
        for block in blocks:
            for line in block.get('lines', []):
                text = line.get('text', '')
                bounding_box = line.get('boundingBox', {})
                vertices = bounding_box.get('vertices', [])
                result.append((vertices, text, None)) 

        return result
        
user_iam_token = input("Enter IAM token: ")
user_folder_id = input("Enter folder id: ")
md = MarkItDown(ocr_client=YandexVisualOCRClient(iam_token=user_iam_token, folder_id=user_folder_id))
result = md.convert("/Users/vdaleke/Projects/markitdown/tests/test_files/test.jpg")

print(result.text_content)

# ============= EasyOCR OUTPUT =================================
# 
# # Text:
# - AutoGen: Enabling Next-Gen LLM
# - Applications via Multi-Agent Conversation
# - Qingyun Wut , Gagan Bansal
# - Jieyu Zhangt , Yiran Wut , Beibin Li*
# - Erkang Zhu
# - Li Jiang*
# - Xiaoyun Zhang *
# - Shaokun Zhangt
# - Jiale
# - Ahmed Awadallah
# - Ryen W White* , Doug Burger
# - Chi Wang*1
# - 8
# - Microsoft Research; tPennsylvania State University
# - +University of Washington; #Xidian University
# - 8
# - 0
# - Conversable agent
# - Plot
# - chart of
# - Output:
# - META and TESL
# - stcck рrice change
# - YTD
# - 2
# - followeg codee
# - Month
# - Multi-Agent Conversations
# - Еггог package
# - No; please
# - yfinаnсе is not
# - change
# - installed
# - Got it! Неге is the
# - Sorry!
# - lease first
# - revlsed ccde
# - pip install yfinапсе
# - and then execute
# - Output:
# - the ccde
# - Installing
# - Joint chat
# - Hierarchical chat
# - 2
# - Agent Customization
# - Flexible Conversation Patterns
# - Example Agent Chat
# - Month
# - Figure 1: AutoGen enables diverse LLM-based
# - applications using multi-agent conversations  (Left)
# - AutoGen agents are conversable; customizable; and can be based on LLMs; tools; humans; or even
# - a combination of them. (Top-middle)
# - Agents can converse to solve tasks
# - (Right)
# - can form
# - chat;   potentially with humans in the
# - (Bottom-middle)  The framework supports flexible
# - conversation patterns
# - а
# - bstract
# - AutoGen? is an open-source framework that allows developers to build LLM ар-
# - plications via multiple agents that can converse with each other to accomplish
# - tasks:
# - AutoGen agents are customizable; conversable, and can operate in
# - ous modes that employ combinations of LLMs; human inputs; and tools. Using
# - AutoGen; developers can also fexibly define agent interaction behaviors:
# - Both
# - natural language and computer code can be used to program flexible conversation
# - patterns for different applications:
# - AutoGen
# - serves as
# - generic framework for
# - building diverse applications of various complexities and LLM capacities  Em-
# - pirical studies demonstrate the effectiveness of the framework in many example
# - applications; with domains ranging from mathematics; coding; question answer-
# - operations research; online decision-making; entertainment; etc.
# - 1Corresponding author: Email: auto-gen@outlook com
# - 1Igithub_
# - com/microsoft/autogen
# - LiuF
# - Plot
# - They
# - loop.
# - vari-
# - ing;
# - 2https:

# ============= Yandex Vision OCR =============================

# # Text:
# - AutoGen: Enabling Next-Gen LLM
# - Applications via Multi-Agent Conversation
# - Qingyun Wu', Gagan Bansal*, Jieyu Zhang1, Yiran Wu', Beibin Li*
# - Erkang Zhu*, Li Jiang*, Xiaoyun Zhang*, Shaokun Zhang', Jiale Liu*
# - Conversable agent
# - Agent Customization
# - Ahmed Awadallah*, Ryen W. White*, Doug Burger*, Chi Wang*1
# - *Microsoft Research, Pennsylvania State University
# - #University of Washington,+Xidian University
# - Multi-Agent Conversations
# - Joint chat
# - Hierarchical chat
# - Flexible Conversation Patterns
# - Figure 1: AutoGen enables diverse LLM-based applications using multi-agent conversations. (Left)
# - AutoGen agents are conversable, customizable, and can be based on LLMs, tools, humans, or even
# - a combination of them. (Top-middle) Agents can converse to solve tasks. (Right) They can form
# - a chat, potentially with humans in the loop. (Bottom-middle) The framework supports flexible
# - conversation patterns.
# - Abstract
# - Plot a chart of
# - META and TESLA
# - stock price change
# - YTD.
# - Error package
# - yfinance is not
# - installed
# - Execute the
# - following code…
# - Sorry! Please first
# - pip install yfinance
# - and then execute
# - the code
# - Installing…
# - Example Agent Chat
# - Output:
# - Output:
# - Month
# - No, please plot %
# - change!
# - Got it! Here is the
# - revised code …
# - Month
# - AutoGen2 is an open-source framework that allows developers to build LLM ap-
# - plications via multiple agents that can converse with each other to accomplish
# - tasks. AutoGen agents are customizable, conversable, and can operate in vari-
# - ous modes that employ combinations of LLMs, human inputs, and tools. Using
# - AutoGen, developers can also flexibly define agent interaction behaviors. Both
# - natural language and computer code can be used to program flexible conversation
# - patterns for different applications. AutoGen serves as a generic framework for
# - building diverse applications of various complexities and LLM capacities. Em-
# - pirical studies demonstrate the effectiveness of the framework in many example
# - applications, with domains ranging from mathematics, coding, question answer-
# - ing, operations research, online decision-making, entertainment, etc.
# - 1Corresponding author. Email: auto-gen@outlook.com
# - 2https:// github.com/microsoft/autogen

