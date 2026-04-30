import React from "react";

export default function Dashboard({ user, setUser }) {
  const handleLogout = () => {
    localStorage.removeItem("userProfile");
    setUser(null);
  };

  return (
    <div>
      <h2>Welcome, {user.name}!</h2>
      <p>Email: {user.email}</p>
      <p>Age: {user.age}</p>
      <p>Gender: {user.gender}</p>

      <h3>Next Steps</h3>
      <button>Record Cough</button>
      <button>Fill Symptoms</button>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}
