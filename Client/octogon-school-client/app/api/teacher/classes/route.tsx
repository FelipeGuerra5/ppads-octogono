import { NextResponse } from "next/server"
import Classes from '@/lib/Classes.json'

export async function GET() {
    // try {

    //     const token = window.localStorage.getItem("accessToken")

    //     const res = await fetch(`${process.env.IP_API}api/users/login/`,
    //         {
    //             method: 'GET',
    //             headers: {
    //                 'Content-Type': 'application/json',
    //                 'Authorization': `Bearer ${token}`
    //             }
    //         })
    //     var response = await res.json()
    //     console.log(response)
    // } catch (error) {
    //     console.log('Unable Get Classes', error)
    //     response = { error: 'Unable to Get Classes' }
    // }

    // return NextResponse.json(response)
    // Development Only
    const classes: Classes = Classes
    return NextResponse.json(classes)
}

