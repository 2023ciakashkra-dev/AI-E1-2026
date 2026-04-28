import React, { useState } from "react";



export default function QueueDashboard() {
  const [currentToken, setCurrentToken] = useState(18);
  const [yourToken, setYourToken] = useState(null);
  const [queue, setQueue] = useState([19, 20, 21, 22, 23]);

  const takeToken = () => {
    const newToken = queue.length > 0 ? queue[queue.length - 1] + 1 : currentToken + 1;
    setQueue([...queue, newToken]);
    setYourToken(newToken);
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Stationery Queue Management</h1>

      <div style={styles.cardContainer}>
        <div style={styles.card}>
          <h2>Now Serving</h2>
          <p style={styles.bigText}>{currentToken}</p>
        </div>

        <div style={styles.card}>
          <h2>Your Token</h2>
          <p style={styles.bigText}>{yourToken ? yourToken : "--"}</p>
        </div>

        <div style={styles.card}>
          <h2>People Ahead</h2>
          <p style={styles.bigText}>
            {yourToken ? queue.indexOf(yourToken) : 0}
          </p>
        </div>
      </div>

      <button style={styles.button} onClick={takeToken}>
        Take Token
      </button>

      <div style={styles.queueBox}>
        <h2>Queue List</h2>
        {queue.map((token) => (
          <div key={token} style={styles.queueItem}>
            <span>Token {token}</span>
            <span>Waiting</span>
          </div>
        ))}
      </div>
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    background: "linear-gradient(to right, #c2e9fb, #a1c4fd)",
    padding: "20px",
    fontFamily: "Arial, sans-serif",
    textAlign: "center",
  },
  heading: {
    marginBottom: "20px",
  },
  cardContainer: {
    display: "flex",
    justifyContent: "center",
    gap: "20px",
    flexWrap: "wrap",
  },
  card: {
    background: "white",
    padding: "20px",
    borderRadius: "15px",
    width: "200px",
    boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
  },
  bigText: {
    fontSize: "28px",
    fontWeight: "bold",
  },
  button: {
    marginTop: "30px",
    padding: "12px 25px",
    fontSize: "16px",
    borderRadius: "10px",
    border: "none",
    backgroundColor: "#4CAF50",
    color: "white",
    cursor: "pointer",
  },
  queueBox: {
    marginTop: "40px",
    background: "white",
    padding: "20px",
    borderRadius: "15px",
    maxWidth: "500px",
    marginInline: "auto",
    boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
  },
  queueItem: {
    display: "flex",
    justifyContent: "space-between",
    padding: "10px",
    marginTop: "10px",
    borderRadius: "10px",
    background: "#f1f1f1",
  },
};