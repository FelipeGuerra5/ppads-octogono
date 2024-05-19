export async function POST(req: Request) {
    const body = await req.json()
    try {
        const res = await fetch(`${process.env.IP_API}api/users/login/`,
            {
                method: 'POST',
                body: JSON.stringify(body),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        var response = await res.json()

    } catch (error) {
        console.log('Unable to Login', error)
        response = { error: 'Unable to Login' }
    }
    return new Response(JSON.stringify(response))
}
