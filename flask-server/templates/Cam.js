import React, { useState } from "react";
// This react component file  is used to to render the video image
//  window on the backend at localhost:5000 mainly for testing purposes  
const Cam = () => {
return (
  <div>
    <p> test </p>
   <img
    src="http://localhost:5000/video_feed"
    alt="Video"
   />
  </div>
 );
};
export default Cam;