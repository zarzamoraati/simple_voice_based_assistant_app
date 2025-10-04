# import pyttsx3
# import pyautogui
# import base64
# import requests
# from fpdf import FPDF
# import webbrowser
# import os
# from dotenv import load_dotenv


# load_dotenv()


# GEMINI_KEY=os.getenv("GEMINI_API_KEY")


# # Initialize text-to-speech engine
# tts_engine = pyttsx3.init()

# # Function to speak text
# def speak(text):
#     tts_engine.say(text)
#     tts_engine.runAndWait()

# # Prebuilt prompt template
# prompt_template = """
# Process the following instruction on the provided screen capture (which may contain an invoice or relevant content):
# Instruction: {instruction}
# """

# # Variables to store data
# instruction = None
# screen_image_path = None
# response_text = None
# pdf_filename = "response.pdf"
# api_key = GEMINI_KEY  # Replace with your actual Gemini API key

# # Main loop for processing text input
# speak("System started. Enter commands: record, stop, capture, process, open, or exit.")
# while True:
#     try:
#         # Get text input from user
#         command = input("Enter command: ").lower().strip()
#         print(f"Received command: {command}")  # For debugging

#         if command == "exit":
#             speak("Exiting system.")
#             break

#         elif command == "record":
#             speak("Please enter your instruction.")
#             instruction = input("Enter instruction: ").strip()
#             speak("Instruction recorded.")
#             print(f"Instruction: {instruction}")

#         elif command == "stop":
#             instruction = None
#             speak("Recording stopped. Instruction cleared.")
#             print("Instruction cleared.")

#         elif command == "capture":
#             speak("Capturing screen.")
#             screenshot = pyautogui.screenshot()
#             screen_image_path = "screen_capture.png"
#             screenshot.save(screen_image_path)
#             speak("Screen captured.")

#         elif command == "process":
#             if instruction and screen_image_path:
#                 speak("Processing data with LLM.")
                
#                 # Read and base64 encode the image
#                 with open(screen_image_path, "rb") as image_file:
#                     image_data = base64.b64encode(image_file.read()).decode('utf-8')
                
#                 # Format the prompt
#                 formatted_prompt = prompt_template.format(instruction=instruction)
                
#                 # Gemini API endpoint (using gemini-1.5-flash for multimodal)
#                 #url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
#                 url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
                
#                 # Request payload
#                 payload = {
#                     "contents": [
#                         {
#                             "parts": [
#                                 {"text": formatted_prompt},
#                                 {
#                                     "inline_data": {
#                                         "mime_type": "image/png",
#                                         "data": image_data
#                                     }
#                                 }
#                             ]
#                         }
#                     ]
#                 }
                
#                 # Send request to Gemini API
#                 response = requests.post(url, json=payload)
                
#                 if response.status_code == 200:
#                     # Extract the generated text
#                     response_json = response.json()
#                     response_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
#                     speak("Processing successful. Here is the response.")
#                     speak(response_text)
                    
#                     # Generate PDF
#                     pdf = FPDF()
#                     pdf.add_page()
#                     pdf.set_font("Arial", size=12)
#                     pdf.multi_cell(200, 10, txt=response_text)
#                     pdf.output(pdf_filename)
#                     speak("PDF generated.")
#                 else:
#                     speak("Error processing with LLM.")
#                     print(f"Error: {response.text}")
#             else:
#                 speak("Missing instruction or screen capture. Please record and capture first.")

#         elif command == "open":
#             if os.path.exists(pdf_filename):
#                 speak("Opening PDF in browser.")
#                 webbrowser.open(f"file://{os.path.abspath(pdf_filename)}")
#             else:
#                 speak("No PDF generated yet.")

#         else:
#             speak("Unknown command. Please enter: record, stop, capture, process, open, or exit.")

#     except Exception as e:
#         speak("An error occurred.")
#         print(f"Error: {e}")


# import pyttsx3
# import pyautogui
# import base64
# import requests
# from fpdf import FPDF
# import webbrowser
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Get Gemini API key
# GEMINI_KEY = os.getenv("GEMINI_API_KEY")
# if not GEMINI_KEY:
#     raise ValueError("GEMINI_API_KEY not found in .env file")

