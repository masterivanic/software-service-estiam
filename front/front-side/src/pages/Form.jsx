import React, { useState } from 'react';
import axios from 'axios';
import { useAuth } from '../AuthContext';
import { useNavigate } from 'react-router-dom';

const Form = () => {
  const { login } = useAuth();
  const navigate = useNavigate();

  const [registerData, setRegisterData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
  });
  const [registerMessage, setRegisterMessage] = useState('');

  const [loginData, setLoginData] = useState({
    username: '',
    password: '',
  });
  const [loginMessage, setLoginMessage] = useState('');

  const handleRegisterChange = (e) => {
    const { name, value } = e.target;
    setRegisterData({ ...registerData, [name]: value });
  };

  const handleLoginChange = (e) => {
    const { name, value } = e.target;
    setLoginData({ ...loginData, [name]: value });
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    if (registerData.password !== registerData.confirmPassword) {
      setRegisterMessage("Passwords do not match");
      return;
    }

    try {
      const response = await axios.post('http://localhost:8030/api/auth/register/', {
        email: registerData.email,
        username: registerData.username,
        password: registerData.password,
        password2: registerData.confirmPassword,
      });
      setRegisterMessage(response.data.message);
      navigate('/home'); 
    } catch (error) {
      setRegisterMessage(error.response.data.detail || 'Registration failed');
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8030/api/auth/login/', {
        username: loginData.username,
        password: loginData.password,
      });
      login(response.data);
      navigate('/home'); 
    } catch (error) {
      setLoginMessage(error.response.data.detail || 'Login failed');
    }
  };

  return (
    <div className='formular'>
      <form className='form form-register' onSubmit={handleRegister}>
        <h1>Register</h1>
        <input
          type='text'
          placeholder='Username'
          name='username'
          value={registerData.username}
          onChange={handleRegisterChange}
        />
        <input
          type='email'
          placeholder='E-mail'
          name='email'
          value={registerData.email}
          onChange={handleRegisterChange}
        />
        <input
          type='password'
          placeholder='Password'
          name='password'
          value={registerData.password}
          onChange={handleRegisterChange}
        />
        <input
          type='password'
          placeholder='Confirm Password'
          name='confirmPassword'
          value={registerData.confirmPassword}
          onChange={handleRegisterChange}
        />
        <button type='submit' className='btn-register'>Register</button>
        {registerMessage && <p>{registerMessage}</p>}
      </form>

      <form className='form form-connection' onSubmit={handleLogin}>
        <h1>Login</h1>
        <input
          className="input-connection"
          type='text'
          placeholder='Username'
          name='username'
          value={loginData.username}
          onChange={handleLoginChange}
        />
        <input
          className="input-connection"
          type='password'
          placeholder='Password'
          name='password'
          value={loginData.password}
          onChange={handleLoginChange}
        />
        <button type='submit' className='btn-connection'>Login</button>
        {loginMessage && <p>{loginMessage}</p>}
      </form>
    </div>
  );
};

export default Form;
