import React, { useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import axios from 'axios';
import './App.css';
import Home from './Home';

const AUTH_URL = 'https://accounts.spotify.com/authorize';
const REDIRECT_URI = 'http://localhost:3000/callback';
const CLIENT_ID = 'dd4fcb9412ea4f6bab19c5bb8a4021c0';

const Login = () => {
  const handleLogin = () => {
    window.location = `${AUTH_URL}?client_id=${CLIENT_ID}&response_type=code&redirect_uri=${REDIRECT_URI}`;
  };

  return (
    <div className="login-page">
      <h1 className="logo">Spotify</h1>
      <p className="tagline">Get Your Groove On</p>
      <button className="spotify-button" onClick={handleLogin}>Log in with Spotify</button>
    </div>
  );
};

const Callback = () => {
  const handleCallback = async () => {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');
    if (code) {
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
    }
  };

  useEffect(() => {
    handleCallback();
  }, []);

  return <div>Loading...</div>;
};

const App = () => {
  return (
    <Router>
      <div className="app">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/callback" element={<Callback />} />
          <Route path="/home" element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;