# # Initialize text-to-speech engine with configuration
# tts_engine = pyttsx3.init()
# tts_engine.setProperty('rate', 150)  # Adjust speech rate (words per minute)
# tts_engine.setProperty('volume', 0.9)  # Set volume (0.0 to 1.0)

# # Function to speak text, handling long responses
# def speak(text):
#     try:
#         # Split long text into chunks to avoid pyttsx3 issues
#         max_chunk_length = 500  # Maximum characters per chunk
#         if len(text) > max_chunk_length:
#             chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
#             for chunk in chunks:
#                 tts_engine.say(chunk)
#                 tts_engine.runAndWait()
#         else:
#             tts_engine.say(text)
#             tts_engine.runAndWait()
#     except Exception as e:
#         print(f"Text-to-speech error: {e}")

# # Prebuilt prompt template
# prompt_template = """
# Process the following instruction on the provided screen capture (which may contain an invoice or relevant content):
# Instruction: {instruction}
# """

# # Variables to store data
# instruction = None
# screen_image_path = None
# response_text = None
# pdf_filename = "response.pdf"
# api_key = GEMINI_KEY

# # Test audio on startup
# speak("System started. Enter commands: record, stop, capture, process, open, or exit.")

# # Main loop for processing text input
# while True:
#     try:
#         # Get text input from user
#         command = input("Enter command: ").lower().strip()
#         print(f"Received command: {command}")  # For debugging

#         if command == "exit":
#             speak("Exiting system.")
#             break

#         elif command == "record":
#             speak("Please enter your instruction.")
#             instruction = input("Enter instruction: ").strip()
#             speak("Instruction recorded.")
#             print(f"Instruction: {instruction}")

#         elif command == "stop":
#             instruction = None
#             speak("Recording stopped. Instruction cleared.")
#             print("Instruction cleared.")

#         elif command == "capture":
#             speak("Capturing screen.")
#             screenshot = pyautogui.screenshot()
#             screen_image_path = "screen_capture.png"
#             screenshot.save(screen_image_path)
#             speak("Screen captured.")

#         elif command == "process":
#             if instruction and screen_image_path:
#                 speak("Processing data with LLM.")
                
#                 # Read and base64 encode the image
#                 with open(screen_image_path, "rb") as image_file:
#                     image_data = base64.b64encode(image_file.read()).decode('utf-8')
                
#                 # Format the prompt
#                 formatted_prompt = prompt_template.format(instruction=instruction)
                
#                 # Gemini API endpoint (using gemini-2.5-flash as per your update)
#                 url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
                
#                 # Request payload
#                 payload = {
#                     "contents": [
#                         {
#                             "parts": [
#                                 {"text": formatted_prompt},
#                                 {
#                                     "inline_data": {
#                                         "mime_type": "image/png",
#                                         "data": image_data
#                                     }
#                                 }
#                             ]
#                         }
#                     ]
#                 }
                
#                 # Send request to Gemini API
#                 response = requests.post(url, json=payload)
                
#                 if response.status_code == 200:
#                     # Extract the generated text
#                     response_json = response.json()
#                     try:
#                         response_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
#                         print(f"Gemini API response: {response_text}")  # Debug response
#                         speak("Processing successful. Here is the response.")
#                         speak(response_text)  # Map response to voice
                        
#                         # Generate PDF
#                         pdf = FPDF()
#                         pdf.add_page()
#                         pdf.set_font("Arial", size=12)
#                         pdf.multi_cell(200, 10, txt=response_text)
#                         pdf.output(pdf_filename)
#                         speak("PDF generated.")
#                     except KeyError as ke:
#                         speak("Error extracting response from LLM.")
#                         print(f"Response extraction error: {ke}")
#                         print(f"Full response: {response_json}")
#                 else:
#                     speak("Error processing with LLM.")
#                     print(f"Error: {response.text}")
#             else:
#                 speak("Missing instruction or screen capture. Please record and capture first.")

#         elif command == "open":
#             if os.path.exists(pdf_filename):
#                 speak("Opening PDF in browser.")
#                 webbrowser.open(f"file://{os.path.abspath(pdf_filename)}")
#             else:
#                 speak("No PDF generated yet.")

#         else:
#             speak("Unknown command. Please enter: record, stop, capture, process, open, or exit.")

