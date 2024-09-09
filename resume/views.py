from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import ResumeFeedbackSerializer
from .utils import get_gemini_response, input_pdf


class ResumeFeedbackViewSet(ModelViewSet):
    serializer_class = ResumeFeedbackSerializer
    parser_classes = [
        MultiPartParser
    ]  # Use `parser_classes` instead of `pagination_class`

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ResumeFeedbackSerializer(data=data)
        if serializer.is_valid():
            job_description = serializer.validated_data["job_description"]
            resume = serializer.validated_data["resume"]
            task = serializer.validated_data["task"]

            input_prompt1 = """
            You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description.
            Please share your professional evaluation on whether the candidate's profile aligns with the role.
            Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
            """
            input_prompt2 = """
            You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality,
            your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
            the job description. First the output should come as percentage and then keywords missing and last final thoughts.
            """

            input_prompt = input_prompt1 if task == "review" else input_prompt2

            try:
                # Convert PDF to text
                pdf_content = input_pdf(resume)
                response = get_gemini_response(
                    job_description, pdf_content, input_prompt
                )
                return Response({"response": response})
            except PDFInfoNotInstalledError as e:
                return Response(
                    {
                        "error": "Poppler is not installed or not found. Please install it to proceed.",
                        "details": str(e),
                    },
                    status=500,
                )
            except (PDFPageCountError, PDFSyntaxError) as e:
                return Response(
                    {
                        "error": "There was an issue with processing the PDF file.",
                        "details": str(e),
                    },
                    status=400,
                )
            except Exception as e:
                return Response(
                    {"error": "An unexpected error occurred.", "details": str(e)},
                    status=500,
                )

        return Response(serializer.errors, status=400)
