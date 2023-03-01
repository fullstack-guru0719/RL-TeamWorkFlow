import Topbar from './components/topbar/Topbar';
import './app.css';
import Home from './pages/home/Home';
import Sidebar from './components/sidebar/Sidebar';
function App() {
  return (
    <div>
      <Topbar />
      <div className="container">
        <Sidebar />
        <Home />
      </div>
    </div>
  );
}

export default App;