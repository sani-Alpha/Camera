var captureButton = document.getElementById("capture");
var stopButton = document.getElementById("stop");

stopButton.disabled = true;

captureButton.onclick = function() {
    // var url = window.location.href + "record_status";
    captureButton.disabled = true;
    stopButton.disabled = false;

    // disable download link
    var downloadLink = document.getElementById("download");
    downloadLink.text = "";
    downloadLink.href = "";

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // alert(xhr.responseText);
        }
    }
    xhr.open("POST", "/capture_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "true" }));
};

stopButton.onclick = function() {
    captureButton.disabled = false;
    stopButton.disabled = true;

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // alert(xhr.responseText);

            // enable download link
            var downloadLink = document.getElementById("download");
            downloadLink.text = "Download Image";
            downloadLink.href = "/static/imageD.jpg";
        }
    }
    xhr.open("POST", "/capture_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "false" }));
};