#     except Exception as e:
#         speak("An error occurred.")
#         print(f"Error: {e}")




# import pyttsx3
# import pyautogui
# import base64
# import requests
# from fpdf import FPDF
# import webbrowser
# import os
# from dotenv import load_dotenv
# import unicodedata

# # Load environment variables
# load_dotenv()

# # Get Gemini API key
# GEMINI_KEY = os.getenv("GEMINI_API_KEY")
# if not GEMINI_KEY:
#     raise ValueError("GEMINI_API_KEY not found in .env file")

# # Initialize text-to-speech engine with configuration
# tts_engine = pyttsx3.init()
# tts_engine.setProperty('rate', 150)  # Adjust speech rate (words per minute)
# tts_engine.setProperty('volume', 0.9)  # Set volume (0.0 to 1.0)

# # Function to speak text, handling long responses
# def speak(text):
#     try:
#         print(f"Attempting to speak: {text[:50]}...")  # Debug first 50 chars
#         max_chunk_length = 500  # Maximum characters per chunk
#         if len(text) > max_chunk_length:
#             chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
#             for chunk in chunks:
#                 tts_engine.say(chunk)
#                 tts_engine.runAndWait()
#         else:
#             tts_engine.say(text)
#             tts_engine.runAndWait()
#         print("Speech completed successfully.")
#     except Exception as e:
#         print(f"Text-to-speech error: {e}")

# # Function to clean text for PDF (replace problematic Unicode characters)
# def clean_text_for_pdf(text):
#     # Normalize Unicode characters to their closest ASCII equivalents
#     text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
#     # Replace specific problematic characters
#     text = text.replace('\u2013', '-')  # Replace en dash with hyphen
#     text = text.replace('\u2014', '-')  # Replace em dash with hyphen
#     text = text.replace('\u2018', "'")  # Replace left single quote
#     text = text.replace('\u2019', "'")  # Replace right single quote
#     text = text.replace('\u201c', '"')  # Replace left double quote
#     text = text.replace('\u201d', '"')  # Replace right double quote
#     return text

# # Prebuilt prompt template
# prompt_template = """
# Process the following instruction on the provided screen capture (which may contain an invoice or relevant content):
# Instruction: {instruction}
# """

# # Variables to store data
# instruction = None
# screen_image_path = None
# response_text = None
# pdf_filename = "response.pdf"
# api_key = GEMINI_KEY

# # Test audio on startup
# speak("System started. Enter commands: record, stop, capture, process, open, or exit.")

# # Main loop for processing text input
# while True:
#     try:
#         # Get text input from user
#         command = input("Enter command: ").lower().strip()
#         print(f"Received command: {command}")  # For debugging

#         if command == "exit":
#             speak("Exiting system.")
#             break

#         elif command == "record":
#             speak("Please enter your instruction.")
#             instruction = input("Enter instruction: ").strip()
#             speak("Instruction recorded.")
#             print(f"Instruction: {instruction}")

#         elif command == "stop":
#             instruction = None
#             speak("Recording stopped. Instruction cleared.")
#             print("Instruction cleared.")

#         elif command == "capture":
#             speak("Capturing screen.")
#             try:
#                 screenshot = pyautogui.screenshot()
#                 screen_image_path = "screen_capture.png"
#                 screenshot.save(screen_image_path)
#                 speak("Screen captured.")
#             except Exception as capture_error:
#                 speak("Error capturing screen.")
#                 print(f"Capture error: {capture_error}")

#         elif command == "process":
#             if instruction and screen_image_path:
#                 speak("Processing data with LLM.")
                
#                 # Read and base64 encode the image
#                 with open(screen_image_path, "rb") as image_file:
#                     image_data = base64.b64encode(image_file.read()).decode('utf-8')
                
#                 # Format the prompt
#                 formatted_prompt = prompt_template.format(instruction=instruction)
                
#                 # Gemini API endpoint (using gemini-2.5-flash)
#                 url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
                
#                 # Request payload
#                 payload = {
#                     "contents": [
#                         {
#                             "parts": [
#                                 {"text": formatted_prompt},
#                                 {
#                                     "inline_data": {
#                                         "mime_type": "image/png",
#                                         "data": image_data
#                                     }
#                                 }
#                             ]
#                         }
#                     ]
#                 }
                
