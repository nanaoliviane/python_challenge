// main.js

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide messages after 5 seconds
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.remove();
            }, 500);
        }, 5000);
    });

    // Comment form handling
    const commentForm = document.querySelector('.comment-form');
    if (commentForm) {
        commentForm.addEventListener('submit', function(e) {
            // Optional: Add client-side validation here
            const commentContent = commentForm.querySelector('textarea');
            if (commentContent && commentContent.value.trim() === '') {
                e.preventDefault();
                alert('Please enter a comment before submitting.');
            }
        });
    }

    // Responsive navigation toggle
    const navbarToggler = document.querySelector('.navbar-toggler');
    if (navbarToggler) {
        navbarToggler.addEventListener('click', function() {
            const navbarNav = document.querySelector('#navbarNav');
            navbarNav.classList.toggle('show');
        });
    }

    // Add confirmation for delete actions
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Handle post preview (if implementing a preview feature)
    const previewButton = document.querySelector('#preview-button');
    if (previewButton) {
        previewButton.addEventListener('click', function() {
            const content = document.querySelector('#id_content').value;
            const previewArea = document.querySelector('#preview-area');
            if (previewArea) {
                // You might want to add markdown parsing here
                previewArea.innerHTML = content;
            }
        });
    }
});