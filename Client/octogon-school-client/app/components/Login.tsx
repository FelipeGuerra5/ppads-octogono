"use client"

import styles from '@/app/page.module.css'
import validateLogin from '@/lib/validateLogin'
import { useRouter } from 'next/navigation'
import { useState } from 'react'

export default function Login() {
    const [login, setLogin] = useState<string>('')
    const [password, setPassword] = useState<string>('')

    const router = useRouter()

    const handleLogin = async () => {
        try {
            const token = await validateLogin({ params: { login, password } });
            if (token) {
                localStorage.setItem('accessToken', token);
                window.alert('Login successful!');
                router.push(`/home/fernanda/1`) //Must Return from API 
            } else {
                window.alert("Usuário não Registrado\n Entre em contato com a Administração")
            }
        } catch (error) {
            window.alert(`handleLogin Error: ${error}`);
        }
    }

    return (
        <form action="#" className={styles.loginform}>
            Login
            <div className={styles.login}>
                <input
                    className={styles.input}
                    type="text"
                    placeholder="Usuário"
                    id="login"
                    value={login}
                    onChange={(e) => setLogin(e.target.value)}
                />
            </div>
            <div className={styles.password}>
                <input
                    className={styles.input}
                    type="password"
                    placeholder="Senha"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            <button
                type="button"
                className={styles.submitButton}
                onClick={handleLogin}
            >
                Login
            </button>
        </form>
    )
}
