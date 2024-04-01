import styles from '@/app/page.module.css'
import Link from 'next/link'
import Image from 'next/image'

export default function NavBar() {
    return (
        <nav className={styles.navbar}>
            <div className={styles.navbaroptions}>
                <Link
                    href='/'
                    className={styles.navbarhome}
                >
                    Octogono
                </Link>
            </div>
            <div className={styles.navbarprofile}>
                <Image
                    className={styles.navbarpic}
                    src="/images/profilepicnavbar.svg"
                    width={50}
                    height={50}
                    alt="Felipe Guerra"
                    title="UserProfile"
                    priority={true}
                />
            </div>
        </nav>
    )
}