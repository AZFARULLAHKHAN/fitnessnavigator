class AIChat {
    constructor() {
        console.log('Initializing AI Chat...');
        this.container = null;
        this.messages = [];
        this.currentContext = {};
        try {
            this.init();
            console.log('AI Chat initialized successfully');
        } catch (error) {
            console.error('Error in AI Chat initialization:', error);
        }
    }

    init() {
        console.log('Creating chat interface...');
        this.createChatInterface();
        this.bindEvents();
        this.gatherPageContext();
        // Send initial greeting through server
        this.processMessage('hi');
        // Force show the chat interface after a short delay
        setTimeout(() => {
            const trigger = document.querySelector('.ai-chat-trigger');
            if (trigger) {
                console.log('Chat trigger found, making visible');
                trigger.style.display = 'flex';
            } else {
                console.log('Chat trigger not found');
            }
        }, 1000);
        console.log('Chat interface ready!');
    }

    createChatInterface() {
        // Create chat trigger button
        const trigger = document.createElement('div');
        trigger.className = 'ai-chat-trigger';
        trigger.innerHTML = '🤖';
        document.body.appendChild(trigger);

        // Create chat container
        const container = document.createElement('div');
        container.className = 'ai-chat-container';
        container.innerHTML = `
            <div class="ai-chat-header">
                <h3>AI Fitness Assistant</h3>
                <button class="ai-chat-close">×</button>
            </div>
            <div class="ai-chat-messages"></div>
            <div class="ai-chat-input">
                <input type="text" placeholder="Ask me anything about your fitness plan...">
                <button>Send</button>
            </div>
        `;
        document.body.appendChild(container);
        this.container = container;
    }

    bindEvents() {
        // Toggle chat window
        const trigger = document.querySelector('.ai-chat-trigger');
        console.log('Chat trigger element:', trigger);
        
        trigger.addEventListener('click', (e) => {
            console.log('Chat trigger clicked');
            e.preventDefault();
            e.stopPropagation();
            this.container.classList.add('active');
            console.log('Added active class:', this.container.classList.contains('active'));
        });

        // Close chat window
        const closeBtn = this.container.querySelector('.ai-chat-close');
        closeBtn.addEventListener('click', (e) => {
            console.log('Close button clicked');
            e.preventDefault();
            e.stopPropagation();
            this.container.classList.remove('active');
        });

        // Send message
        const input = this.container.querySelector('input');
        const sendBtn = this.container.querySelector('button');
        
        const sendMessage = () => {
            const message = input.value.trim();
            if (message) {
                this.addMessage('user', message);
                this.processMessage(message);
                input.value = '';
            }
        };

        sendBtn.addEventListener('click', sendMessage);
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }

    gatherPageContext() {
        // Gather user data
        const userDataElements = document.querySelectorAll('.list-group-item');
        const userData = {};
        userDataElements.forEach(elem => {
            const label = elem.textContent.split('\n')[0].trim();
            const value = elem.querySelector('.badge')?.textContent.trim();
            if (value) {
                userData[label] = value;
            }
        });

        // Gather workout plan
        const workoutPlan = {};
        document.querySelectorAll('.accordion-item').forEach(item => {
            const day = item.querySelector('.accordion-button').textContent.split('-')[0].trim();
            const focus = item.querySelector('.accordion-button').textContent.split('-')[1].trim();
            const exercises = Array.from(item.querySelectorAll('.list-group-item')).map(ex => {
                return ex.textContent.trim();
            });
            workoutPlan[day] = { focus, exercises };
        });

        this.currentContext = { userData, workoutPlan };
    }

    async processMessage(message) {
        const loadingId = this.addMessage('loading', 'Thinking...');
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: `Context: ${JSON.stringify(this.currentContext)}\n\nUser Question: ${message}`
                })
            });

            if (!response.ok) {
                throw new Error(`API request failed with status ${response.status}`);
            }

            const data = await response.json();
            if (data.error) {
                throw new Error(data.error);
            }
            if (!data.response) {
                throw new Error('Invalid response format from AI');
            }

            const aiResponse = data.response;
            this.removeMessage(loadingId);
            this.addMessage('ai', aiResponse);
        } catch (error) {
            console.error('Error:', error);
            this.removeMessage(loadingId);
            let errorMessage = 'Sorry, I encountered an error. Please try again.';
            if (error.message.includes('401')) {
                errorMessage = 'API key error. Please check your Gemini API key configuration.';
            } else if (error.message.includes('429')) {
                errorMessage = 'Too many requests. Please try again in a moment.';
            }
            this.addMessage('ai', errorMessage);
        }
    }

    addMessage(type, content) {
        const messagesContainer = this.container.querySelector('.ai-chat-messages');
        const messageDiv = document.createElement('div');
        const messageId = `msg-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
        messageDiv.id = messageId;
        messageDiv.className = `ai-chat-message ${type}`;
        
        if (type === 'loading') {
            messageDiv.innerHTML = `${content}<span class="loading-dots"></span>`;
        } else {
            messageDiv.textContent = content;
        }
        
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        return messageId;
    }

    removeMessage(messageId) {
        const message = document.getElementById(messageId);
        if (message) {
            message.remove();
        }
    }
}

// Initialize AI Chat when the page loads
document.addEventListener('DOMContentLoaded', () => {
    try {
        console.log('DOM Content Loaded - Initializing chat...');
        window.aiChat = new AIChat();
        console.log('Chat initialization complete');
    } catch (error) {
        console.error('Error initializing chat:', error);
    }
});
