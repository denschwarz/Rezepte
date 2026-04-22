Pizzarechner für Sauerteig
-----------------

<div style="background: #f9f9f9; padding: 20px; border-radius: 8px; border: 1px solid #ddd;">
  <label>Anzahl Pizzen:</label><br>
  <input type="number" id="n_pizza" value="2" style="width: 100%; margin-bottom: 10px;">
  
  <label>Gewicht pro Pizza [g]:</label><br>
  <input type="number" id="w_pizza" value="280" style="width: 100%; margin-bottom: 10px;">
 
  <label>Hydration [%]:</label><br>
  <input type="number" id="hydration" value="70" style="width: 100%; margin-bottom: 10px;">
  
  <label>Anteil Vorteig [%]:</label><br>
  <input type="number" id="starter_fraction" value="20" style="width: 100%; margin-bottom: 10px;">
  
  <button onclick="runMath()" style="padding: 10px 20px; cursor: pointer;">Berechnen</button>
</div>

**Zutaten gesamt**
<span id="w_flour_total">---</span> g <strong>Mehl</strong> 
<span id="w_water_total">---</span> g <strong>Wasser</strong> 
<span id="w_salt_total">---</span> g <strong>Salz</strong> 
<span id="w_sour">---</span> g <strong>Sauerteig</strong> 

**Zutaten Vorteig**
<span id="w_sour">---</span> g <strong>Sauerteig</strong> 
<span id="w_flour_starter">---</span> g <strong>Mehl</strong> 
<span id="w_water_starter">---</span> g <strong>Wasser</strong> 

**Zutaten Hauptteig**
<strong>Vorteig</strong> 
<span id="w_flour_main">---</span> g <strong>Mehl</strong> 
<span id="w_water_main">---</span> g <strong>Wasser</strong> 
<span id="w_salt_total">---</span> g <strong>Salz</strong> 

**Teigführung**
* 4-5 Tage vorher: Sauerteig füttern
* 3 Tage vorher: Vorteig anrühren, 3h gehen lassen
* Hauptteig anrühreren, 10-20 Min kneten, mit feuchtem Tuch bedecken
* Insgesamt 3h gehen lassen, alle 1h stretch and fold
* Bälle machen, 72h in Kühlschrank
* 2-3h vorm Backen Bälle auf Zimmertemperatur wärmen lassen

**Ofen**
* 400°C oben
* 350°C unten
* 2 Min

<script>
function runMath() {
  // 1. Grab values from the inputs
  const n = parseFloat(document.getElementById('n_pizza').value);
  const w = parseFloat(document.getElementById('w_pizza').value);
  const h = parseFloat(document.getElementById('hydration').value);
  const f = parseFloat(document.getElementById('starter_fraction').value);

  // Total numbers
  const w_total = n*w*1.1
  const w_flour_total = w_total/(1+h/100)
  const w_water_total = w_flour_total*h/100
  const w_salt_total = w_flour_total * 0.03
  const w_starter = w_total * f/100
  const w_sour = 0.2 * w_starter
  const w_flour_starter = 0.4 * w_starter
  const w_water_starter = 0.4 * w_starter
  const w_flour_main = w_flour_total - (0.5 * w_starter)
  const w_water_main = w_water_total - (0.5 * w_starter)

  // Collect results
  document.getElementById('w_flour_total').innerText = w_flour_total.toFixed(0);
  document.getElementById('w_water_total').innerText = w_water_total.toFixed(0);
  document.getElementById('w_salt_total').innerText = w_salt_total.toFixed(0);
  document.getElementById('w_sour').innerText = w_sour.toFixed(0);
  document.getElementById('w_flour_starter').innerText = w_flour_starter.toFixed(0);
  document.getElementById('w_water_starter').innerText = w_water_starter.toFixed(0);
  document.getElementById('w_flour_main').innerText = w_flour_main.toFixed(0);
  document.getElementById('w_water_main').innerText = w_water_main.toFixed(0);
}
</script>



[🏠 Home](./../)