Pizza Rechner
-----------------

<div style="background: #f9f9f9; padding: 20px; border-radius: 8px; border: 1px solid #ddd;">
  <h4>Universal Calculator</h4>
  
  <label>Anzahl Pizzen:</label><br>
  <input type="number" id="npizza" value="4" style="width: 100%; margin-bottom: 10px;">
  
  <label>Gewicht pro Pizza [g]:</label><br>
  <input type="number" id="w_pizza" value="280" style="width: 100%; margin-bottom: 10px;">
 
  <label>Hydration [%]:</label><br>
  <input type="number" id="hydration" value="70" style="width: 100%; margin-bottom: 10px;">
  
  <label>Sauerteiganteil in Starter [%]:</label><br>
  <input type="number" id="sour_fraction" value="20" style="width: 100%; margin-bottom: 10px;">
  

  <button onclick="runMath()" style="padding: 10px 20px; cursor: pointer;">Calculate Result</button>

  <hr>
  <p><strong>Result:</strong> <span id="finalResult">---</span></p>
</div>

<script>
function runMath() {
  // 1. Grab values from the inputs
  const a = parseFloat(document.getElementById('npizza').value);
  const b = parseFloat(document.getElementById('w_pizza').value);
  const c = parseFloat(document.getElementById('hydration').value);
  const d = parseFloat(document.getElementById('sour_fraction').value);

  // 2. Define your "Complicated Formula"
  // Example: Result = ( (A + B) * C ) / A
  const result = ((a + b) * c) / a;

  // 3. Output the result back to the page
  document.getElementById('finalResult').innerText = result.toFixed(2);
}
</script>


[🏠 Home](./../)