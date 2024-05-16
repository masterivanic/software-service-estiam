import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserList() {
    const [users, setUsers] = useState([]);
    const { user } = useAuth();

    useEffect(() => {
        const fetchUsers = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/users/',
                    headers: {
                    'Authorization': `Estiam ${user.access}`
                });
                setUsers(response.data);
            } catch (error) {
                console.error('Erreur lors de la récupération de la liste des utilisateurs :', error);
            }
        };

        fetchUsers();
    }, []);

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
                    <hr />
                ))}
                
            </div>

        </div>
    );
}

export default UserList;

// import React from 'react'

// function UserList() {
//     return (
//         <div className='user-list'>

//             <div className='user-list-main-title'>
//                 <h1>USERS LIST</h1>
//             </div>

//             <div className='user-list-table'>

//                 <div className='u-items'>
//                     <p>Email</p>
//                     <p>Username</p>
//                     <p className='filler'></p>
//                 </div>

//                 <hr />

//             </div>

//         </div>
//     )
// }

// export default UserList
