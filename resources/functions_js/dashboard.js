const btnNavCol = document.getElementById('nav-btn-collapse')
const delayInMilliseconds = 345;
var flagBtnNav = false;
var cartIcon = document.getElementById('cart-icon')

btnNavCol.addEventListener('click', function() {
  flagBtnNav = !flagBtnNav;
  if(flagBtnNav){
    cartIcon.classList.add("hidden");
  } else {
    setTimeout(function() {
        cartIcon.classList.remove("hidden");
    }, delayInMilliseconds);
  }
})