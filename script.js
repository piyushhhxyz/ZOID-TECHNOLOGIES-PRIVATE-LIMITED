const sensorGrid = document.getElementById("sensor-grid");

function updateSensorData(data) {
    sensorGrid.innerHTML = ""; // Clear previous data

    for (const id in data) {
        const item = data[id];
        const card = document.createElement("div");
        card.className = `card ${item.Status === "Active" ? "active" : "inactive"}`;
        card.innerHTML = `
            <h3>ID: ${id}</h3>
            <p>Status: ${item.Status}</p>
            <p>Object Class: ${item.Properties.Class}</p>
            <p>Location: ${item.Properties.Location.join(", ")}</p>
            <p>Detection Time: ${item.Properties.DetectionTime}</p>
        `;

        sensorGrid.appendChild(card);
    }
}

function fetchData() {
    fetch("sensor_output.json") // Adjust the path if necessary
        .then(response => response.json())
        .then(data => updateSensorData(data))
        .catch(error => console.error("Error fetching data:", error));
}

// Fetch data initially and then every 5 seconds
fetchData();
setInterval(fetchData, 5000);
