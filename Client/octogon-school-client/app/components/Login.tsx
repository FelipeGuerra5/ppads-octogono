"use client"

import styles from '@/app/page.module.css'
import validateLogin from '@/lib/validateLogin'
import { useState } from 'react'


export default function Login() {
    const [login, setLogin] = useState<string>()
    const [password, setPassword] = useState<string>()

    return (
        <>
            <div className={styles.login}>
                <input type="text" placeholder={login} id="login" value={login} onChange={(e) => { setLogin((e.target.value)) }} />
                <label htmlFor="login" >Insira o seu Usuário</label>
            </div>
            <div className={styles.password}>
                <input type="password" placeholder={password} id="Password" value={password} onChange={(e) => { setPassword((e.target.value)) }} />
                <label htmlFor="Password" >Insira o sua Senha</label>
            </div>
            <button
                type="button"
                className={styles.submitButton}
                onClick={() => {
                    validateLogin({ params: { login, password } })
                }}
            >login</button>
        </>
    )
}