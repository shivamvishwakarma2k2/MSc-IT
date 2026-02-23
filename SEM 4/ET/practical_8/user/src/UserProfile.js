import React, { useState, useEffect } from "react";
import axios from "axios";
import "./UserProfile.css"; // Import CSS

const UserProfile = () => {
  const [user, setUser] = useState(null);
  const [isFollowing, setIsFollowing] = useState(false);
  const [darkMode, setDarkMode] = useState(false);

  // Fetch a random user from API
  useEffect(() => {
    axios
      .get("https://randomuser.me/api/")
      .then((response) => {
        setUser(response.data.results[0]);
      })
      .catch((error) => {
        console.error("Error fetching user:", error);
      });
  }, []);

  if (!user) {
    return <p className="loading">Loading user...</p>;
  }

  return (
    <div className={`profile-card ${darkMode ? "dark" : "light"}`}>
      <button
        className="theme-toggle"
        onClick={() => setDarkMode(!darkMode)}
      >
        {darkMode ? "Light Mode" : "Dark Mode"}
      </button>

      <img
        src={user.picture.large}
        alt="Profile"
        className="profile-img"
      />

      <h2 className="name">
        {user.name.first} {user.name.last}
      </h2>

      <p className="email">{user.email}</p>

      <p className="city">
        {user.location.city}, {user.location.country}
      </p>

      <button
        className={`btn ${isFollowing ? "unfollow" : "follow"}`}
        onClick={() => setIsFollowing(!isFollowing)}
      >
        {isFollowing ? "Unfollow" : "Follow"}
      </button>
    </div>
  );
};

export default UserProfile;