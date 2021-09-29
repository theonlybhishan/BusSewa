
$(document).ready(function(){
    $("#sld").datepicker({
        minDate: 0,
        maxDate: 3,
    });
});


// seat selectiion section
var busId
var busName
var busPrice
const container = document.querySelector('.select-container');
const seats = document.querySelectorAll('.seat-row .seat:not(.occupied)');
const count= document.getElementById('count');
const total = document.getElementById('total');
const price = document.getElementById('fare');
// const amountbtn = document.getElementById('book-btn');
// console.log(amountbtn.value);
// let ticketPrice = +price.value;
let ticketPrice = busPrice
// const ticketPrice = ticketPrice;
// console.log(ticketPrice);
const selectedSeats = document.querySelectorAll('.seat-row .seat.selected');
console.log('selectedSeats:',selectedSeats)



// update total and count
function updateSelectedCount(){
    const selectedSeats = document.querySelectorAll('.seat-row .seat.selected');
    const seatsIndex = [...selectedSeats].map(function(seat){
        return[...seats].indexOf(seat);
    });
    localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));
    // console.log(seatsIndex)

    const selectedSeatsCount = selectedSeats.length;
    console.log(selectedSeatsCount);
    count.innerText = selectedSeatsCount;
    total.innerText = selectedSeatsCount*ticketPrice;
}

function myfunc(myvar){
    let ans = myvar.attributes.for.value;
    console.log('ans',ans)
    movieTitle = myvar.getAttribute('data-busName')
    console.log(movieTitle)
    let ans1= ans.split("#");
    var iterator = ans1.values();
    ticketPrice= iterator.next().value;
    updateSelectedCount();
}

const modalBtns = [...document.getElementsByClassName('modal-button')];
                                    // console.log(modalBtns)
const modalHeading = document.getElementById('heading');
// console.log(modalHeading)



modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=>{
    busId = modalBtn.getAttribute('data-busId');
    busName = modalBtn.getAttribute('data-busName');
    console.log ('seats',seats)
    // all_seats = modalBtn.querySelectorAll('.seat-row .seat')
    // console.log ('all_seats',all_seats)
    const routeId = modalBtn.getAttribute('data-routeId');
    const busSeat = modalBtn.getAttribute('data-busSeat');
    const seatType = modalBtn.getAttribute('data-seatType');
    busPrice= modalBtn.getAttribute('data-busPrice');

    localStorage.setItem('selectedBusIndex',busId);
    localStorage.setItem('selectedBusPrice',busPrice);
    modalHeading.innerHTML=`
    <p class="text-center" id="heading"><b> Select ${busName} Seat</b></p>
    `
    // return busName
}))

// console.log(modalBtns.busName)



container.addEventListener('click',(e)=>{
    if(e.target.classList.contains('seat') && !e.target.classList.contains('occupied')){
        e.target.classList.toggle('selected')
    }
    updateSelectedCount();
})


// modal clear after closing()

$(document).ready(function() {
    $('#mymodal').on('hidden.bs.modal', function() {
      history.go(0);
    });
  });