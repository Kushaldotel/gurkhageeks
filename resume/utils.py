from dotenv import load_dotenv

load_dotenv()
import base64
import io
import os

import google.generativeai as genai
import pdf2image

genai.configure(api_key=os.getenv("GeminiAPIKey"))


def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text


def input_pdf(pdffile):
    if pdffile is not None:
        image = pdf2image.convert_from_bytes(pdffile.read())  # convert pdf to image
        first_page = image[0]

        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode(),  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
