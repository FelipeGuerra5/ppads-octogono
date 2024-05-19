type Student = {
    "name": string,
    "id": number,
    "attending": boolean
}

type Students = {
    "period": string,
    "schoolGrade": number,
    "classMeta": string,
    "teacher": number,
    // "attendance": number,
    "date": string,
    "studentsList": {
        "name": string,
        "id": number,
        "attending": boolean
    }[]

}

type ClassRoom = {
    "period": string,
    "schoolGrade": number,
    "classMeta": string,
    "teacher": number,
    // "attendance": number,
    "recorded": boolean,
    "date": string,
    "studentsList": {
        "name": string,
        "id": number,
        "attending": true
    }[]
}

type Teacher = {
    teacher: string,
    teacherId: string,
}

type Classes = {
    "teacher": string,
    "teacherId": number,
    "classes": {
        "class": string
        "room": string
        "grade": string
        "period": string
    }[];
}