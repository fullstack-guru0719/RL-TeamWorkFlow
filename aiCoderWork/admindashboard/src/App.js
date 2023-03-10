import Topbar from './components/topbar/Topbar';
import './app.css';
import Home from './pages/home/Home';
import Sidebar from './components/sidebar/Sidebar';
import {
  BrowserRouter as Router,
  Route,
  Routes,
} from "react-router-dom"
import UserList from './pages/userList/UserList';
function App() {
  return (
    <Router>
      <Topbar />
      <div className="container">
        <Sidebar />
        <Routes>
          <Route exact path='/'>
            <Home />
          </Route>
          <Route path='/users'>
            <UserList />
          </Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
