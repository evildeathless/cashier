const tbnCalcular = document.getElementById('sp');
const totals = document.getElementById('total').textContent;
const val = document.getElementById('rec');
const sob = document.getElementById('sob');
const fal = document.getElementById('fal');
const total = totals.split(" ");

tbnCalcular.addEventListener('click', () => {
  if(val.value != ""){
    let temp = val.value - total[1];
    if(temp > 0){
      sob.textContent = "SOBRANTE: " + (temp) + " PEN";
      fal.textContent = "FALTANTE: 00.00 PEN"
    } else if(temp < 0){
      fal.textContent = "FALTANTE: " + (temp) + " PEN";
      sob.textContent = "SOBRANTE: 00.00 PEN"
    }
  }
})