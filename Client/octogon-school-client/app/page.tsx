import Image from "next/image";
import styles from "./page.module.css";
import Login from "./components/Login";

export default function Home() {
  return (
    <main className={styles.container}>
      <div className={styles.loginform}>
        <Login />
      </div>
    </main>
  );
}
