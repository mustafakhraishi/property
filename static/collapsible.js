const collapsibleElements = document.getElementsByClassName('collapsible');

for (let i = 0; i < collapsibleElements.length; i++) {
    collapsibleElements[i].addEventListener('click', function () {
        // Toggle active class on clicked element
        this.classList.toggle('active');

        // Get content of clicked element
        const content = this.nextElementSibling;

        // Toggle max-height of content based on whether it is currently set
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + 'px';
        }
    });
}