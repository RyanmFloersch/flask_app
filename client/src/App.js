import React, {useState, useEffect} from 'react';

function App() {
  const [data, setData] = useState([{}])

  // Fetching json data and logging it
  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data);
      }
    )
  }, [])

  // If the data isn't fetched yet it displays loading while the promise hasn't resolved
  // When it has resolved it then prints out all the members on the page. 
  // return (
  //   <div>
  //     {(typeof data.members === 'undefined') ? (
  //       <p>Loading...</p>
  //     ) : (
  //       data.members.map((member, i) => (
  //         <p key={i}>{member}</p>
  //       ))
  //     )}
  //   </div>
  // );

return(
  <div className='container'>
    <div className='row'>
      <h3 className='mt-5'>Live Streaming</h3>
      <img src="{{url_for('video_feed')}}" width="100%" alt="video feed" />
    </div>
  </div>
)

}

export default App;
