async function sendMessage() {
    let userInput = document.getElementById("userInput");
    let userMessage = userInput.value.trim();
    if (!userMessage) return;

    let messagesDiv = document.getElementById("messages");

    // Display user message
    // Display user message with icon
    let userMsgDiv = document.createElement("div");
    userMsgDiv.className = "message-container user-message";

    // Create user icon
    let userIcon = document.createElement("img");
    userIcon.src = "static/images/person.png";
    userIcon.alt = "User Icon";
    userIcon.className = "user-icon";

    // Create text container
    let userTextDiv = document.createElement("div");
    userTextDiv.className = "message user";
    userTextDiv.textContent = userMessage;

    // Append icon and text
    userMsgDiv.appendChild(userTextDiv);
    userMsgDiv.appendChild(userIcon);
    messagesDiv.appendChild(userMsgDiv);


    userInput.value = ""; // Clear input

    try {
        // Send message to Flask backend
        let response = await fetch("http://localhost:5001/send_message", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage }),
        });

        let data = await response.json();

        // Handle bot response
        let botReply = data.bot_response || (data.map ? data.map(item => item.text).join(" ") : "No response from bot");

        // Display bot response
        // Display bot message with icon
        let botMsgDiv = document.createElement("div");
        botMsgDiv.className = "message-container bot-message";

        // Create bot icon
        let botIcon = document.createElement("img");
        botIcon.src = "static/images/bot.png";
        botIcon.alt = "Bot Icon";
        botIcon.className = "bot-icon";

        // Create text container
        let botTextDiv = document.createElement("div");
        botTextDiv.className = "message bot";
        botTextDiv.innerHTML = botReply;

        // Append icon and text
        botMsgDiv.appendChild(botIcon);
        botMsgDiv.appendChild(botTextDiv);
        messagesDiv.appendChild(botMsgDiv);


      

        // Auto-scroll to latest message
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    } catch (error) {
        console.error("Error fetching bot response:", error);
        
        // Display error message
        let errorMsgDiv = document.createElement("div");
        errorMsgDiv.className = "message bot error";
        errorMsgDiv.textContent = "Error communicating with the bot.";
        messagesDiv.appendChild(errorMsgDiv);
    }
}

// Allow sending messages using Enter key
document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});