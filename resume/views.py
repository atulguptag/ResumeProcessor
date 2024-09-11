import os
from .models import Candidate
from rest_framework import status
from pyresparser import ResumeParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CandidateSerializer

# Create your views here.

class ExtractResumeView(APIView):
    def post(self, request, *args, **kwargs):
        # Get the uploaded resume file from the request
        file = request.FILES['resume']

        # Define the path where the file will be saved
        file_path = os.path.join('uploads', file.name)

        # Save the uploaded file to the specified path
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Use pyresparser to extract data from the resume
        data = ResumeParser(file_path).get_extracted_data()

        # Create a new Candidate instance with the extracted data
        candidate = Candidate(
            first_name=data.get('name', ''),
            email=data.get('email', ''),
            mobile_number=data.get('mobile_number', '')
        )

        # Save the Candidate instance to the database
        candidate.save()

        # Serialize the Candidate instance to JSON format
        serializer = CandidateSerializer(candidate)

        # Return the serialized data as a JSON response with a 201 status code
        return Response(serializer.data, status=status.HTTP_201_CREATED)