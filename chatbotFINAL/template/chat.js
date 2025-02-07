const ws = new WebSocket("ws://localhost:8010");  // Use the correct port

ws.onopen = () => {
    console.log("Connected to the WebSocket server");
};

ws.onmessage = (event) => {
    const chatbox = document.getElementById("chatbox");
    const message = document.createElement("div");
    message.textContent = event.data;
    chatbox.appendChild(message);
    console.log(message);
};

let username = prompt("Enter your username:");

// Function to send messages
function sendMessage() {
    const input = document.getElementById("message");
    const message = `${username}: ${input.value}`;
    console.log("Sending message:", message); // For debugging purposes
    ws.send(message);
    input.value = "";
}
