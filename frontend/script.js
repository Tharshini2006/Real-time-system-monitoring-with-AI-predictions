const API_URL = "http://127.0.0.1:8000/status";

const labels = [];
const cpuData = [];
const ramData = [];
const diskData = [];
const predictedCpuData = [];

// Chart setup
const ctx = document.getElementById("usageChart").getContext("2d");
const usageChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: labels,
        datasets: [
            { label: "CPU Usage", data: cpuData, borderColor: "red", fill: false },
            { label: "RAM Usage", data: ramData, borderColor: "green", fill: false },
            { label: "Disk Usage", data: diskData, borderColor: "orange", fill: false },
            { label: "Predicted CPU", data: predictedCpuData, borderColor: "blue", borderDash: [5,5], fill: false }
        ]
    },
    options: {
        responsive: true,
        animation: false,
        scales: {
            y: { beginAtZero: true, max: 100 }
        }
    }
});

async function fetchSystemStatus() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        // Update text
        document.getElementById("cpu").innerText = `CPU: ${data.cpu_usage}%`;
        document.getElementById("ram").innerText = `RAM: ${data.ram_usage}%`;
        document.getElementById("disk").innerText = `Disk: ${data.disk_usage}%`;
        document.getElementById("predicted").innerText =
            `Predicted CPU: ${data.predicted_cpu_usage}%`;

        // Alert system
        const alertBox = document.getElementById("alert");
        if (data.cpu_usage > 80) {
            alertBox.innerText = "⚠️ ALERT: CPU usage is very high!";
            alertBox.style.color = "red";
        } else {
            alertBox.innerText = "✅ System running normally";
            alertBox.style.color = "green";
        }

        // Add data to graph
        const time = new Date().toLocaleTimeString();
        labels.push(time);
        cpuData.push(data.cpu_usage);
        ramData.push(data.ram_usage);
        diskData.push(data.disk_usage);
        predictedCpuData.push(data.predicted_cpu_usage);

        // Keep only last 10 points
        if (labels.length > 10) {
            labels.shift();
            cpuData.shift();
            ramData.shift();
            diskData.shift();
            predictedCpuData.shift();
        }

        usageChart.update();

    } catch (error) {
        console.error("Error fetching system status:", error);
    }
}

setInterval(fetchSystemStatus, 3000);
fetchSystemStatus();
