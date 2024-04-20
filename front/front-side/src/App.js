import './App.css';
import { Routes, Route } from 'react-router-dom';
import SideMenu from './components/SideMenu';
import HomePage from './pages/Vitrine';
import Form from './pages/Form';
import UserList from './pages/UserList';

function App() {
  return (
    <div className="App">
      <SideMenu />
      <div className='container'>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/form" element={<Form />} />
          <Route path="/users" element={<UserList />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
