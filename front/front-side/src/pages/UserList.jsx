import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from '../AuthContext'; 

function UserList() {
    const [users, setUsers] = useState([]);
    const { user } = useAuth();

    useEffect(() => {
        const fetchUsers = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/users/', {
                    headers: {
                        'Authorization': `Estiam ${user.access}`
                    }
                });

                if (response.status === 200) {
                    setUsers(response.data);
                } else {
                    console.error('Erreur lors de la récupération de la liste des utilisateurs. Statut:', response.status);
                }
            } catch (error) {
                console.error('Erreur lors de la récupération de la liste des utilisateurs :', error);
            }
        };

        fetchUsers();
    }, [user.access]); // Ajoutez user.access comme dépendance pour recharger la liste des utilisateurs lorsque l'utilisateur change

    return (
        <div className='user-list'>
            <div className='user-list-main-title'>
                <h1>USERS LIST</h1>
            </div>

            <div className='user-list-table'>
                {users.map(user => (
                    <div key={user.id} className='u-items'>
                        <p>{user.email}</p>
                        <p>{user.username}</p>
                        <p className='filler'></p>
                    </div>
                ))}
                <hr />
            </div>
        </div>
    );
}

export default UserList;
