// Global utility functions for the Smart Recruitment System

// Show loading state on a button
function showLoading(button) {
    if (!button) return;
    
    const spinner = button.querySelector('.spinner-border');
    if (spinner) {
        spinner.classList.remove('d-none');
    }
    button.disabled = true;
    button.innerHTML = button.innerHTML.replace('Analyze', 'Analyzing...');
}

// Hide loading state on a button
function hideLoading(button) {
    if (!button) return;
    
    const spinner = button.querySelector('.spinner-border');
    if (spinner) {
        spinner.classList.add('d-none');
    }
    button.disabled = false;
    button.innerHTML = button.innerHTML.replace('Analyzing...', 'Analyze');
}

// Show alert message
function showAlert(message, type = 'info', container = null) {
    // Remove any existing alerts
    const existingAlerts = document.querySelectorAll('.alert-dismissible');
    existingAlerts.forEach(alert => {
        if (alert.parentNode) {
            alert.remove();
        }
    });
    
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show mt-3`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Insert in the appropriate container
    if (container) {
        container.prepend(alertDiv);
    } else {
        // Try to find a reasonable place to put the alert
        const cardBody = document.querySelector('.card-body');
        if (cardBody) {
            cardBody.prepend(alertDiv);
        } else {
            document.body.prepend(alertDiv);
        }
    }
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

// Format JSON for display
function formatJSON(obj) {
    if (typeof obj === 'string') {
        try {
            obj = JSON.parse(obj);
        } catch (e) {
            return obj;
        }
    }
    return JSON.stringify(obj, null, 2);
}

// Manual Interview Functions
let qaCount = 0;
function addQAPair() {
    qaCount++;
    const qaContainer = document.getElementById('qaContainer');
    if (!qaContainer) return;
    
    const qaDiv = document.createElement('div');
    qaDiv.className = 'qa-pair border p-3 mb-3 rounded';
    qaDiv.innerHTML = `
        <h6>Question ${qaCount}</h6>
        <div class="mb-2">
            <label class="form-label">Question:</label>
            <input type="text" class="form-control" name="questions[]" required 
                   placeholder="Enter the interview question">
        </div>
        <div class="mb-2">
            <label class="form-label">Candidate's Answer:</label>
            <textarea class="form-control" name="answers[]" rows="3" required 
                      placeholder="Enter the candidate's response"></textarea>
        </div>
        <button type="button" class="btn btn-sm btn-outline-danger" onclick="removeQAPair(this)">
            <i class="fas fa-trash"></i> Remove
        </button>
    `;
    qaContainer.appendChild(qaDiv);
}

function removeQAPair(button) {
    if (button && button.parentNode) {
        button.parentNode.remove();
        updateQACount();
    }
}

function updateQACount() {
    const pairs = document.querySelectorAll('.qa-pair');
    pairs.forEach((pair, index) => {
        const header = pair.querySelector('h6');
        if (header) {
            header.textContent = `Question ${index + 1}`;
        }
    });
    qaCount = pairs.length;
}

// Voice Interview Functions
let voiceQuestionCount = 0;
function addVoiceQuestion() {
    voiceQuestionCount++;
    const questionsContainer = document.getElementById('voiceQuestions');
    if (!questionsContainer) return;
    
    const questionDiv = document.createElement('div');
    questionDiv.className = 'voice-question border p-3 mb-3 rounded';
    questionDiv.innerHTML = `
        <h6>Question ${voiceQuestionCount}</h6>
        <div class="mb-2">
            <label class="form-label">Question Text:</label>
            <input type="text" class="form-control" name="questions[]" required 
                   placeholder="What was the interview question?">
        </div>
        <div class="mb-2">
            <label class="form-label">Audio Response:</label>
            <input type="file" class="form-control" name="audio_files" accept="audio/*" required>
            <div class="form-text">Supported formats: WAV, MP3, M4A</div>
        </div>
        <button type="button" class="btn btn-sm btn-outline-danger" onclick="removeVoiceQuestion(this)">
            <i class="fas fa-trash"></i> Remove
        </button>
    `;
    questionsContainer.appendChild(questionDiv);
}

function removeVoiceQuestion(button) {
    if (button && button.parentNode) {
        button.parentNode.remove();
        updateVoiceQuestionCount();
    }
}

function updateVoiceQuestionCount() {
    const questions = document.querySelectorAll('.voice-question');
    questions.forEach((question, index) => {
        const header = question.querySelector('h6');
        if (header) {
            header.textContent = `Question ${index + 1}`;
        }
    });
    voiceQuestionCount = questions.length;
}

// Initialize pages when DOM loads
document.addEventListener('DOMContentLoaded', function() {
    // Initialize manual interview page
    if (document.getElementById('qaContainer') && qaCount === 0) {
        addQAPair();
    }
    
    // Initialize voice interview page
    if (document.getElementById('voiceQuestions') && voiceQuestionCount === 0) {
        addVoiceQuestion();
    }
    
    console.log('Smart Recruitment System initialized');
});