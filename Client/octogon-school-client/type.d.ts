type Student = {
    "name": string,
    "attending": boolean
}

type Students = {
    "period": string,
    "schoolGrade": number,
    "class": string,
    "teacher": string,
    "attendance" : number,
    "studentsList": [
        {
            "name": string,
            "attending": boolean
        }
    ]
}

type ClassRoom = {
    "period": string,
    "schoolGrade": number,
    "class": string,
    "teacher": string,
    "attendance" : number,
    "recorded" : boolean
    "studentsList": [
        {
            "name": string,
            "attending": true
        }
    ]
}