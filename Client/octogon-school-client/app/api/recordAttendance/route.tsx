export async function POST(req: Request) {
    const body = await req.json()
    try {
        const res = await fetch(`${process.env.IP_API}api/register-attendance/`,
            {
                method: 'POST',
                body: JSON.stringify(body),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        var response = await res.json()

    } catch (error) {
        console.log('Unable to Record Attendance', error)
    }
    return new Response('OK')
}
