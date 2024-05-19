'use client'

import getClasses from "@/lib/getClasses"
import Styles from '@/app/home/[teacher]/[teacherId]/page.module.css'
import Link from "next/link"

export default async function Home({ params }: { params: Teacher }) {

    const { teacher, teacherId } = params
    const classes: Classes = await getClasses({ params })

    return (
        <main className={Styles.content} >
            {
                classes.classes.map((i) => (
                    <Link
                        className={Styles.block}
                        href={`./${teacherId}/${i.Grade}`}
                    >

                        <div>
                            Clase: {i.class}
                        </div>
                        <div>
                            Sala: {i.Room}
                        </div>
                    </Link>
                ))
            }
        </main>
    )
}
