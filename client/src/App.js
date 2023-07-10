import React from 'react';
import Cam from "./components/Cam";


function App() {




  return (
    <div className='flex h-screen justify-center align-center items-center    bg-slate-800'>
      <div className='flex flex-col w-1/2 h-full  align-center items-center justify-evenly text-center bg-slate-600'>
        <p className='text-3xl text-emerald-200 '>Object Detection</p>
        
        <Cam />  
      </div>
    </div>
  )

}

export default App;
