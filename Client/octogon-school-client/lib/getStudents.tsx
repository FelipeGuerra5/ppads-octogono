type Props = {
    params: {
        period: string,
        schoolGrade: number
    }
}

export default async function getStudents({ params }: Props) {
    const res = await fetch('http://localhost:3000/api/students');
    const students = await res.json();
    return students
}