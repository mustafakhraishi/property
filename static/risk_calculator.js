document.addEventListener('DOMContentLoaded', function() {
  const interestRateInput = document.getElementById("interest_rate");
  const ltvInput = document.getElementById("ltv");

  interestRateInput.addEventListener("input", updateRiskCalculator);
  ltvInput.addEventListener("input", updateRiskCalculator);

  function updateRiskCalculator() {
    const riskInterestRate = parseFloat(interestRateInput.value) / 100;
    const riskLTV = parseFloat(ltvInput.value / 100);

    if (isNaN(riskInterestRate) || isNaN(riskLTV)) {
      return;
    }

    fetch("/risk-calculator", {
      method: "POST",
      body: JSON.stringify({ risk_interest_rate: riskInterestRate, risk_LTV: riskLTV }),
      headers: {
        "Content-Type": "application/json"
      }
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById("new_borrowed").innerText = "£ " + data.new_borrowed.toFixed(2);
      document.getElementById("adjusted_borrowed").innerText = "£ " + data.adjusted_borrowed.toFixed(2);
      document.getElementById("annual_mortgage_payment").innerText = "£ " + data.annual_mortgage_payment.toFixed(2);
      document.getElementById("mortgage_payment").innerText = "£ " + data.monthly_mortgage_payment.toFixed(2);
      document.getElementById("monthly_cashflow").innerText = "£ " + data.monthly_cashflow.toFixed(2);
    });
  }
});