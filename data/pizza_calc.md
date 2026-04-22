---
layout: page
title: Portionen-Rechner
---

### Menge anpassen
Gib die Anzahl der Personen ein: 
<input type="number" id="servings" value="4" oninput="calculate()">

* Mehl: <span class="calc-val" data-base="500">500</span>g
* Eier: <span class="calc-val" data-base="4">4</span> Stück

<script>
function calculate() {
  let factor = document.getElementById('servings').value / 4;
  document.querySelectorAll('.calc-val').forEach(span => {
    let base = span.getAttribute('data-base');
    span.innerText = (base * factor).toFixed(1);
  });
}
</script>
