from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Class, Student
from .models import AttendanceRecord
from .serializers import ClassAttendanceSerializer


class ClassAttendanceView(APIView):
    def post(self, request):
        serializer = ClassAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Attendance records created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttendanceRecordView(APIView):
    def get(self, request):
        # Capturando os parâmetros da query
        period = request.query_params.get('period', None)
        schoolGrade = request.query_params.get('schoolGrade', None)
        classMeta = request.query_params.get('classMeta', None)
        teacher_id = request.query_params.get('teacher', None)
        date = request.query_params.get('date', None)

        # Construindo os filtros com base nos parâmetros fornecidos
        filters = {}
        if period:
            filters['period'] = period
        if schoolGrade:
            filters['schoolGrade'] = schoolGrade
        if classMeta:
            filters['classMeta'] = classMeta
        if teacher_id:
            filters['teacher_id'] = teacher_id

        # Encontrando a classe específica (assumindo que ela é única)
        class_instance = get_object_or_404(Class, **filters)

        # Filtrando registros de presença por data e classe
        attendance_records = AttendanceRecord.objects.filter(classMeta=class_instance, date=date)

        # Preparando a lista de estudantes para a resposta
        students_list = [
            {
                "student": attendance_record.student.name,
                "attending": attendance_record.attending
            } for attendance_record in attendance_records
        ]

        # Preparando os dados da resposta
        response_data = {
            "period": class_instance.period,
            "schoolGrade": class_instance.schoolGrade,
            "classMeta": class_instance.classMeta,
            "teacher": class_instance.teacher.id,
            "date": date,
            "studentsList": students_list
        }

        return Response(response_data)
