import './App.css';
import { Routes, Route, Navigate, useLocation } from 'react-router-dom';
import SideMenu from './components/SideMenu';
import HomePage from './pages/Vitrine';
import Form from './pages/Form';
import UserList from './pages/UserList';
import { AuthProvider, useAuth } from './AuthContext';

function App() {
  return (
    <AuthProvider>
      <div className="App">
          <Content />
      </div>
    </AuthProvider>
  );
}

const Content = () => {
  const { isAuthenticated } = useAuth();
  const location = useLocation();

  return (
    <>
      {location.pathname !== "/" && <SideMenu />}
      <div className='container'>
        <Routes>
          <Route path="/" element={<Form />} />
          <Route path="/home" element={ <HomePage />}></Route>
          <Route path="/users" element={ <UserList />}></Route>
        </Routes>
      </div>
    </>
  );
}

export default App;
