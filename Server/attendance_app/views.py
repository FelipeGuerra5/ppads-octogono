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
        # Construindo o filtro com base nos parâmetros opcionais
        period = request.query_params.get('period')
        schoolGrade = request.query_params.get('schoolGrade')
        classMeta = request.query_params.get('classMeta')
        teacher_id = request.query_params.get('teacher')
        date = request.query_params.get('date')

        # Encontrando as classes específicas com os filtros aplicados
        class_instance = get_object_or_404(Class,
                                           period=period,
                                           schoolGrade=schoolGrade,
                                           classMeta=classMeta,
                                           teacher_id=teacher_id)

        # Filtrando registros de presença por data e classe
        attendance_records = AttendanceRecord.objects.filter(classMeta=class_instance, date=date)
        student_ids = attendance_records.values_list('student', flat=True)
        students = Student.objects.filter(id__in=student_ids)

        # Preparando a lista de estudantes para a resposta
        students_list = [{
            "student": attendance_record.student.id,
            "attending": attendance_record.attending
        } for attendance_record in attendance_records]

        # Preparando os dados da resposta
        response_data = {
            "period": period,
            "schoolGrade": schoolGrade,
            "classMeta": classMeta,
            "teacher": teacher_id,
            "date": date,
            "studentsList": students_list
        }

        return Response(response_data, status.HTTP_201_CREATED)
