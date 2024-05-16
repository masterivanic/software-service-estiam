import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from '../AuthContext';

function HomePage() {
    const [userData, setUserData] = useState(null);
    const { user } = useAuth();
    console.log(user);
    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const response = await axios.get('http://localhost:8030/api/auth/me/', {
                    headers: {
                        'Authorization': `Estiam ${user.access}`
                    }
                });
                setUserData(response.data);
            } catch (error) {
                console.error('Erreur lors de la récupération des données utilisateur :', error);
            }
        };

        fetchUserData();
    }, []);

    return (
        <>
            <div className='home'>
                {userData ? (
                    <>
                        <h1>Welcome, {userData.username}!</h1>
                        <p>Email: {userData.email}</p>
                    </>
                ) : (
                    <p>Loading...</p>
                )}
            </div>
        </>
    );
}

export default HomePage;
