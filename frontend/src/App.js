import logo from './logo.svg';
import './App.css';
import FrontTest from './Component/test';
import HomePage from './Component/Homepage';
import {Routes, Route, Link} from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <nav className='topNav'>
        <Link to={'/'} element={<FrontTest/>}>Test</Link>
        <Link to={'/signup'} element={<FrontTest/>}>Signup</Link>
      </nav>
      <Routes>
      <Route path='/' element={<FrontTest/>}/>
      <Route path='/signup' element={<HomePage/>}/>
      </Routes>
    </div>
  );
}

export default App;
