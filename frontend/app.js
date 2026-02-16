async function downloadVideo() {
    const url = document.getElementById("url").value;
    const result = document.getElementById("result");

    result.innerHTML = "Processing...";

    const response = await fetch("http://localhost:5000/api/download", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({url})
    });

    const data = await response.json();

    if (data.video) {
        result.innerHTML = `<a href="${data.video}" download>Click here to Download</a>`;
    } else {
        result.innerHTML = "Error: " + data.error;
    }
}
