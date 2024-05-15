import React from 'react';
import { useAuth } from '../AuthContext';

const Form = () => {
  const { login } = useAuth();

  const handleLogin = () => {
    login();
  };
    return (
        <div className='formular'>

                <form className='form form-register'>
                    <h1>Register</h1>

                    <input type='text' placeholder='Full Name'/>
                    <input type='text' placeholder='Username'/>
                    <input type='text' placeholder='E-mail'/>
                    <input type='number' placeholder='Phone Number'/>
                    <input type='password'  placeholder='Password'/>
                    <input type='password'  placeholder='Confirm Password'/>

                    <button type='submit' className='btn-register'>Register</button>
                </form>

                <form className='form form-connection'>
                    <h1>Login</h1>

                    <input className="input-connection" type='text'placeholder='Username' />
                    <input className="input-connection" type='password' placeholder='Password'/>

                    <button type='submit' className='btn-connection' onClick={handleLogin}>Login </button>
                </form>

        </div>

    )
}

export default Form