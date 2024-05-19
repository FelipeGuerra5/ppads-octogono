type Props = {
    params: {
        login: string | undefined,
        password: string | undefined
    }
}

export default async function validateLogin({ params }: Props): Promise<string> {
    if (params.login == undefined || params.password == undefined) {
        throw new Error("login or password are undefined!");
    }

    try {
        let body = {
            username: params.login,
            password: params.password
        }

        const res = await fetch('/api/login', {
            method: 'POST',
            body: JSON.stringify(body),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!res.ok) {
            throw new Error('Failed to log in');
        }

        const response = await res.json();
        return response.access;  // Assuming response.access is the token you need

    } catch (error) {
        console.error("Unable to LogIn: ", error);
        throw new Error(`Unable to LogIn: ${error}`);
    }
}
