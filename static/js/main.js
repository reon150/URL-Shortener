function start() {
    window.addEventListener("load", start, true);
}

function ajax() {
    var url = document.getElementById("url").value;
    if (url === '') {
        alert('URL field is empty')
    } else {
        // Set up our HTTP request
        var xhr = new XMLHttpRequest();
    
        // Setup our listener to process completed requests
        xhr.onload = function () {
    
            // Process our return data
            if (xhr.status >= 200 && xhr.status < 300) {
                // The request is successful
                document.getElementById('shortenedDiv').style.visibility = "visible"
                document.getElementById('url-shortened').href = this.response;
                document.getElementById('url-shortened').innerHTML = this.response;
            } else {
                // Request failed
                console.log('The request failed!');
            }
    
        };
    
        // Create and send a POST request
        xhr.open('POST', 'http://localhost:5000/getShortURL');
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send(`url=${url}`);
    }
}

function load() { 
    var button = document.getElementById('buttonForm');
    button.addEventListener('click', ajax, false); 
} 

document.addEventListener("DOMContentLoaded", load, false);
