import UCarousel from '././Components/Carousel';
import TNavbar from '././Components/Navbar';
import NewComplaint from './Components/NewComplaint';
import ComplaintStatus from './Components/ComplaintStatus';
import { Button } from 'react-bootstrap';
import { useState } from 'react';
import './App.css';

function App() {
  const [NCmountState, setNCMountState]= useState(false);
  const [CSmountState, setCSMountState]= useState(false);
 function setNCState(){
    setCSMountState(false);
    setNCMountState(!NCmountState);
  };
  function setCSState(){
    setNCMountState(false);
    setCSMountState(!CSmountState);
  }
  return (
    <div className="App">
      <TNavbar />
      <UCarousel />
      <div className="cbutton">
      <Button onClick={setNCState}>New Complaint</Button>
      <Button onClick={setCSState}>Complaint Status</Button>
      </div>
      
      <div style={{display: NCmountState ? null: "none"}} className="mount NewComplaint">
        <NewComplaint />
      </div>
      <div style={{display: CSmountState ? null: "none"}} className="mount ComplaintStatus">
        <ComplaintStatus />
      </div>
    </div>
  );
}

export default App;
