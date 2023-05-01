function updateMaxSpend() {
    const monthlyRentInput = document.querySelector('#gross_annual_rent');
    const desiredGrossYieldInput = document.querySelector('#desired_gross_yield');
    const maxSpendOutput = document.querySelector('#maximum_spend');

    if (!monthlyRentInput.value || !desiredGrossYieldInput.value) {
        return;
    }

    const annualRent = parseFloat(monthlyRentInput.value) * 12;
    const desiredGrossYield = parseFloat(desiredGrossYieldInput.value);

    const formData = new FormData();
    formData.append('monthly_rent', annualRent);
    formData.append('desired_gross_yield', desiredGrossYield);

    fetch('/max-spend-calculator', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        maxSpendOutput.textContent = "£ " + parseFloat(data.max_spend).toFixed(2);
    });
}

document.querySelector('#gross_annual_rent').addEventListener('input', updateMaxSpend);
document.querySelector('#desired_gross_yield').addEventListener('input', updateMaxSpend);