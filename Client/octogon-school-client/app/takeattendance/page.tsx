// import Image from "next/images";
import Styles from '@/app/takeattendance/page.module.css'
import getStudents from '@/lib/getStudents'
import { NextResponse } from 'next/server'


const fetchStudents = async () => {
  try {
    const studentsData: Promise<Students> = await getStudents({ params: {period: "afternoon", schoolGrade: 6}})
    console.log(studentsData)
    return studentsData
  } catch (error) {
    console.log("Error Fetching Students: ", error)
  }
}

export default async function Home() {
  
  const params = { period: "afternoon", schoolGrade: 6 }
  const students: Students = await getStudents({ params });
  console.log(students.studentsList)
  students.studentsList.map(student => (console.log(student.name)))
  
  const page = ( 
    <main className={Styles.main}>
      <section className={Styles.attendanceInfo}>
        <div className={Styles.information}>Info</div>
        <div className={Styles.information}>Time</div>
        <div className={Styles.information}>Class</div>
      </section>
      <div className={Styles.studentsListContainer}>
        <section className={Styles.studentsList}>
          {
            students.studentsList.map((student) => (
              <>
                <div key={student.name} className={Styles.student}>
                <button className={Styles.selectStudent}>{student.name}</button>
                </div>
              </>
            ))
          }
        </section>
      </div>
    </main>
  )

  return page
}


