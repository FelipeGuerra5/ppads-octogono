import { NextResponse } from 'next/server'
import Data from '@/data/students.json'

// Will be needed when we inset actual classes in a DB
type Props = {
    params: {
        "period": string,
        "schoolGrade": number
    }
}

export async function GET() {
    const res = await fetch(`${process.env.IP_API}api/view-attendance/?period=Vespertino&schoolGrade=6&classMeta=Português&teacher=1&date=2024-03-31`);
    const students = await res.json();
    return NextResponse.json(students)
}