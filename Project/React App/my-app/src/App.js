import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import Home from './Home';

const AUTH_URL = 'https://accounts.spotify.com/authorize';
const REDIRECT_URI = 'http://localhost:3000/home';
const CLIENT_ID = 'dd4fcb9412ea4f6bab19c5bb8a4021c0';

const Login = () => {
  const [code, setCode] = useState('');
  const [loggedIn, setLoggedIn] = useState(false);

  const handleLogin = () => {
    window.location = `${AUTH_URL}?client_id=${CLIENT_ID}&response_type=code&redirect_uri=${REDIRECT_URI}`;
    setLoggedIn(true)
  };

  const handleCallback = async () => {
    const { data } = await axios.post('https://accounts.spotify.com/api/token', {
      grant_type: 'authorization_code',
      code,
      redirect_uri: REDIRECT_URI,
      client_id: CLIENT_ID,
      client_secret: '6b50f4087c3c4d9da1728499e497a540',
    });
  
    // Store the access token in local storage
    localStorage.setItem('access_token', data.access_token);
  
    // Redirect the user to the home page
    window.location.href = '/home';
   
  };

  return (
    <div className="login-page">
      <h1 className="logo">Spotify</h1>
      <p className="tagline">Get Your Groove On</p>
      <div className="form">
        <h2 className="form-title">Log in to your account</h2>
        <input className="form-input" type="text" value={code} onChange={(e) => setCode(e.target.value)} placeholder="Enter your authorization code" />
        <button className="form-button" onClick={handleCallback}>Submit code</button>
      </div>
      <button className="spotify-button" onClick={handleLogin}>Log in with Spotify</button>
    </div>
  );
};

export default Login;
