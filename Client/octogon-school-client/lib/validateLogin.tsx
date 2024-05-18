type Props = {
    params: {
        login: string | undefined,
        password: string | undefined
    }
}

export default async function validateLogin({ params }: Props) {
    if (params.login == undefined || params.password == undefined) {
        window.alert("login or password are undefined!")
    }
    try {
        const res = await fetch('http://localhost:3000/api/login',
            {
                method: 'POST',
                body: JSON.stringify(params),
                headers: {
                    'Content-Type': 'Application/json'
                }
            })
        var response = await res.json()
        window.alert(response)

    } catch (error) {
        console.log("Unable to LogIn: ", error)
        window.alert(`Unable to LogIn: ${error}`)
    }
}