#                 # Send request to Gemini API
#                 response = requests.post(url, json=payload)
                
#                 if response.status_code == 200:
#                     # Extract the generated text
#                     response_json = response.json()
#                     try:
#                         response_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
#                         print(f"Gemini API response: {response_text}")  # Debug response
#                         speak("Processing successful. Here is the response.")
#                         speak(response_text)  # Map response to voice
                        
#                         # Generate PDF with cleaned text
#                         try:
#                             pdf = FPDF()
#                             pdf.add_page()
#                             pdf.set_font("Arial", size=12)
#                             cleaned_text = clean_text_for_pdf(response_text)
#                             pdf.multi_cell(200, 10, txt=cleaned_text)
#                             pdf.output(pdf_filename)
#                             speak("PDF generated.")
#                         except Exception as pdf_error:
#                             speak("Error generating PDF.")
#                             print(f"PDF generation error: {pdf_error}")
#                     except KeyError as ke:
#                         speak("Error extracting response from LLM.")
#                         print(f"Response extraction error: {ke}")
#                         print(f"Full response: {response_json}")
#                 else:
#                     speak("Error processing with LLM.")
#                     print(f"Error: {response.text}")
#             else:
#                 speak("Missing instruction or screen capture. Please record and capture first.")

#         elif command == "open":
#             if os.path.exists(pdf_filename):
#                 speak("Opening PDF in browser.")
#                 webbrowser.open(f"file://{os.path.abspath(pdf_filename)}")
#             else:
#                 speak("No PDF generated yet.")

#         else:
#             speak("Unknown command. Please enter: record, stop, capture, process, open, or exit.")

#     except Exception as e:
#         speak("An error occurred.")
#         print(f"Error: {e}")





# import pyttsx3
# import pyautogui
# import base64
# import requests
# from fpdf import FPDF
# import webbrowser
# import os
# from dotenv import load_dotenv
# import unicodedata
# import re
# import time

# from piper import PiperVoice
# import wave  # For audio playback

# # Load voice model once at startup (outside the loop)
# voice = PiperVoice.load(
#     model_path="./voices/en_US-hfc_female-medium.onnx",
#     config_path="./voices/en_US-hfc_female-medium.onnx.json"
# )
# # Load environment variables
# load_dotenv()

# # Get Gemini API key
# GEMINI_KEY = os.getenv("GEMINI_API_KEY")
# if not GEMINI_KEY:
#     raise ValueError("GEMINI_API_KEY not found in .env file")

# # Function to initialize pyttsx3 engine
# def init_tts_engine():
#     try:
#         engine = pyttsx3.init()
#         engine.setProperty('rate', 150)  # Adjust speech rate
#         engine.setProperty('volume', 0.9)  # Set volume
#         return engine
#     except Exception as e:
#         print(f"Failed to initialize pyttsx3: {e}")
#         return None

# # Function to speak text, reinitializing engine each time
# # def speak(text):
# #     try:
# #         print(f"Attempting to speak: {text[:50]}...")
# #         tts_engine = init_tts_engine()  # Reinitialize engine
# #         if not tts_engine:
# #             print("TTS engine initialization failed.")
# #             return
        
# #         max_chunk_length = 500  # Maximum characters per chunk
# #         cleaned_text = clean_text_for_speech(text)
# #         if len(cleaned_text) > max_chunk_length:
# #             chunks = [cleaned_text[i:i + max_chunk_length] for i in range(0, len(cleaned_text), max_chunk_length)]
# #             for i, chunk in enumerate(chunks):
# #                 print(f"Speaking chunk {i + 1}/{len(chunks)}: {chunk[:50]}...")
# #                 tts_engine.say(chunk)
# #                 tts_engine.runAndWait()
# #                 time.sleep(0.5)  # Small delay between chunks
# #         else:
# #             tts_engine.say(cleaned_text)
# #             tts_engine.runAndWait()
# #         print("Speech completed successfully.")
# #         # Explicitly stop and clean up engine
# #         tts_engine.stop()
# #         del tts_engine
# #     except Exception as e:
# #         print(f"Text-to-speech error: {e}")




