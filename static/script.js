const API_URL = "http://127.0.0.1:5000"; // Change if your backend URL is different

// Helper for POST requests
async function postData(endpoint, data) {
    const response = await fetch(API_URL + endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    return response.json();
}

// Helper for GET requests
async function getData(endpoint) {
    const response = await fetch(API_URL + endpoint);
    return response.json();
}