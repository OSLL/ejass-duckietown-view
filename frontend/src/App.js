import './App.css';
import Iframe from 'react-iframe'

function App() {
  return (
    <div className="App">
      <Iframe url="http://autobotglazunov.local/dashboard/robot"
              width="100%"
              height={window.innerHeight}
              id="myId"
              className="myClassname"
              display="initial"
              position="relative"/>
    </div>
  );
}

export default App;
