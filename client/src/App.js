import React from 'react';
import Cam from "./Cam";


function App() {




  return (
    <>
      <div className='flex flex-col h-screen align-center items-center content-center justify-center text-center bg-slate-600'>
        <p className='text-3xl text-emerald-200'>Object Detection</p>

        <Cam />  
      </div>
    </>
  )

}

export default App;
