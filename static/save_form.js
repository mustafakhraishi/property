function saveFormDataToLocalStorage() {
  const formData = {
    purchase_price: document.getElementById("purchase_price").value,
    renovation: document.getElementById("renovation").value,
    legal_fees: document.getElementById("legal_fees").value,
    furnishing: document.getElementById("furnishing").value,
    mortgage_fees: document.getElementById("mortgage_fees").value,
    monthly_rent: document.getElementById("monthly_rent").value,
    LTV: document.getElementById("LTV").value,
    interest_rate: document.getElementById("interest_rate").value,
    management_rate: document.getElementById("management_rate").value,
    repairs: document.getElementById("repairs").value,
    void_weeks: document.getElementById("void_weeks").value,
    service_charge: document.getElementById("service_charge").value,
    ground_rent: document.getElementById("ground_rent").value,
    insurance: document.getElementById("insurance").value,
    bills: document.getElementById("bills").value,
    other_expenses: document.getElementById("other_expenses").value,
  };
  
  localStorage.setItem("propertyFormData", JSON.stringify(formData));
}  

function loadFormDataFromLocalStorage() {
  const storedFormData = localStorage.getItem("propertyFormData");
  
  if (storedFormData) {
    const formData = JSON.parse(storedFormData);
  
    document.getElementById("purchase_price").value = formData.purchase_price;
    document.getElementById("renovation").value = formData.renovation;
    document.getElementById("legal_fees").value = formData.legal_fees;
    document.getElementById("furnishing").value = formData.furnishing;
    document.getElementById("mortgage_fees").value = formData.mortgage_fees;
    document.getElementById("monthly_rent").value = formData.monthly_rent;
    document.getElementById("LTV").value = formData.LTV;
    document.getElementById("interest_rate").value = formData.interest_rate;
    document.getElementById("management_rate").value = formData.management_rate;
    document.getElementById("repairs").value = formData.repairs;
    document.getElementById("void_weeks").value = formData.void_weeks;
    document.getElementById("service_charge").value = formData.service_charge;
    document.getElementById("ground_rent").value = formData.ground_rent;
    document.getElementById("insurance").value = formData.insurance;
    document.getElementById("bills").value = formData.bills;
    document.getElementById("other_expenses").value = formData.other_expenses;
  }
}

document.addEventListener("DOMContentLoaded", loadFormDataFromLocalStorage);

// Clear form data when the page is refreshed
if (performance.navigation.type === 1) {
  localStorage.removeItem("propertyFormData");
}

// Save form data to localStorage when the user leaves the page
window.addEventListener("beforeunload", saveFormDataToLocalStorage);

// Clear form data when the page is restored from cache
window.addEventListener("pageshow", function(event) {
  if (event.persisted) {
    localStorage.removeItem("propertyFormData");
  }
});