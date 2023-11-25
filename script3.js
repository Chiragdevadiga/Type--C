// script.js

function searchVideos() {
    // Get the title entered by the user
    const title = document.getElementById("title").value;

    // Use a video platform API to search for videos based on the title
    // For example, using YouTube Data API
    const apiKey = 'AIzaSyBZEO2RaoBgVKW_wJtYsvuP9EblzSVf_5k';
    const apiUrl = `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${title}&type=video&key=${apiKey}`;

    // Make an API request
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            
              // Log the API response
                // ... rest of your code
           
            
            // Extract video IDs from the API response
            const videoIds = data.items.map(item => item.id.videoId);

            // Update the video container with iframes for each video
            const videoContainer = document.getElementById("video-container");
            videoContainer.innerHTML = ''; // Clear existing videos

            videoIds.forEach(videoId => {
                const iframe = document.createElement("iframe");
                iframe.src = `https://www.youtube.com/embed/${videoId}`;
                iframe.frameBorder = "0";
                iframe.allowFullscreen = true;

                videoContainer.appendChild(iframe);
            });
        })
        .catch(error => {
            console.error('Error fetching videos:', error);
        });
}