# def speak(text):
#     try:
#         print(f"Attempting to speak: {text[:50]}...")
#         cleaned_text = clean_text_for_speech(text)  # Your existing cleaning function
        
#         # Generate WAV bytes
#         wav_bytes = voice.synthesize(cleaned_text)
        
#         # Save to temp WAV and play
#         output_file = "temp_speech.wav"
#         with wave.open(output_file, "wb") as wav_file:
#             wav_file.setnchannels(1)  # Mono
#             wav_file.setsampwidth(2)  # 16-bit
#             wav_file.setframerate(voice.config.sample_rate)  # Use model's sample rate
#             wav_file.writeframes(wav_bytes)
        
#         # Play (Windows example)
#         os.system(f'start {output_file}')  # Opens default media player
        
#         # Cleanup after playback (add delay if needed)
#         import time
#         time.sleep(0.1)  # Brief pause
#         os.remove(output_file)
#         print("Speech completed successfully.")
#     except Exception as e:
#         print(f"Text-to-speech error: {e}")


# # Alternative speak function using gTTS (uncomment to use)
# """
# from gtts import gTTS
# import pygame
# import tempfile

# def speak(text):
#     try:
#         print(f"Attempting to speak: {text[:50]}...")
#         cleaned_text = clean_text_for_speech(text)
#         tts = gTTS(text=cleaned_text, lang='en')
#         temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
#         tts.save(temp_file.name)
#         pygame.mixer.init()
#         pygame.mixer.music.load(temp_file.name)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)
#         pygame.mixer.music.unload()
#         os.unlink(temp_file.name)
#         print("Speech completed successfully.")
#     except Exception as e:
#         print(f"Text-to-speech error: {e}")
# """

# # Function to clean text for speech (remove Markdown and normalize)
# def clean_text_for_speech(text):
#     text = re.sub(r'\*\*+', '', text)  # Remove ** or ****
#     text = re.sub(r'\*+', '', text)    # Remove * or **
#     text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
#     text = text.replace('\u2013', '-')  # En dash
#     text = text.replace('\u2014', '-')  # Em dash
#     text = text.replace('\u2018', "'")  # Left single quote
#     text = text.replace('\u2019', "'")  # Right single quote
#     text = text.replace('\u201c', '"')  # Left double quote
#     text = text.replace('\u201d', '"')  # Right double quote
#     return text.strip()

# # Function to clean text for PDF
# def clean_text_for_pdf(text):
#     text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
#     text = text.replace('\u2013', '-')  # En dash
#     text = text.replace('\u2014', '-')  # Em dash
#     text = text.replace('\u2018', "'")  # Left single quote
#     text = text.replace('\u2019', "'")  # Right single quote
#     text = text.replace('\u201c', '"')  # Left double quote
#     text = text.replace('\u201d', '"')  # Right double quote
#     return text

# # Prebuilt prompt template
# prompt_template = """
# Process the following instruction on the provided screen capture (which may contain an invoice or relevant content):
# Instruction: {instruction}
# """

# # Variables to store data
# instruction = None
# screen_image_path = None
# response_text = None
# pdf_filename = "response.pdf"
# api_key = GEMINI_KEY

# # Test audio on startup
# speak("System started. Enter commands: record, stop, capture, process, open, or exit.")

# # Main loop for processing text input
# while True:
#     try:
#         # Get text input from user
#         command = input("Enter command: ").lower().strip()
#         print(f"Received command: {command}")  # For debugging

#         if command == "exit":
#             speak("Exiting system.")
#             break

#         elif command == "record":
#             speak("Please enter your instruction.")
#             instruction = input("Enter instruction: ").strip()
#             speak("Instruction recorded.")
#             print(f"Instruction: {instruction}")

#         elif command == "stop":
#             instruction = None
#             speak("Recording stopped. Instruction cleared.")
#             print("Instruction cleared.")

#         elif command == "capture":
#             speak("Capturing screen.")
#             try:
#                 screenshot = pyautogui.screenshot()
#                 screen_image_path = "screen_capture.png"
#                 screenshot.save(screen_image_path)
#                 speak("Screen captured.")
#             except Exception as capture_error:
#                 speak("Error capturing screen.")
#                 print(f"Capture error: {capture_error}")

