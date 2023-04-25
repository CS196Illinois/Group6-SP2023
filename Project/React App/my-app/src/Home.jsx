import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const [accessToken, setAccessToken] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (token) {
      setAccessToken(token);
    } else {
      navigate('/');
    }
  }, [navigate]);

  return (
    <div className="home-page">
      <h1 className="welcome">Welcome to Spotify</h1>
      <p className="access-token">Your access token is: {accessToken}</p>
    </div>
  );
};

export default Home;
