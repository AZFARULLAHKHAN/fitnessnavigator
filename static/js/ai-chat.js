class AIChat {
    constructor() {
        this.container = null;
        this.messages = [];
        this.currentContext = {};
        this.createChatInterface();
        // ... other initialization code ...
    }

    createChatInterface() {
        // Create chat label above the trigger
        const label = document.createElement('div');
        label.className = 'ai-chat-label';
        label.textContent = 'For any assistance Ask our AI!';
        label.style.position = 'fixed';
        label.style.bottom = '90px';
        label.style.left = '20px';
        label.style.background = '#007bff';
        label.style.color = 'white';
        label.style.padding = '6px 16px';
        label.style.borderRadius = '8px';
        label.style.fontSize = '15px';
        label.style.boxShadow = '0 2px 8px rgba(0,0,0,0.15)';
        label.style.zIndex = '100000';
        label.style.pointerEvents = 'none';
        label.style.userSelect = 'none';
        document.body.appendChild(label);

        // Create chat trigger button
        const trigger = document.createElement('div');
        trigger.className = 'ai-chat-trigger';
        trigger.innerHTML = '🤖';
        document.body.appendChild(trigger);

        // ... rest of the method ...
    }
    // ... rest of the class ...
}

// Initialize AI Chat when the page loads
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => { window.aiChat = new AIChat(); });
} else {
    window.aiChat = new AIChat();
} 