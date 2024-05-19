type Props = {
    params: Teacher
}

export default async function getClasses({ params }: Props) {
    const res = await fetch('/api/teacher/classes')
    const classes: Classes = await res.json()
    return classes
}