#         elif command == "process":
#             if instruction and screen_image_path:
#                 speak("Processing data with LLM.")
                
#                 # Read and base64 encode the image
#                 with open(screen_image_path, "rb") as image_file:
#                     image_data = base64.b64encode(image_file.read()).decode('utf-8')
                
#                 # Format the prompt
#                 formatted_prompt = prompt_template.format(instruction=instruction)
                
#                 # Gemini API endpoint (using gemini-2.5-flash)
#                 url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
                
#                 # Request payload
#                 payload = {
#                     "contents": [
#                         {
#                             "parts": [
#                                 {"text": formatted_prompt},
#                                 {
#                                     "inline_data": {
#                                         "mime_type": "image/png",
#                                         "data": image_data
#                                     }
#                                 }
#                             ]
#                         }
#                     ]
#                 }
                
#                 # Send request to Gemini API
#                 response = requests.post(url, json=payload)
                
#                 if response.status_code == 200:
#                     # Extract the generated text
#                     response_json = response.json()
#                     try:
#                         response_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
#                         print(f"Gemini API response: {response_text}")  # Debug response
#                         speak("Processing successful. Here is the response.")
#                         time.sleep(1)  # Delay before speaking response
#                         cleaned_response = clean_text_for_speech(response_text)
#                         speak(cleaned_response)  # Map cleaned response to voice
                        
#                         # Generate PDF with cleaned text
#                         try:
#                             pdf = FPDF()
#                             pdf.add_page()
#                             pdf.set_font("Arial", size=12)
#                             cleaned_text = clean_text_for_pdf(response_text)
#                             pdf.multi_cell(200, 10, txt=cleaned_text)
#                             pdf.output(pdf_filename)
#                             speak("PDF generated.")
#                         except Exception as pdf_error:
#                             speak("Error generating PDF.")
#                             print(f"PDF generation error: {pdf_error}")
#                     except KeyError as ke:
#                         speak("Error extracting response from LLM.")
#                         print(f"Response extraction error: {ke}")
#                         print(f"Full response: {response_json}")
#                 else:
#                     speak("Error processing with LLM.")
#                     print(f"Error: {response.text}")
#             else:
#                 speak("Missing instruction or screen capture. Please record and capture first.")

#         elif command == "open":
#             if os.path.exists(pdf_filename):
#                 speak("Opening PDF in browser.")
#                 webbrowser.open(f"file://{os.path.abspath(pdf_filename)}")
#             else:
#                 speak("No PDF generated yet.")

#         else:
#             speak("Unknown command. Please enter: record, stop, capture, process, open, or exit.")

#     except Exception as e:
#         speak("An error occurred.")
#         print(f"Error: {e}")







import pyautogui
import base64
import requests
from fpdf import FPDF
import webbrowser
import os
from dotenv import load_dotenv
import unicodedata
import re
import time
from gtts import gTTS
import pygame

# Load environment variables
load_dotenv()

# Get Gemini API key
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Function to clean text for speech (remove Markdown and normalize)
def clean_text_for_speech(text):
    text = re.sub(r'\*\*+', '', text)  # Remove ** or ****
    text = re.sub(r'\*+', '', text)    # Remove * or **
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.replace('\u2013', '-')  # En dash
    text = text.replace('\u2014', '-')  # Em dash
    text = text.replace('\u2018', "'")  # Left single quote
    text = text.replace('\u2019', "'")  # Right single quote
    text = text.replace('\u201c', '"')  # Left double quote
    text = text.replace('\u201d', '"')  # Right double quote
    return text.strip()

