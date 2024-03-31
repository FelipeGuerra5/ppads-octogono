from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Class, Student, AttendanceRecord
from .serializers import ClassSerializer, AttendanceRecordSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Class
from .serializers import ClassSerializer


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

        class_instance = classes.first()

        data = {
            "period": class_instance.period,
            "schoolGrade": class_instance.schoolGrade,
            "classMeta": class_instance.classMeta,
            "teacher": class_instance.teacher.id,
            "studentsList": []
        }

        for cls in classes:
            class_serializer = ClassSerializer(cls)
            if cls == class_instance:
                data['studentsList'] = class_serializer.data['studentsList']
            else:
                data['studentsList'].extend(class_serializer.data['studentsList'])

        return Response(data)


class RecordAttendanceView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"recorded": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
