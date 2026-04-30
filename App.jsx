import React, { useState, useEffect } from "react";
import LoginScreen from "./screens/LoginScreen.jsx";
import Dashboard from "./screens/Dashboard.jsx";

export default function App() {
  const [user, setUser] = useState(null);

  // Check if user profile exists in localStorage
  useEffect(() => {
    const storedUser = localStorage.getItem("userProfile");
    if (storedUser) setUser(JSON.parse(storedUser));
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      {!user && <LoginScreen setUser={setUser} />}
      {user && <Dashboard user={user} setUser={setUser} />}
    </div>
  );
}