# Function to clean text for PDF
def clean_text_for_pdf(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.replace('\u2013', '-')  # En dash
    text = text.replace('\u2014', '-')  # Em dash
    text = text.replace('\u2018', "'")  # Left single quote
    text = text.replace('\u2019', "'")  # Right single quote
    text = text.replace('\u201c', '"')  # Left double quote
    text = text.replace('\u201d', '"')  # Right double quote
    return text

# Function to speak text using gTTS
def speak(text):
    try:
        print(f"Attempting to speak: {text[:50]}...")
        cleaned_text = clean_text_for_speech(text)
        
        # Generate MP3 with gTTS
        tts = gTTS(text=cleaned_text, lang='en')
        output_file = "speech.mp3"
        tts.save(output_file)
        print(f"MP3 saved to: {os.path.abspath(output_file)}")
        
        # Verify file exists
        if not os.path.exists(output_file):
            raise FileNotFoundError(f"MP3 file not created: {output_file}")
        
        # Play using pygame
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.music.unload()
        
        # Cleanup
        os.remove(output_file)
        print("Speech completed successfully.")
    except Exception as e:
        print(f"Text-to-speech error: {e}")

# Prebuilt prompt template
prompt_template = """
Process the following instruction on the provided screen capture (which may contain an invoice or relevant content):
Instruction: {instruction}
"""

# Variables to store data
instruction = None
screen_image_path = None
response_text = None
pdf_filename = "response.pdf"
api_key = GEMINI_KEY

# Test audio on startup
speak("System started. Enter commands: record, stop, capture, process, open, or exit.")

# Main loop for processing text input
while True:
    try:
        # Get text input from user
        command = input("Enter command: ").lower().strip()
        print(f"Received command: {command}")  # For debugging

        if command == "exit":
            speak("Exiting system.")
            break

        elif command == "record":
            speak("Please enter your instruction.")
            instruction = input("Enter instruction: ").strip()
            speak("Instruction recorded.")
            print(f"Instruction: {instruction}")

        elif command == "stop":
            instruction = None
            speak("Recording stopped. Instruction cleared.")
            print("Instruction cleared.")

        elif command == "capture":
            speak("Capturing screen.")
            try:
                screenshot = pyautogui.screenshot()
                screen_image_path = "screen_capture.png"
                screenshot.save(screen_image_path)
                speak("Screen captured.")
            except Exception as capture_error:
                speak("Error capturing screen.")
                print(f"Capture error: {capture_error}")

        elif command == "process":
            if instruction and screen_image_path:
                speak("Processing data with LLM.")
                
                # Read and base64 encode the image
                with open(screen_image_path, "rb") as image_file:
                    image_data = base64.b64encode(image_file.read()).decode('utf-8')
                
                # Format the prompt
                formatted_prompt = prompt_template.format(instruction=instruction)
                
                # Gemini API endpoint (using gemini-2.5-flash)
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
                
                # Request payload
                payload = {
                    "contents": [
                        {
                            "parts": [
                                {"text": formatted_prompt},
                                {
                                    "inline_data": {
                                        "mime_type": "image/png",
                                        "data": image_data
                                    }
                                }
                            ]
                        }
                    ]
                }
                
                # Send request to Gemini API
                response = requests.post(url, json=payload)
                
                if response.status_code == 200:
                    # Extract the generated text
                    response_json = response.json()
                    try:
                        response_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
                        print(f"Gemini API response: {response_text}")  # Debug response
                        speak("Processing successful. Here is the response.")
                        time.sleep(1)  # Delay before speaking response
                        cleaned_response = clean_text_for_speech(response_text)
                        speak(cleaned_response)  # Map cleaned response to voice
                        
                        # Generate PDF with cleaned text
                        try:
                            pdf = FPDF()
                            pdf.add_page()
                            pdf.set_font("Arial", size=12)
                            cleaned_text = clean_text_for_pdf(response_text)
                            pdf.multi_cell(200, 10, txt=cleaned_text)
                            pdf.output(pdf_filename)
                            speak("PDF generated.")
                        except Exception as pdf_error:
                            speak("Error generating PDF.")
                            print(f"PDF generation error: {pdf_error}")
                    except KeyError as ke:
                        speak("Error extracting response from LLM.")
                        print(f"Response extraction error: {ke}")
                        print(f"Full response: {response_json}")
                else:
                    speak("Error processing with LLM.")
                    print(f"Error: {response.text}")
            else:
                speak("Missing instruction or screen capture. Please record and capture first.")

        elif command == "open":
            if os.path.exists(pdf_filename):
                speak("Opening PDF in browser.")
                webbrowser.open(f"file://{os.path.abspath(pdf_filename)}")
            else:
                speak("No PDF generated yet.")

        else:
            speak("Unknown command. Please enter: record, stop, capture, process, open, or exit.")

    except Exception as e:
        speak("An error occurred.")
        print(f"Error: {e}")