
const tipcalcy = () => {
  let amount = document.getElementById('bill_amount').value;

  let perc = document.getElementById('tip_perc').value;

  let no = document.getElementById('noofpeople').value;
  let total = (amount * (perc / 100))/no;
  document.getElementById('total_billed').value = total;
}














