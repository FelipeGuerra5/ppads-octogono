export async function POST(req: Request) {
    const body = await req.json()
    try {
        const res = await fetch(`${process.env.IP_API}api/users/login/`,
            {
                method: 'POST',
                body: JSON.stringify(body),
                headers: {
                    'Content-Type': 'application/json',
                    'User-Agent': 'insomnia/9.1.1',
                    'Cookie': 'csrftoken=8VBsOWTtj91h1l7CXrHJfnDyvLR9hc6adbPMsc5fy5BxaACwCoi4F9kkREzTTHNA; sessionid=64vgi8rvt0m7e1ncs6j1jar0hyt4xgco'
                }
            })
        var response = await res.json()

    } catch (error) {
        console.log('Unable to Login', error)
        response = { error: 'Unable to Login' }
    }
    return new Response(JSON.stringify(response), {
        headers: {
            'Content-Type': 'application/json'
        }
    })
}
