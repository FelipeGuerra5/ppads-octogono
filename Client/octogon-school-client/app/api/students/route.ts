import { NextResponse } from 'next/server'
import Data from '@/data/students.json'

// Will be needed when we inset actual classes in a DB
type Props = {
    params: {
        "period": string,
        "schoolGrade": number
    }
}

export function GET() {
        return NextResponse.json(Data)
}