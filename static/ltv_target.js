document.addEventListener("DOMContentLoaded", function () {
    const targetLTVInput = document.getElementById("target_ltv");

    targetLTVInput.addEventListener("input", function () {
        // Get the target LTV value from the input field
        let target_LTV = parseFloat(targetLTVInput.value) / 100;

        if (!isNaN(target_LTV)) {
            fetch("/ltv-target", {
                method: "POST",
                body: JSON.stringify({ 'target_LTV': target_LTV }),
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                // Update the displayed values with the response data
                document.getElementById("target_borrowed").innerText = "£ " + data.target_borrowed.toFixed(2);
                document.getElementById("ltv_adjusted_borrowed").innerText = "£ " + data.ltv_adjusted_borrowed.toFixed(2);                
                document.getElementById("saving_12_months").innerText = "£ " + data.saving_12_months.toFixed(2);
                document.getElementById("saving_24_months").innerText = "£ " + data.saving_24_months.toFixed(2);
                document.getElementById("saving_36_months").innerText = "£ " + data.saving_36_months.toFixed(2);
                document.getElementById("saving_48_months").innerText = "£ " + data.saving_48_months.toFixed(2);
                document.getElementById("saving_60_months").innerText = "£ " + data.saving_60_months.toFixed(2);
            });
        } else {
            // Clear the displayed values if the input is invalid
            document.getElementById("target_borrowed").innerText = "-";
            document.getElementById("ltv_adjusted_borrowed").innerText = "-";
            document.getElementById("saving_12_months").innerText = "-";
            document.getElementById("saving_24_months").innerText = "-";
            document.getElementById("saving_36_months").innerText = "-";
            document.getElementById("saving_48_months").innerText = "-";
            document.getElementById("saving_60_months").innerText = "-";
        }
    });
});