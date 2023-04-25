import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const AUTH_URL = 'https://accounts.spotify.com/authorize';
const REDIRECT_URI = 'http://localhost:3000/callback';
const CLIENT_ID = 'dd4fcb9412ea4f6bab19c5bb8a4021c0';

const Home = () => {
  const [savedSongs, setSavedSongs] = useState([]);

  useEffect(() => {
    const accessToken = localStorage.getItem('access_token');
    if (accessToken) {
      axios.get('https://api.spotify.com/v1/me/tracks', {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      })
        .then((response) => {
          setSavedSongs(response.data.items);
        })
        .catch((error) => {
          console.error(error);
        });
    } else {
      window.location = `${AUTH_URL}?client_id=${CLIENT_ID}&response_type=code&redirect_uri=${REDIRECT_URI}`;
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    window.location.reload();
  };

  return (
    <div className="home-page">
      <h1 className="logo">Spotify</h1>
      <button className="logout-button" onClick={handleLogout}>Log out</button>
      <h2 className="page-title">Your Saved Songs</h2>
      <ul className="song-list">
        {savedSongs.map((song) => (
          <li className="song" key={song.track.id}>
            <img className="song-image" src={song.track.album.images[0].url} alt={song.track.name} />
            <div className="song-details">
              <h3 className="song-name">{song.track.name}</h3>
              <p className="song-artist">{song.track.artists.map((artist) => artist.name).join(', ')}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
