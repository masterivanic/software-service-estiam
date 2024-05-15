import React from 'react'

function UserList() {
    return (
        <div className='user-list'>

            <div className='user-list-main-title'>
                <h1>USERS LIST</h1>
            </div>

            <div className='user-list-table'>

                <div className='u-items'>
                    <p>Full Name</p>
                    <p>Phone Number</p>
                    <p>Email</p>
                    <p className='filler'></p>
                </div>

                <hr />

                <div className='u-items-sub'>
                    <p>Full Name</p>
                    <p>Phone Number</p>
                    <p>Email</p>
                    <p className='filler'></p>
                </div>

                <hr />


                <div className='u-items-sub'>
                    <p>Full Name</p>
                    <p>Phone Number</p>
                    <p>Email</p>
                    <p className='filler'></p>
                </div>

            </div>

        </div>
    )
}

export default UserList