'use client'

import { useState } from "react"
import studentsClass from "@/data/students.json"
import Styles from '@/app/takeattendance/page.module.css'
import recordAttendance from "@/lib/recordStudents"

type Props = {
  params: Students
}

export default function RenderClass({ params }: Props) {
  const [students, setStudents] = useState<Students>(params)

  const handleToggleAttendance = (index: number) => {
    // Create a copy of the students array to modify
    const updatedStudents = [...students.studentsList];
    // Toggle the attendance status of the clicked student
    updatedStudents[index].attending = !updatedStudents[index].attending;
    // Update the state with the modified students array
    setStudents({ ...students, studentsList: updatedStudents });
  };

  return (
    <>
      <section className={Styles.studentsList}>
        {
          students.studentsList.map((student, index) => (
            <div key={student.name} className={Styles.student}>
              <button
                key={index}
                className={student.attending ? Styles.selectStudentActive : Styles.selectStudentNotActive}
                onClick={() => {
                  handleToggleAttendance(index)
                }
                }
              >{student.name}</button>
            </div>
          ))
        }
      </section>
      <div>
        <button
          className={Styles.finisheAttendance}
          onClick={() => {
            recordAttendance({ params: students })
            console.log(students)
            alert(`Chamada concluida para Matéria: ${params.classMeta} no Período: ${params.period}`)
          }}
        >
          Finalizar Chamada
        </button>
      </div>
    </>
  )
}


