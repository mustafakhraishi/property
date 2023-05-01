document.addEventListener('DOMContentLoaded', () => {
    // Get form and fieldsets
    const form = document.querySelector('form');
    const fieldsets = form.querySelectorAll('fieldset');

    // Get progress bar and milestones
    const progressBar = document.getElementById('progress-bar');
    const milestones = document.querySelectorAll('.milestone');

    // Add event listeners to input fields
    fieldsets.forEach((fieldset) => {
        const inputs = fieldset.querySelectorAll('input');
        inputs.forEach((input) => {
            input.addEventListener('input', () => {
                updateProgressBar();
            });
        });
    });

    // Update progress bar based on completed fieldsets
    function updateProgressBar() {
        let completedFieldsets = 0;

        fieldsets.forEach((fieldset) => {
            const inputs = fieldset.querySelectorAll('input');
            let allInputsFilled = true;

            inputs.forEach((input) => {
                if (input.value === '') {
                    allInputsFilled = false;
                }
            });

            if (allInputsFilled) {
                completedFieldsets++;
            }
        });

        const progressValue = (completedFieldsets / fieldsets.length) * 100;
        progressBar.value = progressValue;
    }

    // Scroll to milestone when clicked
    milestones.forEach((milestone) => {
        milestone.addEventListener('click', () => {
            const milestoneValue = parseInt(milestone.getAttribute('data-value'));
            const fieldsetIndex = Math.floor(milestoneValue / 25) - 1;
            const targetFieldset = fieldsets[fieldsetIndex];

            targetFieldset.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });
});
