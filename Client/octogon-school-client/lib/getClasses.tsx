type Props = {
    params: Teacher
}

export default async function getClasses({ params }: Props) {
    const res = await fetch('/api/teacher/classes')
    const classes = await res.json()
    return classes
}