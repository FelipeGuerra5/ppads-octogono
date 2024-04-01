from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Class, Student, AttendanceRecord
from .serializers import ClassSerializer, AttendanceRecordSerializer


class ListStudentsView(APIView):
    def get(self, request, *args, **kwargs):
        period = request.query_params.get('period')
        schoolGrade = request.query_params.get('schoolGrade')

        if not period or not schoolGrade:
            return Response({"error": "period and schoolGrade parameters are required"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            schoolGrade = int(schoolGrade)
        except ValueError:
            return Response({"error": "schoolGrade must be an integer"}, status=status.HTTP_400_BAD_REQUEST)

        classes = Class.objects.filter(period=period, schoolGrade=schoolGrade)

        if not classes.exists():
            return Response([], status=status.HTTP_404_NOT_FOUND)

        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class RecordAttendanceView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"recorded": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
