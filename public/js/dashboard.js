// Initial data
let tokenBalance = 1000;
let usageDetails = [
    { week: "2024-10-01", minutes: 150 },
    { week: "2024-10-08", minutes: 175 },
    { week: "2024-10-15", minutes: 120 },
    { week: "2024-10-22", minutes: 200 },
];

// Update UI
function updateUI() {
    document.getElementById("token-balance").textContent = `${tokenBalance} Zen`;

    // Populate usage details table
    const usageTable = document.getElementById("usage-details");
    usageTable.innerHTML = ""; // Clear table first
    usageDetails.forEach(detail => {
        const row = document.createElement("tr");
        row.classList.add("bg-gray-100", "text-gray-700", "hover:bg-gray-200");

        row.innerHTML = `
            <td class="p-4">${detail.week}</td>
            <td class="p-4">${detail.minutes} min</td>
        `;
        usageTable.appendChild(row);
    });
}

// Event listeners for card clicks with animations
document.getElementById("leaderboard-card").addEventListener("click", () => {
    alert("Navigating to the Leaderboard!");
    // Additional actions like navigation can be added here
});

document.getElementById("marketplace-card").addEventListener("click", () => {
    alert("Navigating to the Marketplace!");
    // Additional actions like navigation can be added here
});

document.getElementById("profile-card").addEventListener("click", () => {
    alert("Navigating to Profile!");
    // Additional actions like navigation can be added here
});

// Animate token balance update on page load
function animateTokenBalance() {
    let count = 0;
    const interval = setInterval(() => {
        count += 50;
        document.getElementById("token-balance").textContent = `${count} Zen`;
        if (count >= tokenBalance) {
            clearInterval(interval);
            document.getElementById("token-balance").textContent = `${tokenBalance} Zen`;
        }
    }, 50);
}

// Initialize page content
document.addEventListener("DOMContentLoaded", () => {
    updateUI();
    animateTokenBalance();
});