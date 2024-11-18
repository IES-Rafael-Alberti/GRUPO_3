import { useEffect, useState } from "react";
import styles from "./Home.module.css";

type Data = {
  message: string;
};

export default function Home() {
  const [data, setData] = useState<Data | null>(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch("/api/hello");
        const result: Data = await response.json();
        setData(result);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }
    fetchData();
  }, []);

  return (
    <div className={styles.container}>
      <p className={styles.message}>{data ? data.message : "Loading..."}</p>
    </div>
  );
}
