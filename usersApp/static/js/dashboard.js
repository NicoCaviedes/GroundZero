const panels = document.querySelectorAll( '.panel' );
const btnNavCol = document.getElementById('nav-btn-collapse')
const delayInMilliseconds = 345;
var flagBtnNav = false;
var cartIcon = document.getElementById('cart-icon')

panels.forEach( (panel) => {

    panel.addEventListener('click', () => {
        removeActiveClasses();
        panel.classList.add('active');
    } );

} );

function removeActiveClasses(){
    panels.forEach( panel => {
        panel.classList.remove('active');
    } )
}

btnNavCol.addEventListener('click', function() {
  console.log("Hola mundo")
  flagBtnNav = !flagBtnNav;
  if(flagBtnNav){
    cartIcon.classList.add("hidden");
  } else {
    setTimeout(function() {
        cartIcon.classList.remove("hidden");
    }, delayInMilliseconds);
  }
})