Pizza Rechner
-----------------

<div style="background: #f9f9f9; padding: 20px; border-radius: 8px; border: 1px solid #ddd;">
  <label>Anzahl Pizzen:</label><br>
  <input type="number" id="npizza" value="4" style="width: 100%; margin-bottom: 10px;">
  
  <label>Gewicht pro Pizza [g]:</label><br>
  <input type="number" id="w_pizza" value="280" style="width: 100%; margin-bottom: 10px;">
 
  <label>Hydration [%]:</label><br>
  <input type="number" id="hydration" value="70" style="width: 100%; margin-bottom: 10px;">
  
  <label>Anteil Vorteig [%]:</label><br>
  <input type="number" id="starter_fraction" value="20" style="width: 100%; margin-bottom: 10px;">
  

  <button onclick="runMath()" style="padding: 10px 20px; cursor: pointer;">Berechnen</button>

  <hr>
  <p><strong>Result:</strong> <span id="w_flour_total">---</span></p>
</div>

**Zutaten gesamt**
<strong>Mehl:</strong> <span id="w_flour_total">0</span>

**Zutaten Vorteig**
<strong>Mehl:</strong> <span id="w_flour_starter">---</span>

**Zutaten Hauptteig**
<strong>Mehl:</strong> <span id="w_flour_main">---</span>


**Zubereitung**
1. dies
2. das

<script>
function runMath() {
  // 1. Grab values from the inputs
  const n = parseFloat(document.getElementById('npizza').value);
  const w = parseFloat(document.getElementById('w_pizza').value);
  const h = parseFloat(document.getElementById('hydration').value);
  const f = parseFloat(document.getElementById('starter_fraction').value);

  // Total numbers
  const w_total = n*w*1.1
  const w_flour_total = w_total/(1+h/100)
  const w_water_total = w_flour_total*h/100
  const w_starter = w_total * f/100
  const w_sour = 0.2 * w_starter
  const w_flour_starter = 0.4 * w_starter
  const w_water_starter = 0.4 * w_starter
  const w_flour_main = w_flour_total - (0.5 * weight_starter)
  const w_water_main = w_water_total - (0.5 * weight_starter)

  // Collect results
  document.getElementById('w_flour_starter').innerText = w_flour_starter.toFixed(2);
  document.getElementById('w_flour_main').innerText = w_flour_main.toFixed(2);
  document.getElementById('w_flour_total').innerText = w_flour_total.toFixed(2);

}
</script>



[🏠 Home](./../)