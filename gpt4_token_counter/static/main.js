//static/main.js

document.addEventListener("DOMContentLoaded", (event) => {
  const form = document.getElementById("token-count-form");
  const queryInput = document.getElementById("query");
  const tokenCountElement = document.getElementById("token-count");
  const predictButton = document.getElementById("predict-button");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const query = queryInput.value;

    fetch("http://localhost:5000/count", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: query }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        tokenCountElement.textContent = `Token count: ${data.token_count}`;
      })
      .catch((error) => {
        console.error("Error:", error);
        tokenCountElement.textContent = "Error: Unable to count tokens";
      });
    predictButton.addEventListener("click", (event) => {
      event.preventDefault();
      predictTokens();
    });
  });
  function predictTokens() {
    const text = queryInput.value;
    const model = "cl100k_base";
    fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: text, model: model }),
    })
      .then((response) => response.json())
      .then((data) => {
        tokenCountElement.textContent = `Predicted token count: ${data.token_count}`;
      })
      .catch((error) => {
        console.error("Error:", error);
        tokenCountElement.textContent = "Error predicting token count";
      });
  }
});
