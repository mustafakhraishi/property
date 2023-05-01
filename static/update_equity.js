function updateResults() {
  const equityLTV = parseFloat(document.getElementById("equity_LTV").value / 100);
  const remortgagePrice = parseFloat(document.getElementById("new_purchase_price").value);

  if (isNaN(equityLTV) || isNaN(remortgagePrice)) {
      return;
  }

  fetch("/api/update_results", {
      method: "POST",
      body: JSON.stringify({ equity_LTV: equityLTV, remortgage_price: remortgagePrice }),
      headers: {
          "Content-Type": "application/json"
      }
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("equity_release").innerText = "£ " + data.equity_release.toFixed(2);
    document.getElementById("new_cash_invested").innerText = "£ " + data.new_cash_invested.toFixed(2);
    document.getElementById("new_roi").innerText = data.updated_roi.toFixed(2) + " %";    
  });
}